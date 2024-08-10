

// $(document).ready(function () {
//     $('#importButton').on('click', function () {
//         $('#imageInput').click();
//     });

//     function submitScanForm() {
//         var form = document.getElementById('uploadForm');
//         form.action = "{% url 'upload_scanned_images' %}";
//         form.submit();
//     }

//     $('#imageInput').on('change', function () {
//         let formData = new FormData($('#uploadForm')[0]);
//         $.ajax({
//             url: uploadUrl,
//             type: 'POST',
//             data: formData,
//             processData: false,
//             contentType: false,
//             success: function (data) {
//                 console.log("AJAX Success:", data);
//                 displayImages(data.uploaded_images);
//                 appendHiddenFields(data.uploaded_images);
//             },
//             error: function (xhr, status, error) {
//                 console.error("AJAX Error:", status, error);
//             }
//         });
//     });


//     $('#scanButton').on('click', function () {
//         $.ajax({
//             url: scanUrl,  
//             type: 'POST',
//             data: { source: 'scan' },
//             success: function (data) {
//                 console.log("Scan Success:", data);
//                 displayImages(data.uploaded_images);
//                 appendHiddenFields(data.uploaded_images);
//             },
//             error: function (xhr, status, error) {
//                 console.error("Scan Error:", status, error);
//             }
//         });
//     });

//     function displayImages(images) {
//         console.log("Displaying Images:", images);
//         images.forEach(function (imageUrl, index) {
//             const imgElement = `<img src="${imageUrl}" class="scrollable-image" alt="image ${index + 1}">`;
//             $('#scrollableImages').append(imgElement);
//         });

//         if ($('#selectedImage').attr('src') === '') {
//             $('#selectedImage').attr('src', images[0]);
//         }

//         $(".scrollable-image").on("click", function () {
//             $("#selectedImage").attr("src", $(this).attr("src"));
//             resetTransform();
//         });
//     }

//     function appendHiddenFields(images) {
//         images.forEach(function (imageUrl) {
//             $('#uploadForm').append(`<input type="hidden" name="uploaded_images" value="${imageUrl}">`);
//         });
//     }

//     let zoomLevel = 1;
//     let rotationAngle = 0;
//     let positionX = 0;
//     let positionY = 0;

//     $('#zoomInBtn').on('click', function () {
//         zoomLevel += 0.1;
//         updateTransform();
//     });

//     $('#zoomOutBtn').on('click', function () {
//         if (zoomLevel > 0.1) zoomLevel -= 0.1;
//         updateTransform();
//     });

//     $('#rotateBtn').on('click', function () {
//         rotationAngle = (rotationAngle + 90) % 360;
//         updateTransform();
//     });

//     $('#resetBtn').on('click', function () {
//         resetTransform();
//     });

//     function updateTransform() {
//         $("#selectedImage").css(
//             "transform",
//             `scale(${zoomLevel}) rotate(${rotationAngle}deg) translate(${positionX}px, ${positionY}px)`
//         );
//     }

//     function resetTransform() {
//         zoomLevel = 1;
//         rotationAngle = 0;
//         positionX = 0;
//         positionY = 0;
//         updateTransform();
//     }
// });









// $(document).ready(function () {
//     $('#importButton').on('click', function () {
//         $('#imageInput').click();
//     });

//     function submitScanForm() {
//         var form = document.getElementById('uploadForm');
//         form.action = scanUrl;
//         form.submit();
//     }

//     $('#imageInput').on('change', function () {
//         let formData = new FormData($('#uploadForm')[0]);
//         $.ajax({
//             url: uploadUrl,
//             type: 'POST',
//             data: formData,
//             processData: false,
//             contentType: false,
//             success: function (data) {
//                 console.log("AJAX Success:", data);
//                 displayImages(data.uploaded_images);
//                 appendHiddenFields(data.uploaded_images);
//             },
//             error: function (xhr, status, error) {
//                 console.error("AJAX Error:", status, error);
//             }
//         });
//     });

//     $('#scanButton').on('click', function () {
//         $.ajax({
//             url: scanUrl,
//             type: 'POST',
//             data: { source: 'scan' },
//             success: function (data) {
//                 console.log("Scan Success:", data);
//                 displayImages(data.uploaded_images);
//                 appendHiddenFields(data.uploaded_images);
//             },
//             error: function (xhr, status, error) {
//                 console.error("Scan Error:", status, error);
//             }
//         });
//     });

//     $('#deleteBtn').on('click', function () {
//         console.log("Delete button clicked");
//         let currentImage = $('#selectedImage').attr('src');
//         console.log("Current Image URL:", currentImage); 
//         if (currentImage) {
//             $.ajax({
//                 url: deleteUrl,
//                 type: 'POST',
//                 data: {
//                     deleteUrl: currentImage,
//                     csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
//                 },
//                 success: function (data) {
//                     console.log("AJAX Success:", data);
//                     if (data.success) {
//                         removeImageFromList(currentImage);
//                     } else {
//                         console.error("Failed to delete image:", currentImage);
//                     }
//                 },
//                 error: function (xhr, status, error) {
//                     console.error("Error deleting image:", status, error);
//                 }
//             });
//         }
//     });
    
    

