import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import time
import ctypes
from components.target import draw_sphere

# Variáveis globais para controlar a posição da câmera
camera_position = [0, 0, 5]
look_at = [camera_position[0], camera_position[1], camera_position[2] - 1]
up_vector = [0, 1, 0]

# Variáveis globais para controlar a posição do objeto
object_position = [0, 0, 0]


def normalize_x(x):
        return((x / 200.0) - 1.0)
    
def normalize_y(y):
        return(-(y / 200.0) + 1.0)

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
    draw_sphere(0.5,0, 0, 0)

    glutSwapBuffers()


def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        viewport = glGetIntegerv(GL_VIEWPORT)
        modelview = glGetDoublev(GL_MODELVIEW_MATRIX)
        projection = glGetDoublev(GL_PROJECTION_MATRIX)

        mouse_x = x
        mouse_y = y  
        mouse_pos_near = gluUnProject(mouse_x, mouse_y, 0.0, modelview, projection, viewport)
        mouse_pos_far = gluUnProject(mouse_x, mouse_y, 1.0, modelview, projection, viewport)

        print("Mouse Position Near:", mouse_x-400, mouse_y-300)


def special_key_pressed(key, x, y):
    global camera_position, object_position


    # Atualiza a posição da câmera ou do objeto com base na tecla pressionada

    
    if key == GLUT_KEY_DOWN:
        camera_position[1] += 0.1  # Mover a câmera para trás
    elif key == GLUT_KEY_UP:
        camera_position[1] -= 0.1  # Mover o objeto para baixo
    elif key == GLUT_KEY_LEFT:
        camera_position[0] += 0.1
    elif key == GLUT_KEY_RIGHT:
        camera_position[0] -= 0.1

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

    glutMouseFunc(mouse_click)

    glutMainLoop()

if __name__ == "__main__":
    main()
