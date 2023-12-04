import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_sphere(size,position_X,position_Y,position_Z):

    glPushMatrix()
    glTranslatef(position_X, position_Y, position_Z)
    glutWireSphere(size,20, 20)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1, 0, 0)
    glTranslatef(0, 0, 0)
    glScalef(2, 1, 0.3)
    glutWireCube(2)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1, 0, 0)
    glTranslatef(4, 0, 2)
    glRotatef(-45, 0, 1, 0)
    glScalef(2, 1, 0.3)
    glutWireCube(2)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1, 0, 0)
    glTranslatef(-4, 0, 2)
    glRotatef(45, 0, 1, 0)
    glScalef(2, 1, 0.3)
    glutWireCube(2)
    glPopMatrix()