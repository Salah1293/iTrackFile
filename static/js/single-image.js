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
//     console.log("Edit button clicked");
//     document.querySelector('.popup').classList.add('active');
//     const fields = document.querySelectorAll('.popup input, .popup textarea');
//     fields.forEach(field => console.log(`${field.name}: ${field.disabled}`));
// });



// // document.querySelector(".editbtn").addEventListener('click', function () {
// //     document.querySelector('.popup').classList.add('active');
// // });

// document.querySelector(".popup .close-btn").addEventListener('click', function () {
//     document.querySelector('.popup').classList.remove('active');
// });


// document.querySelector(".deletebtn").addEventListener('click', function () {
//     console.log('delete btn fired')
//     document.querySelector('.delete-popup').classList.add('active');
// });

// document.querySelector(".delete-popup .close-btn").addEventListener('click', function () {
//     document.querySelector('.delete-popup').classList.remove('active');
// });


// document.querySelector(".delete-popup .cancel-btn").addEventListener('click', function () {
//     document.querySelector('.delete-popup').classList.remove('active');
// });

// document.querySelector(".popup .cancel-btn").addEventListener('click', function () {
//     document.querySelector('.popup').classList.remove('active');
// });



// document.querySelector(".printbtn").addEventListener('click', function () {
//     populatePrintOptions();
//     document.querySelector('.print-popup').classList.add('active');
// });


// document.querySelector(".print-popup .close-btn").addEventListener('click', function () {
//     document.querySelector('.print-popup').classList.remove('active');
// });


// document.querySelector(".print-popup .cancel-btn").addEventListener('click', function () {
//     document.querySelector('.print-popup').classList.remove('active');
// });



// var idsList = document.getElementById('ids_list').value;
// document.querySelector(".firstBtn").addEventListener('click', function () {
//     let firstDocId = this.getAttribute('data-item-id');
//     if (firstDocId) {
//         let newUrl = `/single-image/${section.value}/${firstDocId}/?ids=${encodeURIComponent(idsList)}`;
//         window.location.href = newUrl;
//     }
// });

// document.querySelector(".lastBtn").addEventListener('click', function () {
//     let lastDocId = this.getAttribute('data-item-id');
//     if (lastDocId) {
//         let newUrl = `/single-image/${section.value}/${lastDocId}/?ids=${encodeURIComponent(idsList)}`;
//         window.location.href = newUrl;
//     }
// });

// document.querySelector(".prevBtn").addEventListener('click', function () {
//     let prevDocId = this.getAttribute('data-item-id');
//     if (prevDocId) {
//         let newUrl = `/single-image/${section.value}/${prevDocId}/?ids=${encodeURIComponent(idsList)}`;
//         window.location.href = newUrl;
//     }
// });
// document.addEventListener('DOMContentLoaded', function () {
//     document.body.addEventListener('click', function (e) {
//         if (e.target && e.target.classList.contains('nextBtn')) {

//             let nextDocId = e.target.getAttribute('data-item-id');

//             if (nextDocId) {
//                 let newUrl = `/single-image/${section.value}/${nextDocId}/?ids=${encodeURIComponent(idsList)}`;

//                 window.location.href = newUrl;
//             } else {
//                 console.log("No nextDocId found, unable to navigate.");
//             }
//         }
//     });
// });




// function navigateImage(direction) {
//     const imageDataLength = parseInt(document.getElementById('imageDataLength').value);
//     let currentImageIndex = parseInt(document.getElementById('currentImageIndex').value);
//     let ImageData = (document.getElementById('selectedImage').src);
//     let ImageDataArr = document.getElementById('imageDataArr').value;

   
//     var newIndex = currentImageIndex + direction;


    
//     if (newIndex < 0) {
//         newIndex = imageDataLength - 1; 
//     } else if (newIndex >= imageDataLength) {
//         newIndex = 0; 
//     }

//     document.getElementById('currentImageIndex').value = newIndex;
   


//     var yyy = ImageDataArr.slice(1, -1);
//     var xxx  = yyy.split(",");
//     var zzz =[];

//     xxx.forEach((element, index) => {
//         let cleanElement = element.trim().replace(/'/g, '');
//         zzz.push(cleanElement);
//     });

    
//      document.getElementById('selectedImage').src = "data:image/jpeg;base64," + zzz[newIndex];
     
    
//     updateNavigationButtons(newIndex, imageDataLength);
// }



// function updateNavigationButtons(currentIndex, totalImages) {
//     const prevImageBtn = document.querySelector(".prevImageBtn");
//     const nextImageBtn = document.querySelector(".nextImageBtn");

//     if (currentIndex === 0) {
//         prevImageBtn.style.display = "none";
//     } 


//     else if (currentIndex === totalImages - 1) {
//         nextImageBtn.style.display = "none";
//         prevImageBtn.style.display = "block";

