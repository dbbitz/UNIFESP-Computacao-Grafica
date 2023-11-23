#include <glut.h>
#include <stdio.h>

float pointX_1 = 0.0;
float pointY_1 = 0.0;

float pointX_2 = 0.0;
float pointY_2 = 0.0;

float pointX_3 = 0.0;
float pointY_3 = 0.0;

int firstPoint = 1;
int secondPoint = 0;
int thirdPoint = 0;

int mouseClicked = 0;

int mode = 0;

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

void display()
{
    if (mode == 0)
    {
        glClearColor(0.4, 0.4, 0.4, 0.0);
        glClear(GL_COLOR_BUFFER_BIT);

        glPointSize(5.0); // Tamanho do ponto

        // Desenha o primeiro ponto
        glColor3fv(colors[currentColorIndex]);
        glBegin(GL_POINTS);
        glVertex2f(pointX_1, pointY_1);
        glEnd();

        // Desenha o segundo ponto
        glColor3fv(colors[currentColorIndex]);
        glBegin(GL_POINTS);
        glVertex2f(pointX_2, pointY_2);
        glEnd();

        // Desenha uma linha entre os dois pontos
        glColor3fv(colors[currentColorIndex]);
        glBegin(GL_LINES);
        glVertex2f(pointX_1, pointY_1);
        glVertex2f(pointX_2, pointY_2);
        glEnd();

        glFlush();
    }
    if (mode == 1)
    {
        glClearColor(0.2, 0.2, 0.2, 0.2);
        glClear(GL_COLOR_BUFFER_BIT);

        glPointSize(5.0); // Tamanho do ponto

        // Desenha o primeiro ponto
        glColor3f(1.0, 0.0, 0.0);
        glBegin(GL_POINTS);
        glVertex2f(pointX_1, pointY_1);
        glEnd();

        // Desenha o segundo ponto
        glColor3f(0.0, 1.0, 0.0);
        glBegin(GL_POINTS);
        glVertex2f(pointX_2, pointY_2);
        glEnd();

        // Desenha o terceiro ponto
        glColor3f(0.0, 0.0, 1.0);
        glBegin(GL_POINTS);
        glVertex2f(pointX_3, pointY_3);
        glEnd();

        // Desenha uma linha entre os dois pontos
        glColor3fv(colors[currentColorIndex]);
        glBegin(GL_LINES);
        glVertex2f(pointX_1, pointY_1);
        glVertex2f(pointX_2, pointY_2);
        glEnd();

        // Desenha uma linha entre os dois pontos
        glColor3fv(colors[currentColorIndex]);
        glBegin(GL_LINES);
        glVertex2f(pointX_2, pointY_2);
        glVertex2f(pointX_3, pointY_3);
        glEnd();

        // Desenha uma linha entre os dois pontos
        glColor3fv(colors[currentColorIndex]);
        glBegin(GL_LINES);
        glVertex2f(pointX_3, pointY_3);
        glVertex2f(pointX_1, pointY_1);
        glEnd();

        glFlush();
    }
}

void mouse(int button, int state, int x, int y)
{

    
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN && mode == 0)
    {
        // Mapeia as coordenadas do clique para as coordenadas OpenGL
        float mappedX = (float)x / glutGet(GLUT_WINDOW_WIDTH) * 2 - 1;
        float mappedY = -(float)y / glutGet(GLUT_WINDOW_HEIGHT) * 2 + 1;

        if (firstPoint)
        {
            pointX_1 = mappedX;
            pointY_1 = mappedY;
        }
        else
        {
            pointX_2 = mappedX;
            pointY_2 = mappedY;
        }

        firstPoint = !firstPoint;

        mouseClicked = 1;
        glutPostRedisplay();
    }
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN && mode == 1)
    {
        // Mapeia as coordenadas do clique para as coordenadas OpenGL
        float mappedX = (float)x / glutGet(GLUT_WINDOW_WIDTH) * 2 - 1;
        float mappedY = -(float)y / glutGet(GLUT_WINDOW_HEIGHT) * 2 + 1;

        

        if (firstPoint)
        {
            pointX_1 = mappedX;
            pointY_1 = mappedY;
            firstPoint = !firstPoint;
            secondPoint = !secondPoint;

            printf("firstPoint: %d\n", firstPoint);
            printf("secondPoint: %d\n", secondPoint);
            printf("thirdPoint: %d\n", thirdPoint);
        }
        else if (secondPoint)
        {
            pointX_2 = mappedX;
            pointY_2 = mappedY;
            secondPoint = !secondPoint;
            thirdPoint = !thirdPoint;

            printf("firstPoint: %d\n", firstPoint);
            printf("secondPoint: %d\n", secondPoint);
            printf("thirdPoint: %d\n", thirdPoint);
        }
        else if (thirdPoint)
        {
            pointX_3 = mappedX;
            pointY_3 = mappedY;
            thirdPoint = !thirdPoint;
            firstPoint = !firstPoint;

            printf("firstPoint: %d\n", firstPoint);
            printf("secondPoint: %d\n", secondPoint);
            printf("thirdPoint: %d\n", thirdPoint);
        }

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
    if (key == 'r' || key == 'R')
    {
        mode = 0;
    }
    if (key == 't' || key == 'T')
    {
        mode = 1;
        firstPoint = 1;
        secondPoint = 0;
        thirdPoint = 0;
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
