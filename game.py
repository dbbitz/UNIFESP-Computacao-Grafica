from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

# Variáveis globais para controlar a posição do boneco
stick_figure_position = [0, 0, 0]
window_width, window_height = 800, 600

def draw_cube():
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex3f(-0.25,0.25,0.25)
    glVertex3f(0.25,0.25,0.25)
    glVertex3f(0.25,-0.25,0.25)
    glVertex3f(-0.25,-0.25,0.25)
    glEnd()
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_POLYGON)
    glVertex3f(-0.25,0.25,-0.25)
    glVertex3f(0.25,0.25,-0.25)
    glVertex3f(0.25,-0.25,-0.25)
    glVertex3f(-0.25,-0.25,-0.25)
    glEnd()
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(0.25,-0.25,0.25)
    glVertex3f(0.25,0.25,0.25)
    glVertex3f(0.25,0.25,-0.25)
    glVertex3f(0.25,-0.25,-0.25)
    glEnd()
    glColor3f(1.0,1.0,0.0)
    glBegin(GL_POLYGON)
    glVertex3f(-0.25,-0.25,0.25)
    glVertex3f(-0.25,0.25,0.25)
    glVertex3f(-0.25,0.25,-0.25)
    glVertex3f(-0.25,-0.25,-0.25)
    glEnd()
    glColor3f(1.0,0.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(-0.25,0.25,0.25)
    glVertex3f(0.25,0.25,0.25)
    glVertex3f(0.25,0.25,-0.25)
    glVertex3f(-0.25,0.25,-0.25)
    glEnd()
    glColor3f(0.0,1.0,1.0)
    glBegin(GL_POLYGON)
    glVertex3f(-0.25,-0.25,0.25)
    glVertex3f(0.25,-0.25,0.25)
    glVertex3f(0.25,-0.25,-0.25)
    glVertex3f(-0.25,-0.25,-0.25)
    glEnd()
    

def draw_stick_figure():
    glPushMatrix()
    glTranslatef(*stick_figure_position)
    
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 1.5, 0)  # Tronco alongado para a cabeça

    glVertex3f(0, 1.3, 0)
    glVertex3f(-0.5, 0.8, 0)  # Braço esquerdo

    glVertex3f(0, 1.3, 0)
    glVertex3f(0.5, 0.8, 0)  # Braço direito

    glVertex3f(0, 0, 0)
    glVertex3f(-0.5, -0.8, 0)  # Perna esquerda

    glVertex3f(0, 0, 0)
    glVertex3f(0.5, -0.8, 0)  # Perna direita

    
    glEnd()

    glPopMatrix()

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)  # Câmera na posição (0, 0, 5) olhando para (0, 0, 0)

    draw_stick_figure()

    draw_cube()


    glutSwapBuffers()

def special_key_pressed(key, x, y):
    global stick_figure_position

    # Atualiza a posição do boneco com base na tecla pressionada
    if key == GLUT_KEY_LEFT:
        stick_figure_position[0] -= 0.1  # Mover para a esquerda
    elif key == GLUT_KEY_RIGHT:
        stick_figure_position[0] += 0.1  # Mover para a direita
    elif key == GLUT_KEY_UP:
        stick_figure_position[1] += 0.1  # Mover para frente
    elif key == GLUT_KEY_DOWN:
        stick_figure_position[1] -= 0.1  # Mover para trás

    print(stick_figure_position)

    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Stick Figure FPS")

    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (800 / 600), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Registra a função de desenho e a função para teclas especiais
    glutDisplayFunc(draw)
    glutSpecialFunc(special_key_pressed)

    glutMainLoop()

if __name__ == "__main__":
    main()
