import pygame
import time
pygame.init()

window_width = 540 #px Make sure to also adjust the font size when changing this
window_height = 540 #height should be the same as width

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Backtracking algorithm")
background = pygame.image.load('board.jpg').convert()
background = pygame.transform.smoothscale(background, (window_width, window_height))
screen.blit(background, (0, 0))
font = pygame.font.SysFont('arial', 50) #Set font and font size
framerate = 0 #ms between each board update

pygame.display.update()

#This needs to be a 2D array, with each subarray representing a row and empty cells being 0s
puzzle = [[9, 0, 0, 0, 8, 0, 0, 0, 1], 
 [0, 0, 0, 4, 0, 6, 0, 0, 0],
 [0, 0, 5, 0, 7, 0, 3, 0, 0],
 [0, 6, 0, 0, 0, 0, 0, 4, 0],
 [4, 0, 1, 0, 6, 0, 5, 0, 8],
 [0, 9, 0, 0, 0, 0, 0, 2, 0],
 [0, 0, 7, 0, 3, 0, 2, 0, 0],
 [0, 0, 0, 7, 0, 5, 0, 0, 0],
 [1, 0, 0, 0, 4, 0, 0, 0, 7]]

org_puzzle = puzzle #Used for displaying the board

def sudoku():
    is_quit() #Check if user has issued a quit command (eg. pressing the X button)
    
    #Find next 0
    for i, row in enumerate(puzzle):
        if 0 in row:
            index_0 = row.index(0)
            for num in range(1, 10):
                if check_num((num, i, index_0)) == True:
                    puzzle[i][index_0] = num
                    display_current_board()

                    if sudoku() == False:
                        continue
                else:
                    continue

            puzzle[i][index_0] = 0
            display_current_board()

            return False

    print("Puzzle done!")
    print(puzzle)
    while True:
        is_quit()

def check_num(last_added):
    #Last_added = [num, row, column]
    #Check row
    if last_added[0] in puzzle[last_added[1]]:
        return False
    #Check column
    for i in range(9):
        if last_added[0] == puzzle[i][last_added[2]]:
            return False
    #Check box
    box_column = last_added[2] // 3
    box_row = last_added[1] // 3

    box = [puzzle[box_row * 3][box_column * 3:box_column * 3 + 3], puzzle[box_row * 3 + 1][box_column * 3:box_column * 3 + 3], puzzle[box_row * 3 + 2][box_column * 3:box_column * 3 + 3]]       
    if (last_added[0] in box[0]) or (last_added[0] in box[1]) or (last_added[0] in box[2]):
        return False

    return True

def display_org_board():
    pygame.event.get()
    screen.blit(background, (0, 0))
    for i, row in enumerate(puzzle):
        for num in row:
            if num != 0:
                text = font.render(str(num), True, (10, 10, 10))
                text_rect = text.get_rect()
                text_rect.center = ((window_width / 18) + row.index(num) * (window_width / 9), (window_width / 18) + i * (window_width / 9)) 
                screen.blit(text, text_rect)

def display_current_board():
    pygame.event.get()
    display_org_board()

    for i, row in enumerate(puzzle):
        for num in row:
            if num != 0 and num != org_puzzle[i][row.index(num)]:
                text = font.render(str(num), True, (250, 0, 0))
                text_rect = text.get_rect()
                text_rect.center = ((window_width / 18) + row.index(num) * (window_width / 9), (window_width / 18) + i * (window_width / 9)) 
                screen.blit(text, text_rect)
    time.sleep(framerate / 1000)
    pygame.display.update()

def is_quit():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()

if __name__ == "__main__":
    display_org_board()
    pygame.display.update()
    
    if sudoku() == False:
        print('The puzzle has no solutions!')

