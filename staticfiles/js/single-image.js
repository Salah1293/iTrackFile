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

document.querySelector(".popup .cancel-btn").addEventListener('click', function () {
    document.querySelector('.popup').classList.remove('active');
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
    console.log("First  button clicked", section); 
    console.log("last button.", section.value); 
    let firstDocId = this.getAttribute('data-item-id');
    if (firstDocId) {
        let newUrl = `/single-image/${section.value}/${firstDocId}/?ids=${encodeURIComponent(idsList)}`;
        window.location.href = newUrl;
    }
});

document.querySelector(".lastBtn").addEventListener('click', function () {
    console.log("last button.", section); 
    console.log("last button.", section.value); 
    let lastDocId = this.getAttribute('data-item-id');
    if (lastDocId) {
        let newUrl = `/single-image/${section.value}/${lastDocId}/?ids=${encodeURIComponent(idsList)}`;
        window.location.href = newUrl;
    }
});

document.querySelector(".prevBtn").addEventListener('click', function () {
    console.log("prev button.", section); 
    console.log("last button.", section.value); 
    let prevDocId = this.getAttribute('data-item-id');
    if (prevDocId) {
        let newUrl = `/single-image/${section.value}/${prevDocId}/?ids=${encodeURIComponent(idsList)}`;
        window.location.href = newUrl;
    }
});
document.addEventListener('DOMContentLoaded', function () {
    document.body.addEventListener('click', function (e) {
        if (e.target && e.target.classList.contains('nextBtn')) {
            console.log("Next button clicked. Current section:", section.value); 

            let nextDocId = e.target.getAttribute('data-item-id');
            console.log("Next document ID:", nextDocId);

            if (nextDocId) {
                let newUrl = `/single-image/${section.value}/${nextDocId}/?ids=${encodeURIComponent(idsList)}`;
                console.log("Navigating to:", newUrl);

                window.location.href = newUrl;
            } else {
                console.log("No nextDocId found, unable to navigate.");
            }
        }
    });
});


// document.querySelector(".nextBtn").addEventListener('click', function () {
//     console.log("Next button clicked", section); 
//     console.log("last button.", section.value); 
//     let nextDocId = this.getAttribute('data-item-id');
//     if (nextDocId) {
//         let newUrl = `/single-image/${section.value}/${nextDocId}/?ids=${encodeURIComponent(idsList)}`;
//         window.location.href = newUrl;
//     }
// });




// document.querySelector(".nextBtn").addEventListener('click', function () {
//     console.log("Next button clicked");
//     let nextDocId = this.getAttribute('data-item-id');
//     console.log("Next document ID:", nextDocId);
//     // Check if `nextDocId` is correctly retrieved and the URL generation works as expected
//     if (nextDocId) {
//         let newUrl = `/single-image/${section.value}/${nextDocId}/?ids=${encodeURIComponent(idsList)}`;
//         console.log("New URL:", newUrl);
//         // Ensure the new URL is correct and navigate to it
//         window.location.href = newUrl;
//     }
// });




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
        console.log(`The ${index + 1} is: ${cleanElement}`);
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




let draggableElem = document.getElementById('drag-handle');
let  initialX = 0, initialy = 0;
let moveElement = false

let events = {
    mouse: {
        down: 'mousedown',
        move: 'mousemove',
        up: 'mouseup'
    },
    touch: {
        down: 'touchstart',
        move: 'touchmove',
        up: 'touchend'
    }
}

let deviceType = '';

const isTouchDevide = () => {
    try{
        document.createEvent('TouchEvent');
        deviceType = 'touch';
        return true;
    }
    catch(e) {
        deviceType = 'mouse';
        return false;
    }
};

isTouchDevide();
draggableElem.addEventListener(events[deviceType].down,
    (e) => {
        e.preventDefault();
        initialX = !isTouchDevide() ? e.clientx : touches[0].
        clientx;
        initialy = !isTouchDevide() ? e.clienty : touches[0].
        clienty;

        moveElement = true;
    });


    draggableElem.addEventListener(events[deviceType].move,
        (e) => {
            if(moveElement) {
                e.preventDefault();
                let newx = !isTouchDevide() ? e.clientx : e.touches
                [0].clientx;
                let newy = !isTouchDevide() ? e.clienty : e.touches
                [0].clienty;

                draggableElem.style.top = 
                draggableElem.offsetTop - (initialy - newy) + 'px';
                draggableElem.style.left = 
                draggableElem.offsetLeft - (initialx - newx) + 'px';
                initialX = newx;
                initialy = newy;
            }
        });


    draggableElem.addEventListener(
        events[deviceType].up,
        (stopMovement = (e) => {
            moveElement = false
        })
    );


    draggableElem.addEventListener('mouseleave',
        stopMovement);

    draggableElem.addEventListener(events[deviceType].up,
        (e) => {
            moveElement = false;
        }
    );
        


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


