document.querySelector('form').addEventListener('submit', function (e) {
    e.preventDefault();
    const trackUrl = document.querySelector('input[name="track_url"]').value;

    fetch('/initiate_auth', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'track_url=' + encodeURIComponent(trackUrl)
    })
        .then(response => response.json())
        .then(data => {
            if (data.auth_url) {
                // Instead of opening a new tab, redirect in the same tab
                window.location.href = data.auth_url;
            }
        })
        .catch(error => console.error('Error:', error));
});