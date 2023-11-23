#include <glut.h>

float pointX_1 = 0.0;
float pointY_1 = 0.0;

float pointX_2 = 0.0;
float pointY_2 = 0.0;

int firstPoint = 1;

int mouseClicked = 0;

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
  
    glPointSize(5.0); // Tamanho do ponto

    // Desenha o primeiro ponto
    glColor3f(0.0, 0.0, 1.0);
    glBegin(GL_POINTS);
    glVertex2f(pointX_1, pointY_1);
    glEnd();

    // Desenha o segundo ponto
    glColor3f(0.0, 0.0, 1.0);
    glBegin(GL_POINTS);
    glVertex2f(pointX_2, pointY_2);
    glEnd();

    // Desenha uma linha entre os dois pontos
    glColor3f(0.0, 0.0, 1.0); // Cor preta para a linha
    glBegin(GL_LINES);
    glVertex2f(pointX_1, pointY_1);
    glVertex2f(pointX_2, pointY_2);
    glEnd();
    
    glFlush();
    
    glFlush();
}

void mouse(int button, int state, int x, int y) {
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN) {
        // Mapeia as coordenadas do clique para as coordenadas OpenGL
        float mappedX = (float)x / glutGet(GLUT_WINDOW_WIDTH) * 2 - 1;
        float mappedY = -(float)y / glutGet(GLUT_WINDOW_HEIGHT) * 2 + 1;

        if (firstPoint) {
            pointX_1 = mappedX;
            pointY_1 = mappedY;
        } else {
            pointX_2 = mappedX;
            pointY_2 = mappedY;
        }

        firstPoint = !firstPoint; 

        mouseClicked = 1;
        glutPostRedisplay();
    }
}


int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutCreateWindow("Mouse Click Example");
    glutDisplayFunc(display);
    glutMouseFunc(mouse); 
    glutMainLoop();
    return 0;
}
