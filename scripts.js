// Copy to Clipboard Function
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        Swal.fire('Copied!', 'Text copied to clipboard.', 'success');
    });
}

// SweetAlert Popup for Social Icons
function showMessage(event, platform) {
    event.preventDefault();
    Swal.fire({
        title: platform,
        text: 'You clicked on ' + platform,
        icon: 'info',
        confirmButtonText: 'Close'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = event.target.href;
        }
    });
}

// Dark/Light Mode Toggle
function toggleDarkMode() {
    const body = document.body;
    body.classList.toggle('light-mode');
    localStorage.setItem('theme', body.classList.contains('light-mode') ? 'light' : 'dark');
}

// Check for Saved Theme
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'light') {
        document.body.classList.add('light-mode');
    }
});
