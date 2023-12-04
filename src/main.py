import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import time
import ctypes
import numpy as np
from components.target import draw_arena

# Posição da câmera
camera_pos = [0.0, 0.0, 5.0]
camera_angle = 0.0

# Direção para onde a câmera está olhando
camera_lookat = [0.0, 0.0, 0.0]

# Vetor de 'up'
camera_up = [0.0, 1.0, 0.0]

# Ângulo de rotação inicial


# Variáveis globais para controlar a posição do objeto
object_position = [0, 0, 0]


def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(
        camera_pos[0], camera_pos[1], camera_pos[2],
        camera_lookat[0], camera_lookat[1], camera_lookat[2],
        camera_up[0], camera_up[1], camera_up[2]
    )

    glColor3f(1.0, 1.0, 1.0)  # Cor do objeto (branco)
    glTranslatef(*object_position)
    draw_arena(0.5,0, 0, 0)

    glPushMatrix()
    glColor3f(1, 0, 0)
    glTranslatef(camera_lookat[0],camera_lookat[1], camera_lookat[2])
    glScalef(0.1, 0.1, 0.1)
    glutWireCube(2)
    glPopMatrix()



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



def special_key_pressed(key, x, y):
    global camera_pos, object_position,camera_angle, camera_lookat
    
    # if key == GLUT_KEY_DOWN:
    #     if(look_at[1] > -1):
    #         look_at[1] -= 0.1
    #     else:
    #         look_at[1] = -1

    # elif key == GLUT_KEY_UP:
    #     if(look_at[1] < 2):
    #         look_at[1] += 0.1
    #     else:
    #         look_at[1] = 2

    if key == GLUT_KEY_LEFT:
        camera_angle += 5.0
        camera_lookat[0] = -math.sin(math.radians(camera_angle))*5
        camera_lookat[2] = 5-math.cos(math.radians(camera_angle))*5
        if camera_angle >= 360.0:
            camera_angle -= 360.0
            

    elif key == GLUT_KEY_RIGHT:
        camera_angle -= 5.0
        camera_lookat[0] = -math.sin(math.radians(camera_angle))*5
        camera_lookat[2] = 5-math.cos(math.radians(camera_angle))*5
        if camera_angle <= 0.0:
            camera_angle += 360.0
            
                    



    print("Look at | X: " + str(camera_lookat[0]) + " Y: " + str(camera_lookat[1]) + " Z: " + str(camera_lookat[2]))
    print("angle: " + str(camera_angle))
    glutPostRedisplay()




def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Camera and Object Movement in 3D Space")

    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (800 / 600), 1, 50.0)

    glMatrixMode(GL_MODELVIEW)

    # Registra a função de desenho e a função para teclas especiais
    glutDisplayFunc(draw)
    
    glutSpecialFunc(special_key_pressed)


    glutMouseFunc(mouse_click)

    glutMainLoop()

if __name__ == "__main__":
    main()
