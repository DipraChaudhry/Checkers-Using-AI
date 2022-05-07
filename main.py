import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
green = (0, 255, 0)
blue = (0, 0, 128)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    pygame.init()

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('COMPUTER WINS!', True, green, blue)
    text1 = font.render('USER WINS!', True, green, blue)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)

    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            if game.winner()==(255,255,255):
                print(game.winner())
                WIN.blit(text, textRect)
                pygame.display.update()
                run = True
            elif game.winner()=='Pink':
                print(game.winner())
                WIN.blit(text1, textRect)
                pygame.display.update()
                run = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col,WIN)

        game.update()
    
    pygame.quit()

main()