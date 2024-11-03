


function createBundle() {
    var selectedImage = document.getElementById('selectedImage');
    var form = document.getElementById('myform');

    // Check if form exists
    if (!form) {
        console.error("Form not found.");
        return;
    }

    // Check if selected image exists
    if (!selectedImage || !selectedImage.src) {
        console.error("No image selected or #selectedImage not found.");
        return;
    }

    var currentImage = selectedImage.src;
    console.log("Image displayed is:", currentImage);
    console.log("form data is:", form);

    // Extract the image file name from the URL
    var imageName = currentImage.split('/').pop();

    // Collect form data
    var formData = new FormData(form);  // Create FormData object from form element
    formData.append('imageName', imageName);  // Add the image name to the form data
    console.log("form data is:", formData);

    for (var pair of formData.entries()) {
        console.log(pair[0]+ ': ' + pair[1]);
    }


    console.log('Sending form data to /capture/create-batch/');

    // Fetch function to send the data to the backend view
    fetch('/capture/create-bundle/', {  
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken')  // Add CSRF token to the headers
        }
    })
    // console.log('ajx sent successfully')
    .then(response => {
        console.log('Response received:', response);
        if (response.ok) {
            return response.json();  // Parse the response as JSON if successful
        } else {
            return response.text().then(text => {  // Get response text for error details
                throw new Error('Server error: ' + response.status + ' - ' + text);
            });
        }
    })
    .then(data => {
        if (data.success) {
            console.log('Success:', data.message);
            form.reset();  // Reset the form upon success
            // Optional: Clear the selected image if desired
            // selectedImage.src = '';  
        } else {
            console.error('Error:', data.error);
        }
    })
    .catch((error) => {
        console.error('Error:', error);  // Catch network or other unexpected errors
    });
}






// Helper function to get CSRF token (Django-specific)
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



// function deleteImage(currentImage, deleteUrl, csrfToken) {
//     console.log('Deleted image is:', currentImage);

//     if (currentImage) {
//         fetch(deleteUrl, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//                 'X-CSRFToken': csrfToken,
//             },
//             body: JSON.stringify({
//                 deleteUrl: currentImage
//             })
//         })
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error(`Error: ${response.status} ${response.statusText}`);
//             }
//             return response.json();
//         })
//         .then(data => {
//             if (data.success) {
//                 removeImageFromList(currentImage);
//                 console.log('Delete action succeeded');
                
//                 // Call reloadImages with the updated images list and media URL
//                 reloadImages(data.newImages, data.media_url);
//             }
//         })
//         .catch(error => {
//             console.error("Delete Error:", error);
//         });
//     }
// }

// // Usage example
// document.getElementById('deleteBtn').addEventListener('click', function () {
//     const currentImage = document.getElementById('selectedImage').getAttribute('src');
//     const deleteUrl = '/capture/delete-image/';  // Update with your actual URL
//     const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

//     deleteImage(currentImage, deleteUrl, csrfToken);
// });

// function reloadImages(images, mediaUrl) {
//     const scrollableImagesContainer = document.getElementById('scrollableImages');
//     scrollableImagesContainer.innerHTML = '';

//     images.forEach(image => {
//         const img = document.createElement('img');
//         img.src = `${mediaUrl}/${image}`;  
//         img.alt = "image";
//         img.className = "scrollable-image";
//         img.style.maxWidth = "65px";
//         img.style.maxHeight = "65px";
//         img.style.margin = "4px";
//         img.style.objectFit = "cover";
        
//         img.onclick = () => displayImage(img);

//         scrollableImagesContainer.appendChild(img);
//     });
// }



