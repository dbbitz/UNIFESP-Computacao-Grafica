#include <glut.h>

float pointX = 0.0;
float pointY = 0.0;
int mouseClicked = 0;

GLfloat colors[][9] = {
    {1.0f, 0.0f, 0.0f}, // Vermelho
    {0.0f, 1.0f, 0.0f}, // Verde
    {0.0f, 0.0f, 1.0f},  // Azul
    {1.0f, 1.0f, 0.0f}, // Amarelo
    {1.0f, 0.0f, 1.0f}, // Magenta
    {0.0f, 1.0f, 1.0f}, // Ciano
    {1.0f, 1.0f, 1.0f}, // Branco
    {0.0f, 0.0f, 0.0f}, // Preto
    {0.5f, 0.5f, 0.5f} // Cinza

};
int currentColorIndex = 0;

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
  
    glColor3fv(colors[currentColorIndex]); // Cor azul
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

void keyboard(unsigned char key, int x, int y) {
    // Verifica se a tecla pressionada é um número de 1 a 9
    if (key >= '1' && key <= '9') {
        currentColorIndex = key - '1'; // Alterna para a cor correspondente
        glutPostRedisplay(); // Redesenha a janela
    }
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutCreateWindow("Mouse Click Example");
    glutDisplayFunc(display);
    glutMouseFunc(mouse); 
    glutKeyboardFunc(keyboard);
    glutMainLoop();
    return 0;
}
