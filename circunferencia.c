#include <glut.h>
#include <stdio.h>
#include <math.h>

float pointX_1 = 0.0;
float pointY_1 = 0.0;

int firstPoint = 1;

GLfloat colors[][9] = {
    {1.0f, 0.0f, 0.0f}, // Vermelho
    {0.0f, 1.0f, 0.0f}, // Verde
    {0.0f, 0.0f, 1.0f}, // Azul
    {1.0f, 1.0f, 0.0f}, // Amarelo
    {1.0f, 0.0f, 1.0f}, // Magenta
    {0.0f, 1.0f, 1.0f}, // Ciano
    {1.0f, 1.0f, 1.0f}, // Branco
    {0.0f, 0.0f, 0.0f}, // Preto
    {0.5f, 0.5f, 0.5f}  // Cinza

};
int currentColorIndex = 0;

int mouseClicked = 0;

void display()
{
    glClear(GL_COLOR_BUFFER_BIT);

    glPointSize(5.0); // Tamanho do ponto

    if (mouseClicked)
    {
        // Desenha o primeiro ponto
        glColor3fv(colors[currentColorIndex]);
        glBegin(GL_POINTS);
        glVertex2f(pointX_1, pointY_1);
        glEnd();

        // Desenha circunfernecia em volta do ponto

        float x = pointX_1;
        float y = pointY_1;

        float r = 0.5;

        glColor3fv(colors[currentColorIndex]);

        glBegin(GL_POINTS);

        for (float i = 0; i < 3.14; i += 0.01)
        {
            glVertex2f((x + cos(i) * r), (y + sin(i) * r));
            glVertex2f((x + cos(i) * r), (y - sin(i) * r));
        }

        glEnd();
    }

    glFlush();
}

void mouse(int button, int state, int x, int y)
{
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
    {

        // Mapeia as coordenadas do clique para as coordenadas OpenGL
        float mappedX = (float)x / glutGet(GLUT_WINDOW_WIDTH) * 2 - 1;
        float mappedY = -(float)y / glutGet(GLUT_WINDOW_HEIGHT) * 2 + 1;

        printf("X: %f\n", mappedX);
        printf("Y: %f\n", mappedY);

        pointX_1 = mappedX;
        pointY_1 = mappedY;

        firstPoint = !firstPoint;

        mouseClicked = 1;
        glutPostRedisplay();
    }
}

void keyboard(unsigned char key, int x, int y)
{
    // Verifica se a tecla pressionada é um número de 1 a 9
    if (key >= '1' && key <= '9')
    {
        currentColorIndex = key - '1'; // Alterna para a cor correspondente
        glutPostRedisplay();           // Redesenha a janela
    }
}

int main(int argc, char **argv)
{
    glutInit(&argc, argv);
    glutCreateWindow("Mouse Click Example");
    glutDisplayFunc(display);
    glutMouseFunc(mouse);
    glutKeyboardFunc(keyboard);
    glutMainLoop();
    return 0;
}
