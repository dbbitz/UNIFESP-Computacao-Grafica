import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from components.texture import load_texture

def toldo(c1, c2, c3):
    #pilastra direita do amarelo
    glPushMatrix()
    glColor3f(0.6, 0.3, 0.1)
    glTranslatef(2, 0, 0.5)
    glScalef(0.1, 1, 0.1)
    glutSolidCube(2)
    glPopMatrix()

    #pilastra esquerda do amarelo
    glPushMatrix()
    glColor3f(0.6, 0.3, 0.1)
    glTranslatef(-2, 0, 0.5)
    glScalef(0.1, 1, 0.1)
    glutSolidCube(2)
    glPopMatrix()

    #toldo amarelo
    glPushMatrix()
    glColor3f(c1,c2,c3)
    glTranslatef(0, 1, 0)
    glScalef(2.1, 0.2, 0.65)
    glutSolidCube(2)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1, 1, 1)
    glTranslatef(0, 1, 0)
    glScalef(1, 0.21, 0.66)
    glutSolidCube(2)
    glPopMatrix()

    #parede de tras
    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.5, 0.5)  # Cor cinza
    glVertex3f(-2.0, -1.0, -0.3)
    glVertex3f(-2.0,  1.0, -0.3)
    glVertex3f( 2.0,  1.0, -0.3)
    glVertex3f(2.0, -1.0, -0.3)
    glEnd() 

# Função para desenhar o chão
def draw_floor(texture):
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(-20, -1, -20)
    glTexCoord2f(1.0, 0.0); glVertex3f(20, -1, -20)
    glTexCoord2f(1.0, 1.0); glVertex3f(20, -1, 20)
    glTexCoord2f(0.0, 1.0); glVertex3f(-20, -1, 20)
    glEnd()
    

def draw_scenario(size,position_X,position_Y,position_Z):
    #CHAO
    '''
    glBindTexture(GL_TEXTURE_2D, loadTexture('grama.bmp'))
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.5, 0.5)  # Cor cinza para o chão
    glVertex3f(-2.0, -1.0, -0.3)
    glVertex3f(-2.0, -1.0,  0.3)
    glVertex3f(-2.0,  1.0, -0.3)
    glVertex3f(-2.0,  1.0,  0.3)
    glEnd() 
    '''

    ##########BLOCO DO MEIO-AMERELO##############
    #arena do meio- amarela
    glPushMatrix()
    glColor3f(1, 1, 0)
    glTranslatef(0, 0, 0)
    glScalef(2, 1, 0.3)
    glutWireCube(2)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0, 0)
    toldo(1, 1, 0)
    glPopMatrix()

    #############BLOCO DA DIREITA- ROSA###############
    #arena da direita- rosa
    glPushMatrix()
    glColor3f(1, 0, 1)
    glTranslatef(4, 0, 2)
    glRotatef(-45, 0, 1, 0)
    glScalef(2, 1, 0.3)
    glutWireCube(2)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(4, 0, 2)
    glRotatef(-45, 0, 1, 0)
    toldo(1,0,1)
    glPopMatrix()
    
    #############BLOCO DA DIREITA- ROSA###############
    #arena da esquerda- vermelha
    glPushMatrix()
    glColor3f(1, 0, 0)
    glTranslatef(-4, 0, 2)
    glRotatef(45, 0, 1, 0)
    glScalef(2, 1, 0.3)
    glutWireCube(2)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-4, 0, 2)
    glRotatef(45, 0, 1, 0)
    toldo(1,0,0)
    glPopMatrix()


def draw_target(size, position_X, position_Y, position_Z, r, g, b):
    glPushMatrix()
    glTranslatef(position_X, position_Y, position_Z)
    glColor3f(r, g, b)
    glutSolidSphere(size, 20, 20)
    glPopMatrix()
    