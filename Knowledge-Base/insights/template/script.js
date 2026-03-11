function toggleTheme() {
    const html = document.documentElement;
    const currentTheme = html.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
}

function copyCode(id) {
    const pre = document.getElementById(id);
    const btn = pre.querySelector('.copy-btn');

    // Get text but exclude the button text itself
    const text = pre.innerText.replace(btn.innerText, '').trim();

    navigator.clipboard.writeText(text).then(() => {
        const originalText = btn.innerText;
        btn.innerText = 'COPIED!';
        setTimeout(() => btn.innerText = originalText, 2000);
    });
}

// Global click listener for inline commands (.cmd)
document.addEventListener('click', function(e) {
    if (e.target && e.target.classList.contains('cmd')) {
        const text = e.target.innerText;

        navigator.clipboard.writeText(text).then(() => {
            e.target.classList.add('copied');
            setTimeout(() => e.target.classList.remove('copied'), 2000);
            console.log('Command copied:', text);
        });
    }
});