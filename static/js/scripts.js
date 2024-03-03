
function resetForm(){
    document.getElementById('myForm').reset();
}



let zoomLevel = 1;
let rotationAngle = 0;
let isDragging = false;
let positionX = 0;
let positionY = 0;
let startX = 0;
let startY = 0;

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