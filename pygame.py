import pygame
# Inicializace Pygame
pygame.init()
# Nastavení velikosti okna
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hra")
x1 = 50  # x souřadnice prvního kruhu
x2 = 50  # x souřadnice druhého kruhu
direction = 1  # směr druhéh kruhu 1=vpravo -1=vlevo
r = 50  # poloměr všech kružnic
ball = {"x": 300, "y": 300, "r": 50}  # třetí kruh
vector = {"dx": -1, "dy": 0.3}  # vektor pro pohyb třetího kruhu
# Hlavní smyčka
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((0, 0, 0))
    # horizontální pohyb - na konci se teleportuje
    x1 += 0.2
    if x1 > width + r:
        x1 = -r
    pygame.draw.circle(window, (140, 255, 255), (x1, 200), r)
    # horizonatné pohyb - na koncích se odráží
    x2 += 0.5 * direction
    if x2 > width - r:
        direction = -1
    elif x2 < r:
        direction = 1
    pygame.draw.circle(window, (255, 140, 200), (x2, 400), r)
    # random pohyb dle vektoru (dx,dy) na všech stranách se odráží
    ball["x"] += vector["dx"]
    ball["y"] += vector["dy"]
    if ball["x"] < r or ball["x"] > width - r:
        vector["dx"] *= -1
    if ball["y"] < r or ball["y"] > height - r:
        vector["dy"] *= -1
    pygame.draw.circle(window, (255, 255, 0), (ball["x"], ball["y"]), ball["r"])
    pygame.display.update()
pygame.quit()
