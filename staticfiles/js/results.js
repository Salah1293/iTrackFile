// document.querySelectorAll(".deletebtn").forEach(btn => {
//     btn.addEventListener('click', function () {

//         const docId = this.dataset.docid;
        
//         document.getElementById('delete-id-input').value = docId;
        
//         // document.querySelector('#delete-popup').classList.add('active');
//     });
// });



// document.querySelector(".deletebtn").addEventListener('click', function () {
//     document.querySelector('.delete-popup').classList.add('active');
// });

// document.querySelector(".delete-popup .close-btn").addEventListener('click', function () {
//     document.querySelector('.delete-popup').classList.remove('active');
// });

// document.querySelector(".delete-popup .cls").addEventListener('click', function () {
//     document.querySelector('.delete-popup').classList.remove('active');
// });



function redirectToSingleImage(docId, allIds) {  
    var idsArray = allIds.split(',');
    // it's better to use encodeURIComponent() to ensure that special characters in the IDs are properly encoded.
    let idsParam = encodeURIComponent(idsArray.join(','));
    window.location.href = `/single-image/${docId}/?ids=${idsParam}`;
  }


//   document.addEventListener('DOMContentLoaded', function() {
//     var buttons = document.querySelectorAll('.btn');
//     var resultContainer = document.getElementById('result-container');

//     buttons.forEach(function(button) {
//         button.addEventListener('click', function() {
//             var tableName = button.getAttribute('data-table-name');

//             fetch(`{% url 'general_search' %}?text={{ query }}&table_name=${tableName}`, {
//                 headers: {
//                     'X-Requested-With': 'XMLHttpRequest'
//                 }
//             })
//             .then(response => response.json())
//             .then(data => {
//                 resultContainer.innerHTML = data.html;
//             })
//             .catch(error => console.error('Error:', error));
//         });
//     });
// });