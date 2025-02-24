import random


def count_islands(grid) -> tuple[int, list[list[int]]]:
    """Функция подсчета островов.
    param: grid - list[list[int]] - двумерное поле, вода и острова
    return: int, list[list[int]]] - количество островов и их раскраска"""
    rows, cols = len(grid), len(grid[0])
    island_count = 0
    island_map = [[0] * cols for _ in range(rows)]

    def dfs(row, col, island_id):
        if (row < 0 or row >= rows or 
            col < 0 or col >= cols or 
            grid[row][col] != 1 or 
            island_map[row][col] != 0):
            return
        
        island_map[row][col] = island_id

        dfs(row - 1, col, island_id)
        dfs(row + 1, col, island_id)
        dfs(row, col - 1, island_id)
        dfs(row, col + 1, island_id)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and island_map[i][j] == 0:
                island_count += 1
                dfs(i, j, island_count)
    
    return island_count, island_map


def generate_random_grid(rows, cols):
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]


if __name__ == '__main__':
    sea = generate_random_grid(5, 5)
    print('Исходное поле:')
    print(*sea, sep='\n')
    print()

    i_count, map = count_islands(sea)
    print('Количество островов:', i_count)
    print('Окрашенное поле:')
    print(*map, sep='\n')