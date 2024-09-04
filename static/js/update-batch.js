document.addEventListener("DOMContentLoaded", function () {
    const selectedImage = document.getElementById("selectedImage");
    const scrollableImages = document.getElementById("scrollableImages");

    let currentImageIndex = 0;

    window.displayImage = function (img) {
        selectedImage.src = img.src;
        currentImageIndex = Array.from(scrollableImages.children).indexOf(img);
    };

    document.getElementById("deleteBtn").addEventListener("click", function () {
        if (scrollableImages.children.length > 0) {
            scrollableImages.removeChild(scrollableImages.children[currentImageIndex]);

            if (currentImageIndex >= scrollableImages.children.length) {
                currentImageIndex = scrollableImages.children.length - 1;
            }

            if (scrollableImages.children.length > 0) {
                selectedImage.src = scrollableImages.children[currentImageIndex].src;
            } else {
                selectedImage.src = ""; 
            }
        }
    });

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
