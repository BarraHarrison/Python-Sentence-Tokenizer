document.getElementById('tokenizeButton').addEventListener('click', function () {
    const paragraph = document.getElementById('paragraph').ariaValueMax;

    fetch('/tokenize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'paragraph=' + encodeURIComponent(paragraph)
    })

        .then(response => response.text())
        .then(data => {
            document.getElementById('output').textContent = data;
        });
});