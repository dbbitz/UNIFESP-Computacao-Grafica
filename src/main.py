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

gun_position = [0, 0, 0]

object_position = [0, 0]
sphere_positions = [[0.2, 0, 0, 0.1], [0.1, 1, 0, 0.1], [0.3, 2, 0, 0.1], [0.1, 1.2, 0.4, 0.1], [0.2, -1, -0.3, 0.1], [0.2, -1.2, -0.8, 0.1], [0.2, -1.5, 0, 0.1], [0.2, -0.3, 0.1, 0.1], [0.2, 0.3, 0.2, 0.1]]

aim_position = [0, 0, 0]
score = 0
time_appear = 30000


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

    glLineWidth(2.0)  # Define a largura da linha     
    glBegin(GL_LINES)
    # Linha horizontal
    aim_position[0] = 400 + look_at[0]*100
    aim_position[1] = 250 + look_at[1]*100

    glVertex2f(400 + look_at[0]*100 - 10, 250 + look_at[1]*100)
    glVertex2f(400 + look_at[0]*100 + 10, 250 + look_at[1]*100)
    # Linha vertical
    glVertex2f(400 + look_at[0]*100, 250 + look_at[1]*100 - 10)
    glVertex2f(400 + look_at[0]*100, 250 + look_at[1]*100 + 10)
    glEnd()

    

    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ctypes.c_int(ord(char)))

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


def draw():
    texture = load_texture('C:/Users/danie/Documents/GitHub/UNIFESP-Computacao-Grafica/src/components/grama.bmp')

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

    glPushMatrix()




    glTranslatef(look_at[0]/3, camera_position[1]-0.3+ look_at[1]/20 , look_at[2]/20 + 3.73)
    glRotatef(-look_at[0]*20, 0, 1, 0)  # Rotaciona o objeto
    glRotatef(look_at[1]*30, 1, 0, 0)  # Rotaciona o objeto
    draw_gun(0.025, 0.3, 25)
    glPopMatrix()
 



    score_text = f"Score: {score}"
    draw_text(10, 580, score_text)

    glutSwapBuffers()

    
def TargetTimer(value):
    global current_sphere_index
    current_sphere_index = (current_sphere_index + 1) % len(sphere_positions)
    glutPostRedisplay()  
    glutTimerFunc(time_appear, TargetTimer, 0)


def special_key_pressed(key, x, y):
    global camera_position, object_position

    if key == GLUT_KEY_LEFT:
            if (look_at[2] >= 1.22):
                look_at[2] = 1.22

            if(look_at[0] < -0.83):
                look_at[0] = -0.83
                

            if(look_at[2] <= 5):
                look_at[0] -= math.cos(1.55)*5
                if(look_at[0] < 0):
                    look_at[2] += math.sin(0.01745)*5
                else:
                    look_at[2] -= math.sin(0.01745)*5
            

    elif key == GLUT_KEY_RIGHT:
            if (look_at[2] >= 1.22):
                look_at[2] = 1.22

            if(look_at[0] > 0.83):
                look_at[0] = 0.83

            if(look_at[2] <= 5):
                look_at[0] += math.cos(1.55)*5
                if(look_at[0] < 0): 
                    look_at[2] -= math.sin(0.01745)*5
                else:
                    look_at[2] += math.sin(0.01745)*5

    elif key == GLUT_KEY_UP:
        if(look_at[1] > 0.5):
            look_at[1] = 0.5
        look_at[1] += 0.05

    elif key == GLUT_KEY_DOWN:
        if(look_at[1] < -0.5):
            look_at[1] = -0.5
        look_at[1] -= 0.05

            
    glutPostRedisplay()


def mouse_click(button, state, x, y):
    global score
    global time_appear
    global camera_position
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:

        norm_x = ((x/ 400) - 1.0)
        norm_y = (-(y/ 300) + 1.0)
        # norm_x = (((400 + look_at[0]*100)/ 400) - 1.0)*2
        # norm_y = (-((250 + look_at[1]*100)/ 300) + 1.0)

        mouse_norm_x = norm_x * 2.65
        mouse_norm_y = norm_y * 2
        sphere_radius= sphere_positions[current_sphere_index][0]
        sphere_x= sphere_positions[current_sphere_index][1]
        sphere_y= sphere_positions[current_sphere_index][2]
        if ((mouse_norm_x <= sphere_x + sphere_radius) and  (mouse_norm_x >= sphere_x - sphere_radius)) and ((mouse_norm_y <= sphere_y + sphere_radius) and  (mouse_norm_y >= sphere_y - sphere_radius)):
            score+=1
            print("acertou")
            print("Mira --> "+"X:"+ str(((400 + look_at[0]*265)/ 400)-1)+" Y:" +str((-((250 + look_at[1]*300)/ 300)+1 )))
            print(mouse_norm_x, mouse_norm_y)
            print(sphere_positions[current_sphere_index][0], sphere_positions[current_sphere_index][1], sphere_positions[current_sphere_index][2])
        else:
            score-=1
            print("errou")
            print("Mira --> "+"X:"+ str(((400 + look_at[0]*265)/ 400)-1)+" Y:" +str((-((250 + look_at[1]*265)/ 300)+1 )))
            print(mouse_norm_x, mouse_norm_y)
            print("Raio:"+str(sphere_positions[current_sphere_index][0])+ " X:"+str(sphere_positions[current_sphere_index][1])+" Y:"+str(sphere_positions[current_sphere_index][2]))
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
    
    glutSpecialFunc(special_key_pressed)


    glutMouseFunc(mouse_click)

    glutMainLoop()

if __name__ == "__main__":
    main()
