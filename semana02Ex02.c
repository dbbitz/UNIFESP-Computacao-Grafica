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

int mouseClicked = 0;

void display()
{
    glClear(GL_COLOR_BUFFER_BIT);

    glPointSize(5.0); // Tamanho do ponto

    // Desenha o primeiro ponto
    glColor3fv(colors[currentColorIndex]);
    glBegin(GL_POINTS);
    glVertex2f(pointX_1, pointY_1);
    glEnd();

    // Desenha uma linha entre os dois pontos usando o algoritmo de breshem

    float dx = pointX_2 - pointX_1;
    float dy = pointY_2 - pointY_1;

    float m = dy / dx;

    float x = pointX_1;
    float y = pointY_1;

    float b = y - m * x;

    glColor3fv(colors[currentColorIndex]);
    glBegin(GL_POINTS);

    if (dx > dy)
    {
        while (x <= pointX_2)
        {
            glVertex2f(x, y);
            x += 0.01;
            y = m * x + b;
        }
    }
    else
    {
        while (y <= pointY_2)
        {
            glVertex2f(x, y);
            y += 0.01;
            x = (y - b) / m;
        }
    }

    glEnd();

    // Desenha o segundo ponto
    glColor3fv(colors[currentColorIndex]);
    glBegin(GL_POINTS);
    glVertex2f(pointX_2, pointY_2);
    glEnd();

    // Desenha uma linha entre os dois pontos usando o algoritmo de breshem
    float dx_1 = pointX_3 - pointX_1;
    float dy_1 = pointY_3 - pointY_1;

    float m_1 = dy_1 / dx_1;

    float x_1 = pointX_1;
    float y_1 = pointY_1;

    float b_1 = y_1 - m_1 * x_1;

    glColor3fv(colors[currentColorIndex]);
    glBegin(GL_POINTS);

    if (dx_1 > dy_1)
    {
        while (x_1 <= pointX_3)
        {
            glVertex2f(x_1, y_1);
            x_1 += 0.01;
            y_1 = m_1 * x_1 + b_1;
        }
    }
    else
    {
        while (y_1 <= pointY_3)
        {
            glVertex2f(x_1, y_1);
            y_1 += 0.01;
            x_1 = (y_1 - b_1) / m_1;
        }
    }

    glEnd();

    // Desenha o terceiro ponto
    glColor3fv(colors[currentColorIndex]);
    glBegin(GL_POINTS);
    glVertex2f(pointX_3, pointY_3);
    glEnd();

    // Desenha uma linha entre os dois pontos usando o algoritmo de breshem

    float dx_2 = pointX_3 - pointX_2;
    float dy_2 = pointY_3 - pointY_2;

    float m_2 = dy_2 / dx_2;

    float x_2 = pointX_2;
    float y_2 = pointY_2;

    float b_2 = y_2 - m_2 * x_2;

    glColor3fv(colors[currentColorIndex]);
    glBegin(GL_POINTS);

    if (dx_2 > dy_2)
    {
        while (x_2 <= pointX_3)
        {
            glVertex2f(x_2, y_2);
            x_2 += 0.01;
            y_2 = m_2 * x_2 + b_2;
        }
    }
    else
    {
        while (y_2 <= pointY_3)
        {
            glVertex2f(x_2, y_2);
            y_2 += 0.01;
            x_2 = (y_2 - b_2) / m_2;
        }
    }

    glEnd();

    glFlush();
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
            printf("Point 1: (%f, %f)\n", pointX_1, pointY_1);
        }
        else
        {
            pointX_2 = mappedX;
            pointY_2 = mappedY;
            printf("Point 2: (%f, %f)\n", pointX_2, pointY_2);
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
            printf("Point 1: (%f, %f)\n", pointX_1, pointY_1);
        }
        else if (secondPoint)
        {
            pointX_2 = mappedX;
            pointY_2 = mappedY;
            secondPoint = !secondPoint;
            thirdPoint = !thirdPoint;
            printf("Point 2: (%f, %f)\n", pointX_2, pointY_2);
        }
        else if (thirdPoint)
        {
            pointX_3 = mappedX;
            pointY_3 = mappedY;

            thirdPoint = !thirdPoint;
            firstPoint = !firstPoint;
            printf("Point 3: (%f, %f)\n", pointX_3, pointY_3);
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
        pointX_1 = 0.0;
        pointY_1 = 0.0;
        pointX_2 = 0.0;
        pointY_2 = 0.0;
        pointX_3 = 0.0;
        pointY_3 = 0.0;
        thirdPoint = 0;
        firstPoint = 1;
        mode = 0;
        glutPostRedisplay();
    }
    if (key == 't' || key == 'T')
    {
        firstPoint = 1;
        mode = 1;
        glutPostRedisplay();
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
