// document.addEventListener("DOMContentLoaded", function() {
//     const form = document.getElementById("property-search");
  
//     form.addEventListener("submit", function(event) {
//       event.preventDefault(); // Prevent form submission
  
//       // Get form values
//       const sqft = document.getElementById("sqft").value;
//       const bedrooms = document.getElementById("bedrooms").value;
//       const bathrooms = document.getElementById("bathrooms").value;
//       const location = document.getElementById("location").value;
//       const area = document.getElementById("area").value;
//       const parking = document.getElementById("parking").checked;
//       const buildingType = document.getElementById("building-type").value;
//       const utility = document.getElementById("utility").value;
//       const streetType = document.getElementById("street-type").value;
  
//       // Perform search or display results
//       searchProperties(sqft, bedrooms, bathrooms, location, area, parking, buildingType, utility, streetType);
//     });
  
//     function searchProperties(sqft, bedrooms, bathrooms, location, area, parking, buildingType, utility, streetType) {
//       // Example: Perform AJAX request to fetch properties based on the search criteria
//       // Replace this with your actual search logic
//       console.log("Searching properties...");
//       console.log("Square Feet:", sqft);
//       console.log("Bedrooms:", bedrooms);
//       console.log("Bathrooms:", bathrooms);
//       console.log("Location:", location);
//       console.log("Area:", area);
//       console.log("Parking:", parking ? "Yes" : "No");
//       console.log("Building Type:", buildingType);
//       console.log("Utility:", utility);
//       console.log("Street Type:", streetType);
//     }
//   });

// function searchProperties(sqft, bedrooms, bathrooms, location, area, parking, buildingType, utility, streetType) {
//   // Create an object with the form values
//   const data = {
//       'sqft': sqft,
//       'bedrooms': bedrooms,
//       'bathrooms': bathrooms,
//       'location': location,
//       'area': area,
//       'parking': parking ? 'Yes' : 'No',
//       'building-type': buildingType,
//       'utility': utility,
//       'street-type': streetType
//   };

//   // Send a POST request to the Flask server
//   fetch('/predict', {
//       method: 'POST',
//       headers: {
//           'Content-Type': 'application/json'
//       },
//       body: JSON.stringify(data)  // Convert the data into a JSON string
//   })
//   .then(response => response.json())
//   .then(data => {
//       // Display the prediction result
//       console.log('Predicted Price:', data.prediction);
//   })
//   .catch((error) => {
//       console.error('Error:', error);
//   });
// }

document.addEventListener("DOMContentLoaded", function() {
  const form = document.getElementById("property-search");

  form.addEventListener("submit", function(event) {
    event.preventDefault();

    // Create an object with the form values
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

    // Send a POST request to the Flask server
    fetch("/predict", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
      // Display the prediction result
      document.getElementById('predictionAmount').textContent = 'Predicted Price: ' + data.prediction;
    });
  });
});
