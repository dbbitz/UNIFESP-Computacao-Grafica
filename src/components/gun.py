from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math


def cube():
     glutSolidCube(1.0)

def cylinder(radius, height, num_slices):
    quadric = gluNewQuadric()
    gluCylinder(quadric, radius, radius, height, num_slices, 1)

def disk(radius, num_slices):
    gluDisk(gluNewQuadric(), 0.0, radius, num_slices, 1)

def draw_cylinder_cover(radius, height, num_slices):
    glBegin(GL_QUAD_STRIP)

    for i in range(num_slices + 1):
        theta = (2.0 * math.pi * float(i)) / float(num_slices)
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

        glVertex3f(x, y, 0.0) 
        glVertex3f(x, y, height) 

    glEnd()
   
    glColor3f(0, 0, 0)
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0) 
    disk(radius, num_slices)
    glPopMatrix()

    glColor3f(0.2, 0.2, 0.2)
    glPushMatrix()
    glTranslatef(0.0, 0.0, height) 
    disk(radius, num_slices)
    glPopMatrix()


def draw_gun(radius, height, num_slices):
    glColor3f(0.5, 0.5, 0.5) 
    glPushMatrix()
    glScalef(0.025, 0.12, 0.048)
    glTranslatef(0.0, -0.55, 5.5)
    cube()
    glPopMatrix()

    glColor3f(0.5, 0.5, 0.5) 
    glPushMatrix()
    glScalef(0.025, 0.06, 0.05)
    glTranslatef(0.0, -0.55, 4)
    cube()
    glPopMatrix()

    glColor3f(0.2, 0.2, 0.2)
    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0)
    cylinder(radius, height, num_slices)
    glPopMatrix()

    draw_cylinder_cover(radius, height, num_slices)