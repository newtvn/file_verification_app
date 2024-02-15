document.getElementById('upload-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData();
    const fileInput = document.getElementById('csvFile');
    formData.append('file', fileInput.files[0]);

    fetch('/validate-csv', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        displayResults(data);
    })
    .catch(error => console.error('Error:', error));
});

function displayResults(data) {
    // Assuming 'data' contains arrays of valid and invalid records
    // Populate '#valid-records' and '#invalid-records' divs with this data
    const validRecordsDiv = document.getElementById('valid-records');
    const invalidRecordsDiv = document.getElementById('invalid-records');

    // Example: Inserting text content; you might want to create tables or lists based on 'data'
    validRecordsDiv.textContent = JSON.stringify(data.valid, null, 2);
    invalidRecordsDiv.textContent = JSON.stringify(data.invalid, null, 2);

    document.getElementById('results-section').classList.remove('hidden');
}
