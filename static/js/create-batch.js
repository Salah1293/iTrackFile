

$(document).ready(function () {
    $('#importButton').on('click', function () {
        $('#imageInput').click();
    });

    function submitScanForm() {
        var form = document.getElementById('uploadForm');
        form.action = "{% url 'upload_scanned_images' %}";
        form.submit();
    }

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
        $.ajax({
            url: scanUrl,  
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

    function displayImages(images) {
        console.log("Displaying Images:", images);
        images.forEach(function (imageUrl, index) {
            const imgElement = `<img src="${imageUrl}" class="scrollable-image" alt="image ${index + 1}">`;
            $('#scrollableImages').append(imgElement);
        });

        if ($('#selectedImage').attr('src') === '') {
            $('#selectedImage').attr('src', images[0]);
        }

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
