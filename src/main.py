import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import time
import ctypes
from PIL import Image
from components.target import draw_target
from components.gun import draw_gun
from components.target import draw_target
from components.target import draw_scenario
from components.target import draw_floor
from components.texture import load_texture

camera_position = [0, 0, 5]
look_at = [0, 0, 0]
up_vector = [0, 1, 0]
current_sphere_index = 0

object_position = [0, 0, 0]
sphere_positions = [[0.2, 0, 0, 0], [0.1, 1, 0, 0], [0.3, 2, 0, 0], [0.1, 1.2, 0.4, 0]]

def normalize_x(x):
        return((x / 200.0) - 1.0)
    
def normalize_y(y):
    return(-(y / 200.0) + 1.0)


def draw():
    texture=load_texture('components/grama.bmp')

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(
        camera_position[0], camera_position[1], camera_position[2],
        look_at[0], look_at[1], look_at[2],
        up_vector[0], up_vector[1], up_vector[2]
    )

    draw_floor(texture)
    glBindTexture(GL_TEXTURE_2D, 0)

    glColor3f(1.0, 1.0, 1.0)  
    glTranslatef(*object_position)
    draw_target(*sphere_positions[current_sphere_index])
    draw_scenario(*sphere_positions[current_sphere_index])

    '''
    #Deixa a camera na arma
    adjustment_factor = 0.1  # Ajuste conforme necessário
    object_position[0] = object_position[0] + adjustment_factor * (look_at[0] - camera_position[0])
    object_position[1] = object_position[1] + adjustment_factor * (look_at[1] - camera_position[1])
    object_position[2] = object_position[2] + adjustment_factor * (look_at[2] - camera_position[2])
    '''

    glTranslatef(0, 0, 2.5)
    glRotate(135, 0, 1, 0)
    draw_gun(0.025, 0.3, 25)
    glTranslatef(-object_position[0], -object_position[1], -object_position[2])
    
   

    glutSwapBuffers()

def TargetTimer(value):
    global current_sphere_index
    current_sphere_index = (current_sphere_index + 1) % len(sphere_positions)
    glutPostRedisplay()  
    glutTimerFunc(1500, TargetTimer, 0)


def special_key_pressed(key, x, y):
    global camera_position, object_position

    if look_at[2] > 5:
        look_at[2] = 5

    if look_at[0] < -5:
        look_at[0] = -5

    if look_at[0] > 5:
        look_at[0] = 5

    
    if key == GLUT_KEY_DOWN:
        if(look_at[1] > -1):
            look_at[1] -= 0.1
        else:
            look_at[1] = -1

    elif key == GLUT_KEY_UP:
        if(look_at[1] < 2):
            look_at[1] += 0.1
        else:
            look_at[1] = 2

    elif key == GLUT_KEY_LEFT:
            if(look_at[2] <= 5):
                look_at[0] -= math.cos(1.55)*5
                if(look_at[0] < 0):
                    look_at[2] += math.sin(0.01745)*5
                else:
                    look_at[2] -= math.sin(0.01745)*5
            

    elif key == GLUT_KEY_RIGHT:
            if(look_at[2] <= 5):
                look_at[0] += math.cos(1.55)*5
                if(look_at[0] < 0): 
                    look_at[2] -= math.sin(0.01745)*5
                else:
                    look_at[2] += math.sin(0.01745)*5
            
    glutPostRedisplay()


def mouse_click(button, state, x, y):
    global camera_position

    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        print(f"Mouse position - X: {normalize_x(y)}, Y: {normalize_y(x)}")

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Camera and Object Movement in 3D Space")

    glEnable(GL_DEPTH_TEST)
    glutTimerFunc(1500, TargetTimer, 0)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (800 / 600), 1, 50.0)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)

    glMatrixMode(GL_MODELVIEW)

    glutDisplayFunc(draw)
    
    glutSpecialFunc(special_key_pressed)


    glutMouseFunc(mouse_click)

    glutMainLoop()

if __name__ == "__main__":
    main()
