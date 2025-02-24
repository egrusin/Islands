function generateRandom() {
    const rows = document.getElementById('rows').value;
    const cols = document.getElementById('cols').value;

    fetch('/process', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rows: rows, cols: cols })
    })
    .then(response => response.json())
    .then(data => {
        renderGrid(data.grid, data.island_map);
        document.getElementById('island-count').textContent = data.island_count;
    });
}

function renderGrid(grid, island_map) {
    const container = document.getElementById('grid-container');
    container.innerHTML = '';
    container.style.gridTemplateColumns = `repeat(${grid[0].length}, 30px)`;

    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            if (grid[i][j] === 0) {
                cell.classList.add('water');
            } else {
                cell.classList.add('land');
                if (island_map[i][j] > 0) {
                    cell.classList.add(`island-${island_map[i][j]}`);
                }
            }
            container.appendChild(cell);
        }
    }
}

// Инициализация при загрузке страницы
generateRandom();