import pygame
from Strategy import RunAwayStrategy
from Collisions import BigTreatCollision, GhostCollision
from Treats import BigTreat
from Colors import Colors
from Board import Board
from GameConstants import GameConstants


if __name__ == '__main__':

    pygame.init()
    board = Board("board2.txt", GameConstants.FACTOR)
    screen = pygame.display.set_mode((board.length, board.width + board.factor))
    clock = pygame.time.Clock()
    FPS = GameConstants.FPS  # Frames per second.

    factor = board.factor
    pacman = board.pacman
    walls_xy = board.walls_xy

    pygame.display.set_caption('Show Text')
    font = pygame.font.Font('freesansbold.ttf', 32)
    przegranko_text = font.render('PRZEGRANKO', True, Colors.BLACK, Colors.WHITE)
    wygranko_text = font.render('WYGRANKO', True, Colors.BLACK, Colors.WHITE)
    textRect = przegranko_text.get_rect()
    textRect.center = (board.length // 2, board.width // 2)
    textRect2 = wygranko_text.get_rect()
    textRect2.center = (board.length // 2, board.width // 2)
    textRect3 = wygranko_text.get_rect()
    textRect3.center = (board.length - board.factor, board.width + board.factor // 2)

    Game = True
    game_finished = 0
    i = 0
    while Game:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                Game = False

            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    pacman.onKeyPressed(event.key)

        if not game_finished:

            screen.fill(Colors.BLACK)
            pacman.move()

            for wall in board.walls:
                wall.draw(screen)

            for treat in board.treats:
                treat.draw(screen)
                if treat.center == pacman.center:
                    if isinstance(treat, BigTreat) and not treat.is_eaten:
                        BigTreatCollision.execute_collision(board.ghosts)
                    treat.eat()

            for ghost in board.ghosts:
                if ghost.waiting > 0:
                    ghost.waiting -= 1

                if board.ghost_pacman_are_too_close(ghost):

                    GhostCollision.execute_collision(board, ghost)

                    if not ghost.how_long_it_can_be_eaten:
                        if pacman.lives == 0:
                            game_finished = 1
                            screen.blit(przegranko_text, textRect)
                        else:
                            board.reset_objects_positions()
                            break
                    ghost.how_long_it_can_be_eaten = 0
                ghost.set_direction()
                ghost.move()

                if ghost.how_long_it_can_be_eaten > 0:
                    if i < 4:
                        ghost.draw(screen)
                    elif i < 9:
                        pass
                    else: i = 0
                    ghost.how_long_it_can_be_eaten -= 1

                else:
                    if isinstance(ghost.strategy, RunAwayStrategy):
                        ghost.strategy = ghost.main_strategy
                        ghost.speed.reset_speed()
                    ghost.draw(screen)

            if board.are_all_treats_eaten():
                game_finished = 1
                screen.blit(wygranko_text, textRect2)

            lives_text = font.render("lives: "+str(pacman.lives), True, Colors.WHITE, Colors.BLACK)
            screen.blit(lives_text, textRect3)
            pacman.draw(screen)
            pygame.display.update()  # Or pygame.display.flip()

            i += 1

    pygame.quit()
