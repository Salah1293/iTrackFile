function redirectToSingleImage(section, docId, allIds) {
  var idsArray = allIds.split(',');
  // Encode all IDs properly for URL
  var idsParam = encodeURIComponent(idsArray.join(','));
  // Construct the URL with section, docId, and idsParam
  var url = `/single-image/${section}/${docId}/?ids=${idsParam}`;
  
  // Log the URL to the console for debugging
  console.log('Redirecting to:', url);
  
  // Redirect to the constructed URL
  window.location.href = url;
}