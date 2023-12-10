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
sphere_positions = [[0.2, 0, 0, 0.1], [0.1, 1, 0, 0.1], [0.3, 2, 0, 0.1], [0.1, 1.2, 0.4, 0.1], [0.2, -1, -0.3, 0.1], [0.2, -1.2, -0.8, 0.1], [0.2, -1.5, 0, 0.1], [0.2, -0.3, 0.1, 0.1], [0.2, 0.3, 0.2, 0.1]]

score = 0
time_appear = 1500

def draw_text(x, y, text):
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 600, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos2f(x, y)

    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ctypes.c_int(ord(char)))

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


def draw():
    texture = load_texture('components/grama.bmp')

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
    draw_target(*sphere_positions[current_sphere_index], 1.0, 1.0, 0.0)
    draw_scenario(*sphere_positions[current_sphere_index])

    '''
    #Deixa a câmera na arma
    adjustment_factor = 0.1  # Ajuste conforme necessário
    object_position[0] = object_position[0] + adjustment_factor * (look_at[0] - camera_position[0])
    object_position[1] = object_position[1] + adjustment_factor * (look_at[1] - camera_position[1])
    object_position[2] = object_position[2] + adjustment_factor * (look_at[2] - camera_position[2])
    '''

    glTranslatef(0, 0, 2.5)
    glRotate(135, 0, 1, 0)
    draw_gun(0.025, 0.3, 25)
    glTranslatef(-object_position[0], -object_position[1], -object_position[2])

    score_text = f"Score: {score}"
    draw_text(10, 580, score_text)

    glutSwapBuffers()

    
def TargetTimer(value):
    global current_sphere_index
    current_sphere_index = (current_sphere_index + 1) % len(sphere_positions)
    glutPostRedisplay()  
    glutTimerFunc(time_appear, TargetTimer, 0)


# def special_key_pressed(key, x, y):
#     global camera_position, object_position

#     if look_at[2] > 5:
#         look_at[2] = 5

#     if look_at[0] < -5:
#         look_at[0] = -5

#     if look_at[0] > 5:
#         look_at[0] = 5

    
#     if key == GLUT_KEY_DOWN:
#         if(look_at[1] > -1):
#             look_at[1] -= 0.1
#         else:
#             look_at[1] = -1

#     elif key == GLUT_KEY_UP:
#         if(look_at[1] < 2):
#             look_at[1] += 0.1
#         else:
#             look_at[1] = 2

#     elif key == GLUT_KEY_LEFT:
#             if(look_at[2] <= 5):
#                 look_at[0] -= math.cos(1.55)*5
#                 if(look_at[0] < 0):
#                     look_at[2] += math.sin(0.01745)*5
#                 else:
#                     look_at[2] -= math.sin(0.01745)*5
            

#     elif key == GLUT_KEY_RIGHT:
#             if(look_at[2] <= 5):
#                 look_at[0] += math.cos(1.55)*5
#                 if(look_at[0] < 0): 
#                     look_at[2] -= math.sin(0.01745)*5
#                 else:
#                     look_at[2] += math.sin(0.01745)*5
            
#     glutPostRedisplay()


def mouse_click(button, state, x, y):
    global score
    global time_appear
    global camera_position
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        norm_x = ((x / 400) - 1.0)
        norm_y = (-(y / 300) + 1.0)

        mouse_norm_x = norm_x * 2.65
        mouse_norm_y = norm_y * 2
        sphere_radius= sphere_positions[current_sphere_index][0]
        sphere_x= sphere_positions[current_sphere_index][1]
        sphere_y= sphere_positions[current_sphere_index][2]
        if ((mouse_norm_x <= sphere_x + sphere_radius) and  (mouse_norm_x >= sphere_x - sphere_radius)) and ((mouse_norm_y <= sphere_y + sphere_radius) and  (mouse_norm_y >= sphere_y - sphere_radius)):
            score+=1
        else:
            score-=1
        if (score % 5)==0:
            time_appear-=100
            


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Camera and Object Movement in 3D Space")

    glEnable(GL_DEPTH_TEST)
    glutTimerFunc(time_appear, TargetTimer, 0)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (800 / 600), 1, 50.0)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)

    glMatrixMode(GL_MODELVIEW)

    glutDisplayFunc(draw)
    
    # glutSpecialFunc(special_key_pressed)


    glutMouseFunc(mouse_click)

    glutMainLoop()

if __name__ == "__main__":
    main()