//     } 
//     else{
//         prevImageBtn.style.display = 'block';
//         nextImageBtn.style.display = 'block';

// }
// }



// function populatePrintOptions() {
//     const imageDataArr = document.getElementById('imageDataArr').value.slice(1, -1).split(', ').map(item => item.replace(/'/g, '')).filter(item => item); 
//     const printImagesContainer = document.getElementById('print-images-container');
//     printImagesContainer.innerHTML = ''; 

//     imageDataArr.forEach((imageData, index) => {
//         const imageNumber = index + 1; 
//         const optionDiv = document.createElement('div');
//         optionDiv.classList.add('print-option');

//         const checkbox = document.createElement('input');
//         checkbox.type = 'checkbox';
//         checkbox.id = `print-checkbox-${imageNumber}`;
//         checkbox.value = imageNumber;

//         const label = document.createElement('label');
//         label.htmlFor = `print-checkbox-${imageNumber}`;
//         label.innerText = `${imageNumber}`;

//         optionDiv.appendChild(checkbox);
//         optionDiv.appendChild(label);

//         printImagesContainer.appendChild(optionDiv);
//     });
// }




// function printImages() {
//     const checkedCheckboxes = document.querySelectorAll('#print-images-container input[type="checkbox"]:checked');
//     const imageDataArr = document.getElementById('imageDataArr').value.slice(1, -1).split(', ').map(item => item.replace(/'/g, ''));

//     if (checkedCheckboxes.length === 0) {
//         alert("Please select at least one image to print.");
//         return;
//     }

//     const printWindow = window.open('');
//     printWindow.document.write('<html><head><title>Print Images</title>');
//     printWindow.document.write('<style>');
//     printWindow.document.write(`
//         body, html {
//             margin: 0;
//             padding: 0;
//         }
//         img {
//             max-width: 100%;
//             height: 100%;
//             page-break-inside: avoid;
//         }
//         @media print {
//             img {
//                 max-width: 100%;
//                 height: 100%;
//             }
//         }
//     `);
//     printWindow.document.write('</style></head><body>');

//     checkedCheckboxes.forEach((checkbox, index) => {
//         if (index > 0) {
//             printWindow.document.write('<div style="page-break-before: always;"></div>');
//         }
        
//         const imageIndex = parseInt(checkbox.value, 10) - 1;
//         const imageData = imageDataArr[imageIndex];
//         const image = new Image();
//         image.src = `data:image/jpeg;base64,${imageData}`;

//         printWindow.document.write(image.outerHTML);
//     });

//     printWindow.document.write('</body></html>');
//     printWindow.document.close();
//     printWindow.print();

//     closePrintPopup();
// }










let zoomLevel = 1;
let rotationAngle = 0;

function rotateImage() {
    rotationAngle += 90;
    updateTransform();
}

function resetTransform() {
    zoomLevel = 1;
    rotationAngle = 0;
    updateTransform();
}

function updateTransform() {
    document.getElementById('selectedImage').style.transform = `scale(${zoomLevel}) rotate(${rotationAngle}deg)`;
}

document.querySelector(".editbtn").addEventListener('click', function () {
    console.log("Edit button clicked");
    document.querySelector('.popup').classList.add('active');
});

document.querySelector(".popup .close-btn").addEventListener('click', function () {
    document.querySelector('.popup').classList.remove('active');
});

const fields = document.querySelectorAll('.popup input, .popup textarea');
fields.forEach(field => {
    field.addEventListener('click', function () {
        console.log(`Field clicked: ${field.name}, Disabled: ${field.disabled}`);
    });
});

document.querySelector(".deletebtn").addEventListener('click', function () {
    console.log('Delete button clicked');
    document.querySelector('.delete-popup').classList.add('active');
});

document.querySelector(".delete-popup .close-btn").addEventListener('click', function () {
    document.querySelector('.delete-popup').classList.remove('active');
});

document.querySelector(".delete-popup .cancel-btn").addEventListener('click', function () {
    document.querySelector('.delete-popup').classList.remove('active');
});

document.querySelector(".printbtn").addEventListener('click', function () {
    populatePrintOptions();
    document.querySelector('.print-popup').classList.add('active');
});

document.querySelector(".print-popup .close-btn").addEventListener('click', function () {
    document.querySelector('.print-popup').classList.remove('active');
});

document.querySelector(".print-popup .cancel-btn").addEventListener('click', function () {
    document.querySelector('.print-popup').classList.remove('active');
});




var idsList = document.getElementById('ids_list').value;

document.querySelector(".firstBtn").addEventListener('click', function () {
    let firstDocId = this.getAttribute('data-item-id');
    if (firstDocId) {
        let newUrl = `/single-image/${section.value}/${firstDocId}/?ids=${encodeURIComponent(idsList)}`;
        window.location.href = newUrl;
    }
});

