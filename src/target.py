import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_sphere(position_X,position_Y,position_Z):

    glTranslatef(position_X, position_Y, position_Z)
    glutWireSphere(0.1, 20, 20)
    print("Sphere Position:", position_X, position_Y, position_Z)