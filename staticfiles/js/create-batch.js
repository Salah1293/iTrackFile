// $(document).ready(function () {
//     $(".scrollable-image").on("click", function () {
//       // Update the source of the selectedImage
//       $("#selectedImage").attr("src", $(this).attr("src"));

//       resetTransform();
//     });

//     let zoomLevel = 1;
//     let rotationAngle = 0;
//     let isDragging = false;
//     let positionX = 0;
//     let positionY = 0;
//     let startX = 0;
//     let startY = 0;

//     $("#selectedImage")
//       .on("wheel", function (event) {
//         event.preventDefault();
//         const delta = event.originalEvent.deltaY;

//         if (delta < 0 && zoomLevel < 2) {
//           zoomLevel += 0.1;
//         }

//         if (delta > 0 && zoomLevel > 0.5) {
//           zoomLevel -= 0.1;
//         }

//         updateTransform();
//       })
//       .on("mousedown", function (event) {
//         isDragging = true;
//         startX = event.clientX - positionX;
//         startY = event.clientY - positionY;
//       })
//       .on("mouseup", function () {
//         isDragging = false;
//       })
//       .on("mousemove", function (event) {
//         if (isDragging) {
//           positionX = event.clientX - startX;
//           positionY = event.clientY - startY;
//           updateTransform();
//         }
//       });

//     $("#selectedImage").on("click", function (event) {
//       const rect = this.getBoundingClientRect();
//       const mouseX = event.clientX - rect.left;
//       const mouseY = event.clientY - rect.top;

//       positionX -= mouseX * (zoomLevel - 1);
//       positionY -= mouseY * (zoomLevel - 1);

//       updateTransform();
//     });

//     $("#zoomInBtn").on("click", function () {
//       if (zoomLevel < 2) {
//         zoomLevel += 0.1;
//         updateTransform();
//       }
//     });

//     $("#zoomOutBtn").on("click", function () {
//       if (zoomLevel > 0.5) {
//         zoomLevel -= 0.1;
//         updateTransform();
//       }
//     });

//     $("#rotateBtn").on("click", function () {
//       rotationAngle += 90;
//       updateTransform();
//     });

//     $("#resetBtn").on("click", function () {
//       resetTransform();
//     });

//     function updateTransform() {
//       $("#selectedImage").css(
//         "transform",
//         `scale(${zoomLevel}) rotate(${rotationAngle}deg) translate(${positionX}px, ${positionY}px)`
//       );
//     }

//     function resetTransform() {
//       zoomLevel = 1;
//       rotationAngle = 0;
//       positionX = 0;
//       positionY = 0;
//       updateTransform();
//     }
//   });










$(document).ready(function () {
    // Open file selector when Import button is clicked
    $('#importButton').on('click', function () {
        $('#imageInput').click();
    });

    // Trigger AJAX form submission when files are selected
    $('#imageInput').on('change', function () {
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


    // Trigger scan and upload scanned images
    $('#scanButton').on('click', function () {
        $.ajax({
            url: scanUrl,  // URL for the scan endpoint
            type: 'POST',
            data: { source: 'scan' },
            success: function (data) {
                console.log("Scan Success:", data);
                displayImages(data.uploaded_images);
                appendHiddenFields(data.uploaded_images);
            },
            error: function (xhr, status, error) {
                console.error("Scan Error:", status, error);
            }
        });
    });

    // Display images and set the first image as selectedImage
    function displayImages(images) {
        console.log("Displaying Images:", images);
        images.forEach(function (imageUrl, index) {
            const imgElement = `<img src="${imageUrl}" class="scrollable-image" alt="image ${index + 1}">`;
            $('#scrollableImages').append(imgElement);
        });

        // Set the first image as selectedImage if not already set
        if ($('#selectedImage').attr('src') === '') {
            $('#selectedImage').attr('src', images[0]);
        }

        // Add click event listener to each scrollable image
        $(".scrollable-image").on("click", function () {
            $("#selectedImage").attr("src", $(this).attr("src"));
            resetTransform();
        });
    }

    function appendHiddenFields(images) {
        images.forEach(function (imageUrl) {
            $('#uploadForm').append(`<input type="hidden" name="uploaded_images" value="${imageUrl}">`);
        });
    }

    // Additional code for zoom, rotate, and reset functionalities...
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
