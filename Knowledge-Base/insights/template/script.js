function toggleTheme() {
    const html = document.documentElement;
    if (html.classList.contains('dark-theme')) {
        html.classList.replace('dark-theme', 'light-theme')
        localStorage.setItem('theme', 'light-theme')
    } else {
        html.classList.replace('light-theme', 'dark-theme')
        localStorage.setItem('theme', 'dark-theme')
    }
}

function copyCode(id) {
    const pre = document.getElementById(id);
    const text = pre.innerText.replace('COPY', '').trim()
    navigator.clipboard.writeText(text)

    const btn = pre.querySelector('.copy-btn')
    const originalText = btn.innerText
    btn.innerText = 'COPIED!'
    setTimeout(() => btn.innerText = originalText, 2000)
}

document.addEventListener('click', function(e) {
    if (e.target && e.target.classList.contains('cmd')) {
        const text = e.target.innerText

        navigator.clipboard.writeText(text).then(() => {
            e.target.classList.add('copied')
            setTimeout(() => e.target.classList.remove('copied'), 2000)

            console.log('Copied to clipboard:', text)
        })
    }
})