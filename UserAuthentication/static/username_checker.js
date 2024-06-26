const usernameInput = document.getElementById('id_username');
const debouncedCheckUsername = _.debounce(checkUsername, 500);
usernameInput.addEventListener('input', debouncedCheckUsername);

function checkUsername() {
    const username = document.getElementById('id_username').value;

    fetch('/auth/checkUsername', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ username: username })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data.username_exists);
            if (data.username_exists == "true") {
                alert('Username already exists. Please choose another username.');
                usernameInput.value = '';
            } else {
                // username does not exist, do something else
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + '=') {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
