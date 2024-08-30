document.addEventListener('DOMContentLoaded', function() {
    const matrixLoading = document.getElementById('matrix-loading');
    const downloadButton = document.getElementById('downloadButton');
    const hackingMessage = document.getElementById('hackingMessage');
    const timeToHack = 12000;

    function createMatrixEffect() {
        matrixLoading.innerHTML = '';
        const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
        const matrixContent = document.createElement('div');
        matrixContent.className = 'matrix-content';

        const containerWidth = matrixLoading.offsetWidth;
        const charWidth = 14; // Approximate width of a character in pixels
        const charsPerRow = Math.floor(containerWidth / charWidth);
        const rows = Math.ceil(window.innerHeight / 20); // Adjust based on font size

        for (let i = 0; i < rows; i++) {
            const row = document.createElement('div');
            row.className = 'matrix-row';
            for (let j = 0; j < charsPerRow; j++) {
                const span = document.createElement('span');
                span.textContent = chars[Math.floor(Math.random() * chars.length)];
                row.appendChild(span);
            }
            matrixContent.appendChild(row);
        }

        matrixLoading.appendChild(matrixContent);
    }

    function updateMatrix() {
        const spans = matrixLoading.querySelectorAll('span');
        spans.forEach(span => {
            if (Math.random() < 0.1) {
                span.textContent = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'[Math.floor(Math.random() * 36)];
            }
        });
    }

    function typewriterEffect(element, text, speed, callback) {
        let i = 0;
        element.style.display = 'inline-block';
        element.textContent = '';
        function type() {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                setTimeout(type, speed);
            } else if (callback) {
                callback();
            }
        }
        type();
    }

    createMatrixEffect();
    const matrixInterval = setInterval(updateMatrix, 50);

    setTimeout(() => {
        clearInterval(matrixInterval);
        matrixLoading.style.display = 'none';
        hackingMessage.style.display = 'none';
        
        // Start typewriter effect for the button
        typewriterEffect(downloadButton, 'Download Track', 50, () => {
            downloadButton.classList.add('button-glow');
        });
    }, timeToHack);

    // Recreate matrix effect on window resize
    window.addEventListener('resize', createMatrixEffect);

    downloadButton.addEventListener('click', function() {
        fetch('/download', {
            method: 'POST'
        })
        .then(response => response.blob())
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = 'spotify_track.mp3';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
        })
        .catch(error => console.error('Error:', error));
    });
});