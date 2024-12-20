

function createBundle() {
    var selectedImage = document.getElementById('selectedImage');
    var form = document.getElementById('myform');
 

    if (!form) {
        return;
    }

    if (!selectedImage || !selectedImage.src) {
        return;
    }

    var currentImage = selectedImage.src;
  

    var imageName = currentImage.split('/').pop();

    var formData = new FormData(form); 
    formData.append('imageName', imageName); 
   

    fetch('/capture/create-bundle/', {  
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken')  
        }
    })
    .then(response => {
        if (response.ok) {
            return response.json();  
        } else {
            return response.text().then(text => {  
                throw new Error('Server error: ' + response.status + ' - ' + text);
            });
        }
    })
    .then(data => {
        if (data.success) {

            const newImages = data.unbundled_images;  
            const mediaUrl = data.media_url;  
            const batchId = data.batch_id; 

            form.reset();  
            reloadImages(newImages, mediaUrl, batchId); 
            reloadBundleIcons(data.bundle_ids); 
        } else {
            console.error('Error:', data.error);
        }
    })
    .catch((error) => {
        console.error('Error:', error); 
    });
}



function reloadBundleIcons(bundleIds) {
    var bundleIconsContainer = document.querySelector('.bundle-icons-container');

    while (bundleIconsContainer.children.length > 1) {
        bundleIconsContainer.removeChild(bundleIconsContainer.lastChild);
    }

    bundleIds.forEach(function(bundleId) {
        var newIcon = document.createElement('div');
        newIcon.className = 'bundle-icon';
        newIcon.style.margin = '4px';
        newIcon.style.display = 'flex';
        newIcon.style.justifyContent = 'center';
        newIcon.style.alignItems = 'center';

        var newButton = document.createElement('button');
        newButton.className = 'btn btn--icon';
        newButton.style.width = '30px';
        newButton.style.height = '30px';
        newButton.style.padding = '0';
        newButton.setAttribute('data-bundle-id', bundleId);  
        newButton.onclick = function() {
            sendBundleData(bundleId); 
        };

        var icon = document.createElement('i');
        icon.className = 'fas fa-box'; 

        newButton.appendChild(icon);
        newIcon.appendChild(newButton);
        bundleIconsContainer.appendChild(newIcon);
    });
}



function reloadImages(unbundledImages, mediaUrl, batchId) {
    const scrollableImagesContainer = document.getElementById('scrollableImages');
    
    scrollableImagesContainer.innerHTML = '';

    unbundledImages.forEach(image => {
        const img = document.createElement('img');
        img.src = `${mediaUrl}batch_${batchId}/${image}`; 
        img.alt = "image";
        img.className = "scrollable-image";
        img.onclick = () => displayImage(img);

        scrollableImagesContainer.appendChild(img);
    });
}



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


let savedBundleId; 

function getBundleId(bundleId) {
    savedBundleId = bundleId; 
}


function sendBundleData(bundleId, batchId) {

    var batchid = document.getElementById('batchid').value;

    
    const csrfToken = '{{ csrf_token }}';  
    getBundleId(bundleId);

    fetch(`/capture/bundle-data/${bundleId || 'unbundled'}/${batchid}/`, {  
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken, 
        },
        body: JSON.stringify({
            "bundle_id": bundleId, 
            "batch_id": batchid
        })
    })
    .then(response => {
        if (!response.ok) {
            console.error(`Error: ${response.status} ${response.statusText}`);
            return response.text(); 
        }
        return response.json(); 
    })
    .then(data => {
        const newImages = data.images;  
        const mediaUrl = data.media_url;  
        const result = data.result; 

        updateImages(newImages, mediaUrl, batchid, bundleId);
        fillFormWithResult(result);

        const bundleButtons = document.querySelectorAll('.bundle-icon button');
        bundleButtons.forEach(button => {
        button.classList.remove('selected-bundle');
        });

        const selectedButton = document.querySelector(`button[data-bundle-id="${bundleId}"]`);
        if (selectedButton) {
        selectedButton.classList.add('selected-bundle');
        selectedBundleButton = selectedButton;
        } else {
        selectedBundleButton = null;
        }

    })
    .catch((error) => {
        console.error("Error:", error);
    });
}


function updateImages(newImages, mediaUrl, batchId, bundleId) {
    const scrollableImages = document.getElementById('scrollableImages');
    getBundleId(bundleId)
    scrollableImages.innerHTML = '';  

    const imagePathPrefix = bundleId 
        ? `batch_${batchId}/bundle_${bundleId}/` 
        : `batch_${batchId}/`;

    newImages.forEach(image => {
        const imgElement = document.createElement('img');
        imgElement.src = `${mediaUrl}${imagePathPrefix}${image}`; 
        imgElement.className = 'scrollable-image';
        imgElement.alt = 'image';
        imgElement.onclick = function() { displayImage(this); };

        scrollableImages.appendChild(imgElement);
    });
}


function fillFormWithResult(result) {
    const formInputs = document.querySelectorAll("input[type='text'], textarea");  
    formInputs.forEach(input => {
        input.value = "";  
    });

    for (const field in result) {
        const input = document.querySelector(`[name="${field}"]`);  
        if (input) {
            input.value = result[field]; 
        }
    }
}


