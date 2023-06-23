import sys, pygame, time
import helper
pygame.init()

tamaño = 600

size = (tamaño,tamaño)
fps = 10

#COLORES
BLACK = 0, 0, 0
GRAY = 100, 100, 100

#CONSTANTES DEL JUEGO DE LA VIDA
nColumnas = 60
nFilas = 60
stop = True

anchoCelda = int(tamaño / nColumnas)
altoCelda = int(tamaño / nFilas)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#inicializar la matriz con 0's
grid = helper.create_grid(nFilas, nColumnas)

grid[20][20] = 1
grid[20][21] = 1
grid[20][22] = 1

#UPDATE
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stop = not stop

        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            pos = pygame.mouse.get_pos()
            column = pos[0] // anchoCelda
            row = pos[1] // altoCelda
            grid[row][column] = not mouseClick[2]

    #LÓGICA
    if not stop:
        grid = helper.iteracion(grid)
    

    #DIBUJO
    screen.fill(GRAY)
    helper.print_grid(screen, grid ,tamaño ,anchoCelda)

    pygame.display.flip()
    clock.tick(fps)