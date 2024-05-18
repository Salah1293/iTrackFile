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



var results = JSON.parse('{{ all_results|escapejs }}');

function redirectToSingleImage(docId, allIds) {  
    var idsArray = allIds.split(',');
    // it's better to use encodeURIComponent() to ensure that special characters in the IDs are properly encoded.
    let idsParam = encodeURIComponent(idsArray.join(','));
    window.location.href = `/single-image/${docId}/?ids=${idsParam}`;
  }


  function loadTableResults(table_name) {
    const selectedTable = document.getElementById('table-selector').value;
    const tableResultsContainer = document.getElementById('table-results-container');

    // Clear any existing content
    tableResultsContainer.innerHTML = '';

    if (table_name) {
      // Determine the template name based on the selected table (modify as needed)
      let templateName = `${selectedTable.toLowerCase().replace(" ", "-")}-results.html`;

      console.log("Template name:", templateName);
      // Get the corresponding table data from the all_results dictionary
      const tableData = results[table_name];

      if (tableData) {
        // Include the template with context
        console.log("Template name:", templateName);
        tableResultsContainer.innerHTML = `{% include '${templateName}' table_data=tableData %}`;
        // console.log('template name:', tableResultsContainer)
      } else {
        // Display a message if no data is found for the selected table
        console.log("Selected table name is empty.");
        tableResultsContainer.innerHTML = `<p>No results found for '${selectedTable}'.</p>`;
      }
    }
  }
