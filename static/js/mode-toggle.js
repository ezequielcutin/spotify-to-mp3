// Check for saved theme preference or default to light mode
let isDarkMode = localStorage.getItem('isDarkMode') === 'true' || false;

// Apply the saved theme immediately
document.addEventListener('DOMContentLoaded', applyTheme);

function applyTheme() {
    if (isDarkMode) {
        toggleMode(false);
    }
}

const rainContainer = document.getElementById('rain');
const modeIcon = document.getElementById('mode-icon');
const dayLabel = document.getElementById('day-label');
const nightLabel = document.getElementById('night-label');
const title = document.querySelector('h1');
let rainInterval;

let dropCount = 0;

function createRain() {
    dropCount++;
    if (dropCount % 5 === 0) {
        for (let i = 0; i < 2; i++) {
            createSingleDrop();
        }
    } else {
        createSingleDrop();
    }
}

function createSingleDrop() {
    const drop = document.createElement('div');
    drop.className = 'drop';
    drop.textContent = Math.random() < 0.5 ? '1' : '0';
    drop.style.left = Math.random() * 100 + 'vw';
    rainContainer.appendChild(drop);
    setTimeout(() => drop.remove(), 15000);
}

function toggleMode(savePreference = true) {
    isDarkMode = savePreference ? !isDarkMode : isDarkMode;
    document.body.style.backgroundColor = isDarkMode ? '#121212' : '#ffffff';
    document.body.style.color = isDarkMode ? '#1db954' : '#000000';
    rainContainer.style.display = isDarkMode ? 'block' : 'none';
    toggle.classList.toggle('active', isDarkMode);
    modeIcon.className = isDarkMode ? 'fas fa-moon' : 'fas fa-sun';

    dayLabel.style.color = isDarkMode ? '#1db954' : '#000000';
    nightLabel.style.color = isDarkMode ? '#1db954' : '#000000';
    title.style.color = isDarkMode ? '#1db954' : '#000000';

    if (isDarkMode) {
        if (!rainInterval) rainInterval = setInterval(createRain, 5000);
    } else {
        clearInterval(rainInterval);
        rainInterval = null;
    }

    if (savePreference) {
        localStorage.setItem('isDarkMode', isDarkMode);
    }
}

toggle.addEventListener('click', () => toggleMode(true));