document.addEventListener("DOMContentLoaded", function () {
    const confirmBundleBtn = document.getElementById("confirmBundleBtn");
    var form = document.getElementById('myform');

    confirmBundleBtn.addEventListener("click", function () {
        const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;


        var currentImage = selectedImage.src;

        var imageName = currentImage.split('/').pop();
        const formData = new FormData(form);

        if (savedBundleId === null) {
            if (imageName) {  
                formData.append('imageName', imageName);
            } else {
                console.error("No selected image found.");
            }
        }
        else{
            formData.append('bundle_id', savedBundleId);
        }


        fetch('/capture/submit-bundle/', {
            method: "POST",
            headers: {
                "X-CSRFToken": csrfToken, 
            },
            body: formData 
        })
        .then(response => response.json())
        .then(data => {

            clearForm(form);  
            removeSubmittedBundleIcon(data.bundleid);

            if (data.unbundled_images && data.unbundled_images.length > 0) {
                reloadUnbundledImages(data.unbundled_images, data.media_url, data.batch_id);
            }

        })
        .catch((error) => {
            console.error("Error:", error);
        });
    });
});



function removeSubmittedBundleIcon(bundleId) {
    if (bundleId === null) {
        return;
    }

    const bundleButton = document.querySelector(`button[data-bundle-id="${bundleId}"]`);

    if (bundleButton) {
        const bundleIconDiv = bundleButton.parentElement;  
        bundleIconDiv.remove();  
    } 
}


function reloadUnbundledImages(unbundledImages, mediaUrl, batchId) {
    const scrollableImagesContainer = document.getElementById('scrollableImages');
    
    scrollableImagesContainer.innerHTML = '';

    unbundledImages.forEach(image => {
        const img = document.createElement('img');
        img.src = `${mediaUrl}batch_${batchId}/${image}`;
        img.alt = "image";
        img.className = "scrollable-image";
        img.onclick = () => displayImage(img);

        scrollableImagesContainer.appendChild(img);
    });
}



function clearForm(form) {
    Array.from(form.elements).forEach((element) => {
        if (element.tagName === "INPUT") {
            if (element.type !== "hidden") {  
                if (element.type === "text" || element.type === "file") {
                    element.value = "";  
                } else if (element.type === "checkbox" || element.type === "radio") {
                    element.checked = false; 
                }
            }
        } else if (element.tagName === "SELECT") {
            element.selectedIndex = 0;  
        } else if (element.tagName === "TEXTAREA") {
            element.value = "";  
        }
    });
}


document.addEventListener("DOMContentLoaded", function () {


    const selectedImage = document.getElementById("selectedImage");
    const scrollableImages = document.getElementById("scrollableImages");

    let currentImageIndex = 0;

    var currentImage = selectedImage.src;
    var imageName = currentImage.split('/').pop();

    

    window.displayImage = function (img) {
        selectedImage.src = img.src;
        currentImageIndex = Array.from(scrollableImages.children).indexOf(img);
        
        const images = scrollableImages.querySelectorAll('.scrollable-image');
        images.forEach(image => image.classList.remove('selected-image'));

        img.classList.add('selected-image');
        
        
        currentImage = selectedImage.src;
        imageName = currentImage.split('/').pop();
       
    };

    document.getElementById("deleteBtn").addEventListener("click", function () {

        if (scrollableImages.children.length > 0) {
            const imageToDelete = scrollableImages.children[currentImageIndex];
            const imageUrl = imageToDelete.src.split(window.location.origin)[1]; 
            
            const imageNameToDelete = imageUrl.split('/').pop();

            var form = document.getElementById('myform');
            var formData = new FormData(form);
            const batchId = formData.get('batch_id');



            fetch('/capture/delete-image/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(), 
                },
                body: JSON.stringify({ imageName: imageNameToDelete ,
                     batchid: batchId })
            })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {

                        scrollableImages.removeChild(imageToDelete);

                        if (currentImageIndex >= scrollableImages.children.length) {
                            currentImageIndex = scrollableImages.children.length - 1;
                        }

                        if (scrollableImages.children.length > 0) {
                            selectedImage.src = scrollableImages.children[currentImageIndex].src;
                        } else {
                            selectedImage.src = ""; 
                        }
                    } else {
                        console.error("Error deleting image:", data.error);
                    }
                })
                .catch(error => console.error("Error:", error));
        }
    });

    function getCSRFToken() {
        const name = "csrftoken";
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + "=")) {
                return cookie.substring(name.length + 1);
            }
        }
        return "";
    }


    let zoomLevel = 1;
    document.getElementById("zoomInBtn").addEventListener("click", function () {
        zoomLevel += 0.1;
        selectedImage.style.transform = `scale(${zoomLevel})`;
    });

    document.getElementById("zoomOutBtn").addEventListener("click", function () {
        if (zoomLevel > 0.2) {
            zoomLevel -= 0.1;
            selectedImage.style.transform = `scale(${zoomLevel})`;
        }
    });

    let rotateAngle = 0;
    document.getElementById("rotateBtn").addEventListener("click", function () {
        rotateAngle += 90;
        selectedImage.style.transform = `rotate(${rotateAngle}deg) scale(${zoomLevel})`;
    });

    document.getElementById("resetBtn").addEventListener("click", function () {
        zoomLevel = 1;
        rotateAngle = 0;
        selectedImage.style.transform = `rotate(0deg) scale(1)`;
    });
});





