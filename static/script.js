document.getElementById('storeButton').addEventListener('click', function() {
    const textInput = document.getElementById('textInput').value;
    const storedTextElement = document.getElementById('storedText');

    if (textInput.trim() !== "") {
        // Send text to Flask server for correction
        fetch('/correct', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `text=${encodeURIComponent(textInput)}`
        })
        .then(response => response.json())
        .then(data => {
            storedTextElement.textContent = `Corrected Text: ${data.corrected_text}`;
            document.getElementById('textInput').value = ""; // Clear the input after processing
        });
    } else {
        storedTextElement.textContent = "Please enter some text.";
    }
});
