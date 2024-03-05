document.addEventListener("DOMContentLoaded", function() {
  const form = document.getElementById("property-search");

  form.addEventListener("submit", function(event) {
    event.preventDefault();
    const data = {
      'sqft': document.getElementById("sqft").value,
      'bedrooms': document.getElementById("bedrooms").value,
      'bathrooms': document.getElementById("bathrooms").value,
      'location': document.getElementById("location").value,
      'parking': document.getElementById("parking").checked ? 'Yes' : 'No',
      'building-type': document.getElementById("building-type").value,
      'utility': document.getElementById("utility").checked ? 'Yes' : 'No',
      'street-type': document.getElementById("street-type").value
    };

    fetch("/predict", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('predictionAmount').textContent = 'Predicted Price: ' + data.prediction;
    })
    .catch(error => {
      console.error('Error:', error);
    });
  });
});