
function resetForm(){
    document.getElementById('myForm').reset();
}






// let zoomLevel = 1;
// let rotationAngle = 0;
// let isDragging = false;
// let positionX = 0;
// let positionY = 0;
// let startX = 0;
// let startY = 0;

// function rotateImage() {
//     rotationAngle += 90;
//     updateTransform();
// }

// function resetTransform() {
//     zoomLevel = 1;
//     rotationAngle = 0;
//     positionX = 0;
//     positionY = 0;
//     updateTransform();
// }

// function updateTransform() {
//     document.getElementById('selectedImage').style.transform = `scale(${zoomLevel}) rotate(${rotationAngle}deg) translate(${positionX}px, ${positionY}px)`;
// }


// document.querySelector(".editbtn").addEventListener('click', function () {
//     document.querySelector('.popup').classList.add('active');
// });

// document.querySelector(".popup .close-btn").addEventListener('click', function () {
//     document.querySelector('.popup').classList.remove('active');
// });


// document.querySelector(".deletebtn").addEventListener('click', function () {
//     document.querySelector('.delete-popup').classList.add('active');
// });

// document.querySelector(".delete-popup .close-btn").addEventListener('click', function () {
//     document.querySelector('.delete-popup').classList.remove('active');
// });


// function redirectToSingleImage(docId, allIds) {  
//     var idsArray = allIds.split(',');
//     // it's better to use encodeURIComponent() to ensure that special characters in the IDs are properly encoded.
//     let idsParam = encodeURIComponent(idsArray.join(','));
//     window.location.href = `/single-image/${docId}/?ids=${idsParam}`;
//   }



// window.onload = function(){
//     document.querySelector('.firstBtn').addEventListener('click', function(){
//         navigateImage('{{first_doc}}');
//     });
//     document.querySelector('.lastBtn').addEventListener('click', function(){
//         navigateImage('{{last_doc}}');
//     });
//     document.querySelector('.prevBtn').addEventListener('click', function(){
//         navigateImage('{{prev_doc}}');
//     });
//     document.querySelector('.nextBtn').addEventListener('click', function(){
//         navigateImage('{{next_doc}}');
//     });
// };

// function navigateImage(id){
//     window.location.href = `/single-image/${id}`;
// }