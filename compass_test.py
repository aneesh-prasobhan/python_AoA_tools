import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    #windows name 
    pygame.display.set_caption("Angle of Arrival")
    clock = pygame.time.Clock()
    running = True
    angle = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (0, 0, 0), (200, 200), 200, 2)
        x = 200 + 200 * math.cos(math.radians(angle))
        y = 200 - 200 * math.sin(math.radians(angle))
        pygame.draw.line(screen, (255, 0, 0), (200, 200), (x, y), 2)
        pygame.display.update()

        # slowly increase the angle
        angle += 1
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
