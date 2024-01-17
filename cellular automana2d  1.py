import random
import pygame
import sys
width,height = 600,600
reselusain = 5
col = width//reselusain
row = height//reselusain

def draw_grid(screen,a):
    for row_index, row in enumerate(a):
        for i in range(len(row)):
            x = i * reselusain
            y =  row_index* reselusain
            a = row[i]
            if a ==0:
                color = (0,0,0) 
            elif a == 1: 
                 color = (255,255,255)        
            pygame.draw.rect(screen, color, (x, y, reselusain, reselusain)) 
def update_grid(grid):
    nextgrid = [[0] * len(row) for row in grid] 

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            b = clc(grid, i, j)
            if b == 3:
                nextgrid[i][j] = 1
            elif b >= 4 or b < 2:
                nextgrid[i][j] = 0
            else:
                nextgrid[i][j] = grid[i][j]

    return nextgrid


def clc(grid, i, j):
    sum = 0
    for s in range(-1, 2):
        for l in range(-1, 2):
            sum += grid[(i + s) % len(grid)][(j + l) % len(grid[0])]

    return sum - grid[i][j]

def make2darray(col, row):
    grid = [[] for _ in range(col)]
    for i, inner_row in enumerate(grid):
        for j in range(row):
            a = random.randint(0, 1)
            inner_row.append(a)
    return grid

def main():
    a = make2darray(col, row)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(f"Cellular automaton 2d version")

    clock = pygame.time.Clock()
    fps = 10  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

     
        a = update_grid(a)

      
        screen.fill((255, 255, 255))  
        draw_grid(screen, a)

        pygame.display.flip()
        clock.tick(fps)

if __name__ == "__main__":
    main()


