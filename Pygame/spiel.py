import pygame
import sys
import random

# Initialisiere Pygame
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 800, 600

# Erstelle das Spielfenster
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mein Pygame-Spiel")

# Lade Bilder für Spieler, Gegner, Herzen und Power-Up
player_image = pygame.image.load('ben.jpg')
player_image = pygame.transform.scale(player_image, (75, 75))

enemy_image = pygame.image.load('c#.png')
enemy_image = pygame.transform.scale(enemy_image, (50, 50))

heart_image = pygame.image.load('monster.jpg')
heart_image = pygame.transform.scale(heart_image, (30, 30))

powerup_image = pygame.image.load('volleyball.png')  # Du musst ein Bild für das Power-Up bereitstellen
powerup_image = pygame.transform.scale(powerup_image, (50, 50))

# Spieler-Position und Geschwindigkeit
player = {"x": WIDTH // 2 - 25, "y": HEIGHT - 50, "speed": 6, "powerup_active": False}

# Punkte und Leben
score = 0
lives = 3
font = pygame.font.Font(None, 36)

# Gegner
enemies = []

def create_enemy():
    enemy_size = 50
    enemy_x = random.randint(0, WIDTH - enemy_size)
    enemy_y = -enemy_size
    enemy_speed = random.randint(5, 8)
    return {"x": enemy_x, "y": enemy_y, "size": enemy_size, "speed": enemy_speed}

# Power-Up
powerup = {"x": 0, "y": 0, "active": False, "duration": 5, "timer": 0}

# Clock-Objekt zur Steuerung der Framerate
clock = pygame.time.Clock()

# Timer für das Power-Up
powerup_spawn_timer = 0

# Hauptspiel-Schleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bewegung des Spielers
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player["x"] > 0:
        player["x"] -= player["speed"]
    if keys[pygame.K_RIGHT] and player["x"] < WIDTH - 50:
        player["x"] += player["speed"]

    # Erstelle neue Gegner
    if random.random() < 0.08:
        enemies.append(create_enemy())

    # Bewegung der Gegner
    for enemy in enemies:
        enemy["y"] += enemy["speed"]
        if enemy["y"] > HEIGHT:
            enemies.remove(enemy)
            score += 1

    # Spawn des Power-Ups alle 20 Sekunden
    powerup_spawn_timer += 1
    if powerup_spawn_timer >= 900:
        powerup["x"] = random.randint(0, WIDTH - 30)
        powerup["y"] = HEIGHT - 40
        powerup["active"] = True
        powerup_spawn_timer = 0

    # Überprüfe Kollision mit Power-Up
    if (
            player["x"] < powerup["x"] + 30
            and player["x"] + 75 > powerup["x"]
            and player["y"] < powerup["y"] + 30
            and player["y"] + 75 > powerup["y"]
    ):
        powerup["active"] = False
        powerup["timer"] = powerup["duration"]
        player["powerup_active"] = True
        # Setze die Position des Power-Ups außerhalb des sichtbaren Bereichs
        powerup["x"] = -100
        powerup["y"] = -100

        # Aktiviere Power-Up-Effekt
    if player["powerup_active"]:
        player["speed"] = 8
        # Verwende die Zeitdifferenz zwischen den Frames (in Sekunden) für die Abnahme des Timers
        dt = clock.tick(60) / 1000  # Zeitdifferenz in Sekunden
        powerup["timer"] -= dt
        if powerup["timer"] <= 0:
            player["powerup_active"] = False
            player["speed"] = 4

    # Kollision mit Gegnern überprüfen
    for enemy in enemies:
        if (
            player["x"] < enemy["x"] + enemy["size"]
            and player["x"] + 75 > enemy["x"]
            and player["y"] < enemy["y"] + enemy["size"]
            and player["y"] + 75 > enemy["y"]
        ):
            # Spieler verliert ein Leben, wenn er den Gegner berührt
            lives -= 1
            if lives == 0:
                running = False
            # Entferne den Gegner nach der Kollision
            enemies.remove(enemy)

    # Hintergrund zeichnen
    screen.fill((255, 255, 255))

    # Spieler zeichnen
    screen.blit(player_image, (player["x"], player["y"]))

    # Gegner zeichnen
    for enemy in enemies:
        screen.blit(enemy_image, (enemy["x"], enemy["y"]))

    # Herzen zeichnen
    for i in range(lives):
        screen.blit(heart_image, (10 + i * 35, 10))

    # Power-Up zeichnen, wenn aktiv
    if powerup["active"]:
        screen.blit(powerup_image, (powerup["x"], powerup["y"]))

    # Punkteanzeige
    score_text = font.render("Punkte: {}".format(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 50))

    # Fenster aktualisieren
    pygame.display.flip()

    # Framerate festlegen
    clock.tick(60)

# Anzeige der Endpunktzahl
end_text = font.render("Du hast verloren! Deine Punktzahl: {}".format(score), True, (255, 0, 0))
screen.blit(end_text, (WIDTH // 2 - 200, HEIGHT // 2 - 20))
pygame.display.flip()

# Warte kurz, damit der Spieler die Endpunktzahl sehen kann
pygame.time.delay(3000)

# Pygame beenden
pygame.quit()
sys.exit()
