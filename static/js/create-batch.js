

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

    $('#deleteBtn').on('click', function () {
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
                    if (data.success) {
                        removeImageFromList(currentImage);
                    }
                },
                error: function (xhr, status, error) {
                    console.error("Delete Error:", status, error);
                }
            });
        }
    });


    function displayImages(images) {
        images.forEach(function (imageUrl, index) {
            // Check if the image already exists to avoid duplication
            if (!$("img[src='" + imageUrl + "']").length) {
                const imgElement = `<img src="${imageUrl}" class="scrollable-image" alt="image ${index + 1}" onclick="displayImage(this)">`;
                $('#scrollableImages').append(imgElement);
            }
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