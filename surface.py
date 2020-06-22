# Importar librerias
import pygame
import sys

# Inicializar Pygame
pygame.init()

## Crear la ventana
### Específicar dimensiones
width=400
height=500
surface=pygame.display.set_mode((width, height))

### Poner título
pygame.display.set_caption("Título de la ventana")


### Crear colores:
dark=(10, 10, 10)
my_color=(0,215,200)
verde_claro=(0,255,100)
amarillo_palido=(250, 200, 100)

## Crear rectángulos:
rectangulo_1=pygame.Rect(200, 250, 50, 25)
rectangulo_1.center=(width//2, height//2)
print(rectangulo_1.x)
print(rectangulo_1.y)

## Interactuar con la ventana (Escuchar los eventos que puede tener la ventana)
while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Crear relleno y actualizar
    surface.fill(dark)
    pygame.draw.rect(surface, my_color, rectangulo_1)
    pygame.draw.rect(surface, verde_claro , (100, 100, 120, 40))
    pygame.draw.circle(surface, amarillo_palido, (50, 50), 25)
    pygame.draw.line(surface, (255, 0, 0), (50,50), (50, 100), 4)
    pygame.display.update()



