#include <glut.h>

float pointX = 0.0;
float pointY = 0.0;
int mouseClicked = 0;



void display() {
    glClear(GL_COLOR_BUFFER_BIT);
  
    glColor3f(0.0, 0.0, 1.0); // Cor azul
    glPointSize(5.0); // Tamanho do ponto
    glBegin(GL_POINTS);
    glVertex2f(pointX, pointY);
    glEnd();
    glFlush();
}

void mouse(int button, int state, int x, int y) {
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN) {
        // Mapeia as coordenadas do clique para as coordenadas OpenGL
        pointX = (float)x / glutGet(GLUT_WINDOW_WIDTH) * 2 - 1;
        pointY = -(float)y / glutGet(GLUT_WINDOW_HEIGHT) * 2 + 1;
        
        mouseClicked = 1; // Indica que o botão do mouse foi clicado
        glutPostRedisplay(); // Redesenha a janela
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
