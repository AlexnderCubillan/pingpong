import pygame
import random

# Inicialización de Pygame
pygame.init()

# Definición de constantes
ANCHO = 800
ALTO = 600
COLOR_BOLA = (255, 255, 255)
COLOR_JUGADOR = (255, 0, 0)
VELOCIDAD_BOLA = 5
VELOCIDAD_JUGADOR = 5

# Configuración de la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Ping Pong')

# Clase para la Bola
class Bola:
    def __init__(self):
        self.x = ANCHO // 2
        self.y = ALTO // 2
        self.radio = 10
        self.velocidad_x = VELOCIDAD_BOLA * random.choice([-1, 1])
        self.velocidad_y = VELOCIDAD_BOLA * random.choice([-1, 1])
        self.rect = pygame.Rect(self.x - self.radio, self.y - self.radio, self.radio * 2, self.radio * 2)

    def actualizar(self):
        self.x += self.velocidad_x
        self.y += self.velocidad_y
        self.rect.move_ip(self.velocidad_x, self.velocidad_y)

    def mostrar(self):
        pygame.draw.circle(pantalla, COLOR_BOLA, (self.x, self.y), self.radio)

# Clase para el Jugador
class Jugador:
    def __init__(self, x):
        self.x = x
        self.y = ALTO // 2
        self.ancho = 10
        self.alto = 100
        self.velocidad = VELOCIDAD_JUGADOR
        self.rect = pygame.Rect(self.x, self.y - self.alto // 2, self.ancho, self.alto)

    def actualizar(self, arriba, abajo):
        if arriba:
            self.y -= self.velocidad
        if abajo:
            self.y += self.velocidad
        self.rect.y = self.y - self.alto // 2

    def mostrar(self):
        pygame.draw.rect(pantalla, COLOR_JUGADOR, self.rect)

# Inicialización de la bola y los jugadores
bola = Bola()
jugador1 = Jugador(30)
jugador2 = Jugador(ANCHO - 30)

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Actualización de la bola y los jugadores
    bola.actualizar()
    jugador1.actualizar(pygame.key.get_pressed()[pygame.K_w], pygame.key.get_pressed()[pygame.K_s])
    jugador2.actualizar(pygame.key.get_pressed()[pygame.K_UP], pygame.key.get_pressed()[pygame.K_DOWN])

    # Comprobación de colisiones con los jugadores
    if bola.rect.colliderect(jugador1.rect) or bola.rect.colliderect(jugador2.rect):
        bola.velocidad_x *= -1

    # Comprobación de colisiones con los bordes superior e inferior
    if bola.y - bola.radio <= 0 or bola.y + bola.radio >= ALTO:
        bola.velocidad_y *= -1

    # Comprobación de salida de la pelota por los lados
    if bola.x - bola.radio <= 0:
        print("¡Jugador 2 gana!")
        ejecutando = False
    elif bola.x + bola.radio >= ANCHO:
        print("¡Jugador 1 gana!")
        ejecutando = False

    # Rellenar la pantalla con color negro
    pantalla.fill((0, 0, 0))

    # Dibujar la bola y los jugadores
    bola.mostrar()
    jugador1.mostrar()
    jugador2.mostrar()

    # Actualizar la pantalla
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
