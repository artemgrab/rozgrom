const eyeIcons = document.querySelectorAll('.eye-icon');

eyeIcons.forEach(icon => {
    icon.addEventListener('click', () => {
        const input = icon.previousElementSibling;

        if (input.type === 'password') {
            input.type = 'text';
            icon.style.fill = '#f27a24';
        } else {
            input.type = 'password';
            icon.style.fill = '';
        }
    });
});