$(document).ready(function () {
    $('#importButton').on('click', function () {
        $('#imageInput').click();
    });



    $('#imageInput').on('change', function () {
        console.log('fired!')
        let formData = new FormData($('#uploadForm')[0]);
        $.ajax({
            url: uploadUrl,
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function (data) {
                console.log("AJAX Success:", data);
                displayImages(data.uploaded_images);
                appendHiddenFields(data.uploaded_images);
            },
            error: function (xhr, status, error) {
                console.error("AJAX Error:", status, error);
            }
        });
    });

    $('#scanButton').on('click', function () {
        console.log("scan button clicked");
        $.ajax({
            url: scanUrl,
            type: 'POST',
            data: { source: 'scan' },
            success: function (data) {
                console.log("Scan Success:", data);
                displayImages(data.uploaded_images);
                appendHiddenFields(data.uploaded_images);
                console.log('fired')
            },
            error: function (xhr, status, error) {
                console.error("Scan Error:", status, error);
            }
        });
    });

    // $('#deleteBtn').on('click', function () {
    //     let currentImage = $('#selectedImage').attr('src');
    //     console.log('deleted image is:', currentImage)
    //     if (currentImage) {
    //         $.ajax({
    //             url: deleteUrl,
    //             type: 'POST',
    //             data: {
    //                 deleteUrl: currentImage,
    //                 csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
    //             },
    //             success: function (data) {
    //                 if (data.success) {
    //                     removeImageFromList(currentImage);
    //                     console.log('delete action successed')
    //                 }
    //             },
    //             error: function (xhr, status, error) {
    //                 console.error("Delete Error:", status, error);
    //             }
    //         });
    //     }
    // });

   

    $('#deleteBtn').on('click', function () {
        let currentImage = $('#selectedImage').attr('src');
        console.log('Deleted image is:', currentImage);
    
        if (currentImage) {
            $.ajax({
                url: deleteUrl,
                type: 'POST',
                data: {
                    deleteUrl: currentImage,
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
                },
                success: function (data) {
                    if (data.success) {
                        removeImageFromList(currentImage);
                        console.log('Delete action succeeded');
                        // removeImageFromList(data.imageUrl)
                        // displayImages(data.uploaded_images);
                        
                        // Call reloadImages with the updated images list and media URL
                        // reloadImages(data.newImages, data.media_url);
                    }
                },
                error: function (xhr, status, error) {
                    console.error("Delete Error:", status, error);
                }
            });
        }
    });
    
    // function reloadImages(images, mediaUrl) {
    //     const scrollableImagesContainer = document.getElementById('scrollableImages');
    //     scrollableImagesContainer.innerHTML = '';
    
    //     images.forEach(image => {
    //         const img = document.createElement('img');
    //         img.src = `${mediaUrl}/${image}`;
    //         img.alt = "image";
    //         img.className = "scrollable-image";
    //         img.style.maxWidth = "65px";
    //         img.style.maxHeight = "65px";
    //         img.style.margin = "4px";
    //         img.style.objectFit = "cover";
            
    //         img.onclick = () => displayImage(img);
    
    //         scrollableImagesContainer.appendChild(img);
    //     });
    // }



    function displayImages(images) {
        images.forEach(function (imageUrl, index) {
            console.log("fired")
            // Check if the image already exists to avoid duplication
            // if (!$("img[src='" + imageUrl + "']").length) {
            //     const imgElement = `<img src="${imageUrl}" class="scrollable-image" alt="image ${index + 1}" onclick="displayImage(this)">`;
            //     $('#scrollableImages').append(imgElement);
            // }
        });
    
        // Ensure at least one image is displayed
        if ($('#selectedImage').attr('src') === '' && images.length > 0) {
            $('#selectedImage').attr('src', images[0]);
        }
    
        // Attach the click event to the new images
        $(".scrollable-image").on("click", function () {
            $("#selectedImage").attr("src", $(this).attr("src"));
            resetTransform();  // This should reset any zoom/rotation transformations
        });
    }


    

    function appendHiddenFields(images) {
        images.forEach(function (imageUrl) {
            $('#uploadForm').append(`<input type="hidden" name="uploaded_images" value="${imageUrl}">`);
            console.log('images appended', images)
        });
    }

    function removeImageFromList(imageUrl) {
        let currentImageElement = $("img[src='" + imageUrl + "']");
        console.log('function removeImageFromList fired.')
    
        // Remove the image from the DOM
        currentImageElement.remove();
    
        let remainingImages = $(".scrollable-image");
    
        if (remainingImages.length > 0) {
            // If there are images left, select the next one
            let nextImage = remainingImages.first();
            $("#selectedImage").attr("src", nextImage.attr("src"));
        } else {
            // If no images are left, clear the selected image
            $("#selectedImage").attr("src", '');
        }
    }
    
    
    function displayNextImage() {
        let remainingImages = $('#scrollableImages img');
        console.log("Remaining images:", remainingImages.length); // Check number of remaining images
    
        if (remainingImages.length > 0) {
            let nextImage = $('#scrollableImages img:first').attr('src');
            console.log("Next image to display:", nextImage); // Log the next image URL
    
            if (nextImage) {
                $('#selectedImage').attr('src', nextImage);
            } else {
                $('#selectedImage').attr('src', '');
            }
        } else {
            console.log("No images left to display.");
            $('#selectedImage').attr('src', '');
        }
    }
    

    let zoomLevel = 1;
    let rotationAngle = 0;
    let positionX = 0;
    let positionY = 0;

    $('#zoomInBtn').on('click', function () {
        zoomLevel += 0.1;
        updateTransform();
    });

    $('#zoomOutBtn').on('click', function () {
        if (zoomLevel > 0.1) zoomLevel -= 0.1;
        updateTransform();
    });

    $('#rotateBtn').on('click', function () {
        rotationAngle = (rotationAngle + 90) % 360;
        updateTransform();
    });

    $('#resetBtn').on('click', function () {
        resetTransform();
    });

    function updateTransform() {
        $("#selectedImage").css(
            "transform",
            `scale(${zoomLevel}) rotate(${rotationAngle}deg) translate(${positionX}px, ${positionY}px)`
        );
    }

    function resetTransform() {
        zoomLevel = 1;
        rotationAngle = 0;
        positionX = 0;
        positionY = 0;
        updateTransform();
    }
});