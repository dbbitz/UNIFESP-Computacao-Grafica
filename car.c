#include <glut.h>
#include <stdio.h>
#include <math.h>
#include <stdbool.h>

float pointX_1 = 0.0;
float pointY_1 = 0.0;

int firstPoint = 1;

GLfloat colors[][9] = {
    {1.0f, 0.0f, 0.0f}, // Vermelho 0
    {0.0f, 1.0f, 0.0f}, // Verde 1
    {0.0f, 0.0f, 1.0f}, // Azul 2
    {1.0f, 1.0f, 0.0f}, // Amarelo 3
    {1.0f, 0.0f, 1.0f}, // Magenta 4
    {0.0f, 1.0f, 1.0f}, // Ciano 5
    {1.0f, 1.0f, 1.0f}, // Branco 6
    {0.0f, 0.0f, 0.0f}, // Preto 7
    {0.5f, 0.5f, 0.5f}  // Cinza 8

};
int currentColorIndex = 0;

int mouseClicked = 0;

void circle(float x, float y, float r, int colorIndex, bool fill)
{

    glColor3fv(colors[colorIndex]);

    if (fill)
    {
        glBegin(GL_POINTS);

        for (float i = 0; i < 3.14; i += 0.01)
        {
            glBegin(GL_LINES);
            glVertex2f(x, y);
            glVertex2f((x + cos(i) * r), (y + sin(i) * r));
            glEnd();

            glBegin(GL_LINES);
            glVertex2f(x, y);
            glVertex2f((x + cos(i) * r), (y - sin(i) * r));
            glEnd();
        }

        glEnd();
    } else {
        glBegin(GL_POINTS);

        for (float i = 0; i < 3.14; i += 0.01)
        {
            glVertex2f((x + cos(i) * r), (y + sin(i) * r));
            glVertex2f((x + cos(i) * r), (y - sin(i) * r));
        }

        glEnd();
    }
}

void rectangle(float x, float y, float w, float h, int colorIndex)
{

    glColor3fv(colors[colorIndex]);

    glBegin(GL_POLYGON);

    glVertex2f(x, y);         // Vértice superior esquerdo
    glVertex2f(x + w, y);     // Vértice superior direito
    glVertex2f(x + w, y + h); // Vértice inferior direito
    glVertex2f(x, y + h);

    glEnd();
}

void display()
{
    glClear(GL_COLOR_BUFFER_BIT);

    circle(0.5,-0.2, 0.2, 6, true);
    circle(-0.5, -0.2, 0.2, 6, true);

    //Car

    glBegin(GL_POLYGON);
    glColor3f(colors[0][0], colors[0][1], colors[0][2]);
    glVertex2f(-0.5, -0.2);
    glVertex2f(-0.5, 0.2);
    glVertex2f(-0.25, 0.3);
    glVertex2f(0.25, 0.3);
    
    glVertex2f(0.5, 0.2);
    glVertex2f(0.5, -0.2);
    glEnd();

    glFlush();
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
    glutKeyboardFunc(keyboard);
    glutMainLoop();
    return 0;
}
