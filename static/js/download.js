document.addEventListener('DOMContentLoaded', function() {
    const matrixLoading = document.getElementById('matrix-loading');
    const downloadButton = document.getElementById('downloadButton');

    function createMatrixEffect() {
        matrixLoading.innerHTML = '';
        const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
        const width = 40;
        const height = 20;

        const matrixContent = document.createElement('div');
        matrixContent.className = 'matrix-content';

        for (let i = 0; i < height; i++) {
            const row = document.createElement('div');
            for (let j = 0; j < width; j++) {
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

    createMatrixEffect();
    const matrixInterval = setInterval(updateMatrix, 100);

    setTimeout(() => {
        clearInterval(matrixInterval);
        matrixLoading.style.display = 'none';
        downloadButton.style.display = 'inline-block';
    }, 5000);

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