import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import time
import ctypes

# Variáveis globais para controlar a posição da câmera
camera_position = [0, 0, 5]
look_at = [camera_position[0], camera_position[1], camera_position[2] - 1]
up_vector = [0, 1, 0]

# Variáveis globais para controlar a posição do objeto
object_position = [0, 0, 0]

def draw_cube():
    glutWireCube(1.0)

def draw_target():
    # Tamanho dos lados, altura, n lados, n alturas
    glutWireCylinder(0.3, 0.3, 20, 1)

    glTranslatef(0, 0, 0.3)
    glutSolidCylinder(0.3, 0.01, 20, 1)

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(
        camera_position[0], camera_position[1], camera_position[2],
        look_at[0], look_at[1], look_at[2],
        up_vector[0], up_vector[1], up_vector[2]
    )

    glColor3f(1.0, 1.0, 1.0)  # Cor do objeto (branco)
    glTranslatef(*object_position)
    draw_cube()

    glutSwapBuffers()

def special_key_pressed(key, x, y):
    global camera_position, object_position


    # Atualiza a posição da câmera ou do objeto com base na tecla pressionada
    
    if key == GLUT_KEY_DOWN:
        camera_position[1] += 0.1  # Mover a câmera para trás
    elif key == GLUT_KEY_UP:
        camera_position[1] -= 0.1  # Mover o objeto para baixo
    elif key == GLUT_KEY_LEFT:
        object_position[0] += 0.1
    elif key == GLUT_KEY_RIGHT:
        object_position[0] -= 0.1

    print("Camera Position:", camera_position)
    print("Object Position:", object_position)

    glutPostRedisplay()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Camera and Object Movement in 3D Space")

    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (800 / 600), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)

    # Registra a função de desenho e a função para teclas especiais
    glutDisplayFunc(draw)
    
    glutSpecialFunc(special_key_pressed)

    glutMainLoop()

if __name__ == "__main__":
    main()