//     function displayImages(images) {
//         console.log("Displaying Images:", images);
//         $('#scrollableImages').empty(); // Clear the container before appending new images
    
//         // Check if images is an array and has at least one image
//         if (Array.isArray(images) && images.length > 0) {
//             images.forEach(function (imageUrl, index) {
//                 const imgElement = `<img src="${imageUrl}" class="scrollable-image" alt="image ${index + 1}">`;
//                 $('#scrollableImages').append(imgElement);
//             });
    
//             // Set the first image as selected if none is selected
//             if ($('#selectedImage').attr('src') === '' && images.length > 0) {
//                 $('#selectedImage').attr('src', images[0]);
//             }
    
//             // Add click event listener to each image
//             $(".scrollable-image").on("click", function () {
//                 $("#selectedImage").attr("src", $(this).attr("src"));
//                 resetTransform();
//             });
//         } else {
//             // If no images are left, clear the selected image
//             $('#selectedImage').attr('src', '');
//         }
//     }
    


//     function appendHiddenFields(images) {
//         images.forEach(function (imageUrl) {
//             $('#uploadForm').append(`<input type="hidden" name="uploaded_images" value="${imageUrl}">`);
//         });
//     }

//     function removeImageFromList(imageUrl) {
//         console.log("Removing Image:", imageUrl);
        
//         // Remove the image from the DOM
//         $('img[src="' + imageUrl + '"]').remove();
//         $('input[value="' + imageUrl + '"]').remove();
    
//         // Get the updated list of images
//         const images = $('#scrollableImages img').map(function() {
//             return $(this).attr('src');
//         }).get();
    
//         // Display the next image or the first one if no images are left
//         displayImages(images);
//     }
    
    


//     function displayNextImage() {
//         let nextImage = $('#scrollableImages img:first').attr('src');
//         if (nextImage) {
//             $('#selectedImage').attr('src', nextImage);
//         } else {
//             // If no images are left, clear the selected image
//             $('#selectedImage').attr('src', '');
//         }
//     }

//     let zoomLevel = 1;
//     let rotationAngle = 0;
//     let positionX = 0;
//     let positionY = 0;

//     $('#zoomInBtn').on('click', function () {
//         zoomLevel += 0.1;
//         updateTransform();
//     });

//     $('#zoomOutBtn').on('click', function () {
//         if (zoomLevel > 0.1) zoomLevel -= 0.1;
//         updateTransform();
//     });

//     $('#rotateBtn').on('click', function () {
//         rotationAngle = (rotationAngle + 90) % 360;
//         updateTransform();
//     });

//     $('#resetBtn').on('click', function () {
//         resetTransform();
//     });

//     function updateTransform() {
//         $("#selectedImage").css(
//             "transform",
//             `scale(${zoomLevel}) rotate(${rotationAngle}deg) translate(${positionX}px, ${positionY}px)`
//         );
//     }

//     function resetTransform() {
//         zoomLevel = 1;
//         rotationAngle = 0;
//         positionX = 0;
//         positionY = 0;
//         updateTransform();
//     }
// });


// $(document).on('click', '#deleteBtn', function () {
//     console.log("Delete button clicked");
// });






$(document).ready(function () {
    $('#importButton').on('click', function () {
        $('#imageInput').click();
    });

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

    $('#deleteBtn').on('click', function () {
        console.log("Delete button clicked");
        let currentImage = $('#selectedImage').attr('src');
        if (currentImage) {
            $.ajax({
                url: deleteUrl,
                type: 'POST',
                data: {
                    deleteUrl: currentImage,
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
                },
                success: function (data) {
                    console.log("AJAX Success:", data);
                    if (data.success) {
                        removeImageFromList(currentImage);
                    } else {
                        console.error("Failed to delete image:", currentImage);
                    }
                },
                error: function (xhr, status, error) {
                    console.error("Error deleting image:", status, error);
                }
            });
        }
    });

    function displayImages(images) {
        console.log("Displaying Images:", images);
        // $('#scrollableImages').empty(); 
    
        images.forEach(function (imageUrl, index) {
            const imgElement = `<img src="${imageUrl}" class="scrollable-image" alt="image ${index + 1}">`;
            $('#scrollableImages').append(imgElement);
        });
    
        // Display the first image if none is selected
        if ($('#selectedImage').attr('src') === '' && images.length > 0) {
            $('#selectedImage').attr('src', images[0]);
        }
    
        // Add click event listener to each image
        $(".scrollable-image").on("click", function () {
            $("#selectedImage").attr("src", $(this).attr("src"));
            resetTransform();
        });
    }
    

    function appendHiddenFields(images) {
        images.forEach(function (imageUrl) {
            $('#uploadForm').append(`<input type="hidden" name="uploaded_images" value="${imageUrl}">`);
            console.log('images appended', images)
        });
    }

    function removeImageFromList(imageUrl) {
        console.log("Removing Image:", imageUrl);
        $('img[src="' + imageUrl + '"]').remove();
    
        // Log the number of remaining images
        console.log("Remaining images:", $('#scrollableImages img').length);
    
        // Ensure `displayNextImage` is called to handle image display
        displayNextImage();
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
