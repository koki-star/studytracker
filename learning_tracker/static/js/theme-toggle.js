// Theme toggle with localStorage persistence and system preference detection

document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('themeToggle');
    const htmlElement = document.documentElement;

    // Check localStorage first, then fall back to system preference
    const getPreferredTheme = () => {
        const storedTheme = localStorage.getItem('theme');
        if (storedTheme) {
            return storedTheme;
        }
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    };

    // Apply theme and save to localStorage
    const setTheme = (theme) => {
        htmlElement.setAttribute('data-bs-theme', theme);
        if (theme === 'dark') {
            htmlElement.classList.add('dark-mode');
        } else {
            htmlElement.classList.remove('dark-mode');
        }
        localStorage.setItem('theme', theme);

        // Notify Chart.js and other components about theme change
        window.dispatchEvent(new CustomEvent('themeChanged', { detail: { theme } }));
    };

    // Initialize theme on page load
    const currentTheme = getPreferredTheme();
    setTheme(currentTheme);

    // Toggle theme on button click
    toggleButton.addEventListener('click', () => {
        const currentTheme = htmlElement.getAttribute('data-bs-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(newTheme);
    });
});
