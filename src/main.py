import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import time
import ctypes
from components.target import draw_target

# Variáveis globais para controlar a posição da câmera
camera_position = [0, 0, 5]
look_at = [0, 0, 0]
up_vector = [0, 1, 0]
current_sphere_index = 0

# Variáveis globais para controlar a posição do objeto
object_position = [0, 0, 0]
sphere_positions = [[0.5, 7, 0, 0], [0.2, 2, 3, 5], [0.3, 4, 6, 8], [0.2, 0, 0, 0], [0.1, 1, 0, 0], [0.3, 2, 0, 0]]


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
    draw_target(*sphere_positions[current_sphere_index])



    glutSwapBuffers()

def TargetTimer(value):
    global current_sphere_index
    current_sphere_index = (current_sphere_index + 1) % len(sphere_positions)
    glutPostRedisplay()  
    glutTimerFunc(1500, TargetTimer, 0)


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
    global camera_position, object_position


    # Atualiza a posição da câmera ou do objeto com base na tecla pressionada

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
            
                    



    print("Look at | X: " + str(look_at[0]) + " Y: " + str(look_at[1]) + " Z: " + str(look_at[2]))
    print("Camera  | X: " + str(camera_position[0]) + " Y: " + str(camera_position[1]) + " Z: " + str(camera_position[2]))

    glutPostRedisplay()




def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Camera and Object Movement in 3D Space")

    glEnable(GL_DEPTH_TEST)
    glutTimerFunc(1500, TargetTimer, 0)
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
