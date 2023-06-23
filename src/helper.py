import pygame

def create_grid(rows, columns):
    grid = []
    for row in range(rows):
        grid.append([])
        for column in range(columns):
            grid[row].append(0)
    return grid

def print_grid(screen, grid ,screen_size,cell_size):
    for y in range(0,screen_size,cell_size):
        for x in range(0,screen_size,cell_size):
            points = [(x,y),(x+cell_size,y),(x,y+cell_size),(x+cell_size,y+cell_size)]

            color = pygame.Color(0,0,0)

            if grid[y//cell_size][x//cell_size] == 1:
                color = pygame.Color(100,225,100)

            pygame.draw.rect(screen, color, pygame.Rect(x, y, cell_size, cell_size))
            pygame.draw.line(screen, pygame.Color(100,100,100), (x,0), (x,screen_size))
        pygame.draw.line(screen, pygame.Color(100,100,100), (0,y), (screen_size,y))

def iteracion(grid):
    new_grid = create_grid(len(grid), len(grid))
    for y in range(len(grid)):
        for x in range(len(grid)):
            n_neighbors = count_neighbors(grid, x, y)
            #Si una célula está muerta y tiene tres vecinas vivas, nace
            if grid[y][x] == 0 and n_neighbors == 3:
                new_grid[y][x] = 1
            #Si una célula está viva y tiene menos de dos vecinas vivas o mas de 3, muere
            elif grid[y][x] == 1 and (n_neighbors < 2 or n_neighbors > 3):
                new_grid[y][x] = 0
            else:
                new_grid[y][x] = grid[y][x]
    return new_grid

def count_neighbors(grid, posX, posY):
    count = 0
    for y in range(max(0, posY-1), min(len(grid), posY+2)):
        for x in range(max(0, posX-1), min(len(grid), posX+2)):
            if grid[y][x] == 1 and (x != posX or y != posY):
                count += 1
    return count
    