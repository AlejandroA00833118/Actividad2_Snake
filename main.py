from turtle import *
from random import randrange
from freegames import square, vector
from random import choice


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
# Creación de lista de colores
colores = ['pink', 'purple', 'yellow', 'blue', 'green']
# Elegir colores iniciales al azar de la lista
color = choice(colores)
color2 = choice(colores)
# Verificar que los dos colores sean diferentes
while color2 == color:
    # Cambiar uno de los colores en caso de que ambos sean iguales
    color2 = choice(colores)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

# Creación de nueva función para manejar la generación de la comida de manera independiente
def comida():
    # Generar las coordenadas de la comida
    food.x = randrange(-15, 15) * 10
    food.y = randrange(-15, 15) * 10
    # Uso de un contador para que cada segundo se genere una nueva posición para la comida 
    ontimer(comida, 1000)

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color2)

    square(food.x, food.y, 9, color)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
# Llamada a la función para el cambio de posición de la comida
comida()
done()