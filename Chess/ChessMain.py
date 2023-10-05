import pygame as p
import pygame.display

from Chess import ChessEngine

WIDTH = HEIGHT = 920
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def LoadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("AUTO CHESS")
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)
    clock =  p.time.Clock()
    screen.fill(p.Color("White"))
    gs = ChessEngine.GameState()
    LoadImages()
    running = True
    while running :
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            drawGameState(screen, gs)
            clock.tick(MAX_FPS)
            p.display.flip()

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("Gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):

    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--" :
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()







