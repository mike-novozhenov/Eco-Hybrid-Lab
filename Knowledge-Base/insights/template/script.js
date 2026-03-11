function toggleTheme() {
    const body = document.body;
    const currentTheme = body.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
}

function copyCode(id) {
    const pre = document.getElementById(id);
    const text = pre.innerText.replace('COPY', '').trim();
    navigator.clipboard.writeText(text);

    const btn = pre.querySelector('.copy-btn');
    const originalText = btn.innerText;
    btn.innerText = 'COPIED!';
    setTimeout(() => btn.innerText = originalText, 2000);
}

document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme') || 'dark';
    document.body.setAttribute('data-theme', savedTheme);
});

document.addEventListener('click', function(e) {
    if (e.target && e.target.classList.contains('cmd')) {
        const text = e.target.innerText;

        // Копируем в буфер обмена
        navigator.clipboard.writeText(text).then(() => {
            // Добавляем класс для анимации "Copied!"
            e.target.classList.add('copied');
            setTimeout(() => e.target.classList.remove('copied'), 2000);

            console.log('Copied to clipboard:', text);
        });
    }
});