document.querySelector(".lastBtn").addEventListener('click', function () {
    let lastDocId = this.getAttribute('data-item-id');
    if (lastDocId) {
        let newUrl = `/single-image/${section.value}/${lastDocId}/?ids=${encodeURIComponent(idsList)}`;
        window.location.href = newUrl;
    }
});

document.querySelector(".prevBtn").addEventListener('click', function () {
    let prevDocId = this.getAttribute('data-item-id');
    if (prevDocId) {
        let newUrl = `/single-image/${section.value}/${prevDocId}/?ids=${encodeURIComponent(idsList)}`;
        window.location.href = newUrl;
    }
});


document.addEventListener('DOMContentLoaded', function () {
    document.body.addEventListener('click', function (e) {
        if (e.target && e.target.classList.contains('nextBtn')) {

            let nextDocId = e.target.getAttribute('data-item-id');

            if (nextDocId) {
                let newUrl = `/single-image/${section.value}/${nextDocId}/?ids=${encodeURIComponent(idsList)}`;

                window.location.href = newUrl;
            } else {
                console.log("No nextDocId found, unable to navigate.");
            }
        }
    });
});




function navigateImage(direction) {
    const imageDataLength = parseInt(document.getElementById('imageDataLength').value);
    let currentImageIndex = parseInt(document.getElementById('currentImageIndex').value);
    let ImageData = (document.getElementById('selectedImage').src);
    let ImageDataArr = document.getElementById('imageDataArr').value;

   
    var newIndex = currentImageIndex + direction;


    
    if (newIndex < 0) {
        newIndex = imageDataLength - 1; 
    } else if (newIndex >= imageDataLength) {
        newIndex = 0; 
    }

    document.getElementById('currentImageIndex').value = newIndex;
   


    var yyy = ImageDataArr.slice(1, -1);
    var xxx  = yyy.split(",");
    var zzz =[];

    xxx.forEach((element, index) => {
        let cleanElement = element.trim().replace(/'/g, '');
        zzz.push(cleanElement);
    });

    
     document.getElementById('selectedImage').src = "data:image/jpeg;base64," + zzz[newIndex];
     
    
    updateNavigationButtons(newIndex, imageDataLength);
}



function updateNavigationButtons(currentIndex, totalImages) {
    const prevImageBtn = document.querySelector(".prevImageBtn");
    const nextImageBtn = document.querySelector(".nextImageBtn");

    if (currentIndex === 0) {
        prevImageBtn.style.display = "none";
    } 


    else if (currentIndex === totalImages - 1) {
        nextImageBtn.style.display = "none";
        prevImageBtn.style.display = "block";

    } 
    else{
        prevImageBtn.style.display = 'block';
        nextImageBtn.style.display = 'block';

}
}



function populatePrintOptions() {
    const imageDataArr = document.getElementById('imageDataArr').value.slice(1, -1).split(', ').map(item => item.replace(/'/g, '')).filter(item => item); 
    const printImagesContainer = document.getElementById('print-images-container');
    printImagesContainer.innerHTML = ''; 

    imageDataArr.forEach((imageData, index) => {
        const imageNumber = index + 1; 
        const optionDiv = document.createElement('div');
        optionDiv.classList.add('print-option');

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.id = `print-checkbox-${imageNumber}`;
        checkbox.value = imageNumber;

        const label = document.createElement('label');
        label.htmlFor = `print-checkbox-${imageNumber}`;
        label.innerText = `${imageNumber}`;

        optionDiv.appendChild(checkbox);
        optionDiv.appendChild(label);

        printImagesContainer.appendChild(optionDiv);
    });
}




function printImages() {
    const checkedCheckboxes = document.querySelectorAll('#print-images-container input[type="checkbox"]:checked');
    const imageDataArr = document.getElementById('imageDataArr').value.slice(1, -1).split(', ').map(item => item.replace(/'/g, ''));

    if (checkedCheckboxes.length === 0) {
        alert("Please select at least one image to print.");
        return;
    }

    const printWindow = window.open('');
    printWindow.document.write('<html><head><title>Print Images</title>');
    printWindow.document.write('<style>');
    printWindow.document.write(`
        body, html {
            margin: 0;
            padding: 0;
        }
        img {
            max-width: 100%;
            height: 100%;
            page-break-inside: avoid;
        }
        @media print {
            img {
                max-width: 100%;
                height: 100%;
            }
        }
    `);
    printWindow.document.write('</style></head><body>');

    checkedCheckboxes.forEach((checkbox, index) => {
        if (index > 0) {
            printWindow.document.write('<div style="page-break-before: always;"></div>');
        }
        
        const imageIndex = parseInt(checkbox.value, 10) - 1;
        const imageData = imageDataArr[imageIndex];
        const image = new Image();
        image.src = `data:image/jpeg;base64,${imageData}`;

        printWindow.document.write(image.outerHTML);
    });

    printWindow.document.write('</body></html>');
    printWindow.document.close();
    printWindow.print();

    closePrintPopup();
}


