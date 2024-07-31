let zoomLevel = 1;
let rotationAngle = 0;
let isDragging = false;
let positionX = 0;
let positionY = 0;
let startX = 0;
let startY = 0;

//var image_data = JSON.parse('{{ image_data|escapejs }}');

function rotateImage() {
    rotationAngle += 90;
    updateTransform();
}

function resetTransform() {
    zoomLevel = 1;
    rotationAngle = 0;
    positionX = 0;
    positionY = 0;
    updateTransform();
}

function updateTransform() {
    document.getElementById('selectedImage').style.transform = `scale(${zoomLevel}) rotate(${rotationAngle}deg) translate(${positionX}px, ${positionY}px)`;
}


document.querySelector(".editbtn").addEventListener('click', function () {
    document.querySelector('.popup').classList.add('active');
});

document.querySelector(".popup .close-btn").addEventListener('click', function () {
    document.querySelector('.popup').classList.remove('active');
});


document.querySelector(".deletebtn").addEventListener('click', function () {
    document.querySelector('.delete-popup').classList.add('active');
});

document.querySelector(".delete-popup .close-btn").addEventListener('click', function () {
    document.querySelector('.delete-popup').classList.remove('active');
});


document.querySelector(".delete-popup .cancel-btn").addEventListener('click', function () {
    document.querySelector('.delete-popup').classList.remove('active');
});



var idsList = document.getElementById('ids_list').value;
document.querySelector(".firstBtn").addEventListener('click', function () {
    console.log("First  button clicked");
    let firstDocId = this.getAttribute('data-item-id');
    if (firstDocId) {
        let newUrl = `/single-image/${firstDocId}/?ids=${encodeURIComponent(idsList)}`;
        window.location.href = newUrl;
    }
});

document.querySelector(".lastBtn").addEventListener('click', function () {
    console.log("last button.");
    let lastDocId = this.getAttribute('data-item-id');
    if (lastDocId) {
        let newUrl = `/single-image/${lastDocId}/?ids=${encodeURIComponent(idsList)}`;
        window.location.href = newUrl;
    }
});

document.querySelector(".prevBtn").addEventListener('click', function () {
    console.log("prev button.");
    let prevDocId = this.getAttribute('data-item-id');
    if (prevDocId) {
        let newUrl = `/single-image/${prevDocId}/?ids=${encodeURIComponent(idsList)}`;
        window.location.href = newUrl;
    }
});

document.querySelector(".nextBtn").addEventListener('click', function () {
    console.log("Next button clicked");
    let nextDocId = this.getAttribute('data-item-id');
    // console.log("Next document ID:", nextDocId);
    if (nextDocId) {
        let newUrl = `/single-image/${nextDocId}/?ids=${encodeURIComponent(idsList)}`;
        window.location.href = newUrl;
    }
});


function navigateImage(direction) {
    console.log("Navigating image:", direction);
    const imageDataLength = parseInt(document.getElementById('imageDataLength').value);
    let currentImageIndex = parseInt(document.getElementById('currentImageIndex').value);
    let ImageData = (document.getElementById('selectedImage').src);
    let ImageDataArr = document.getElementById('imageDataArr').value;

    // Calculate the new image index
    var newIndex = currentImageIndex + direction;
    console.log("New index 1:", newIndex);


    // Handle wrapping around for next and previous images
    if (newIndex < 0) {
        newIndex = imageDataLength - 1; // Wrap around to the last image
    } else if (newIndex >= imageDataLength) {
        newIndex = 0; // Wrap around to the first image
    }

    // Update the current image index
    document.getElementById('currentImageIndex').value = newIndex;
    console.log("currentImageIndex:", currentImageIndex);
    console.log("New index 2:", newIndex);
    console.log("Image data length:",  imageDataLength );
    console.log("Image data ----- :",  ImageData);



    var yyy = ImageDataArr.slice(1, -1);
    var xxx  = yyy.split(",");
    var zzz =[];

    xxx.forEach((element, index) => {
        // Remove the single quotes using replace()
        let cleanElement = element.trim().replace(/'/g, '');
        zzz.push(cleanElement);
        console.log(`The ${index + 1} is: ${cleanElement}`);
    });

    
//     debugger;
//     console.log('HHH',ImageDataArr)
//    var yyy = ImageDataArr.slice(3, -3);
//     var xxx  = yyy.split(",");
//     console.log('xxx',xxx)
//     var zzz =[];

//     xxx.forEach((element, index) => {
//         let cleanElement = element.replace(/'/g, '');
//         zzz.push(cleanElement);
//         console.log(`The ${index + 1} is: ${cleanElement}`);
//     });

    // Update the image source
    //document.getElementById('selectedImage').src = "data:image/jpeg;base64,{{ image_data }}.[newIndex]";
     //document.getElementById('selectedImage').src = "data:image/jpeg;base64," + image_data[newIndex];
     document.getElementById('selectedImage').src = "data:image/jpeg;base64," + zzz[newIndex];
     
    
    // Update the visibility of navigation buttons
    updateNavigationButtons(newIndex, imageDataLength);
}





function updateNavigationButtons(currentIndex, totalImages) {
    const prevImageBtn = document.querySelector(".prevImageBtn");
    const nextImageBtn = document.querySelector(".nextImageBtn");

    if (currentIndex === 0) {
        prevImageBtn.style.display = "none";
    } 
    // else {
    //     prevImageBtn.style.display = "block";
    // }

    else if (currentIndex === totalImages - 1) {
        nextImageBtn.style.display = "none";
        prevImageBtn.style.display = "block";

    } 
    else{
        prevImageBtn.style.display = 'block';
        nextImageBtn.style.display = 'block';
    // else {
    //     nextImageBtn.style.display = "block";
    // }
}
}
