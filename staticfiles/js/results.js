function redirectToSingleImage(section, docId, allIds) {
  var idsArray = allIds.split(',');
  var idsParam = encodeURIComponent(idsArray.join(','));
  var url = `/single-image/${section}/${docId}/?ids=${idsParam}`;
  
  console.log('Redirecting to:', url);
  
  window.location.href = url;
}