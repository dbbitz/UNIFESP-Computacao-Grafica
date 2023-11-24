#include <glut.h>
#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>

#define PI 3.141592654

typedef struct BMPImagem
{
    int width;
    int height;
    char *data;
} BMPImage;

/* Qtd máxima de texturas a serem usadas no programa */
#define MAX_NO_TEXTURES 6

/* vetor com os números das texturas */
GLuint texture_id[MAX_NO_TEXTURES];

char *filenameArray[MAX_NO_TEXTURES] = {
    "surface1.bmp",
    "surface1.bmp",
    "surface2.bmp",
    "surface3.bmp",
    "surface4.bmp",
    "surface5.bmp"};

GLUquadricObj *obj;

GLfloat angleX = 0.0f;
GLfloat angleY = 0.0f;

//-----------------------------------------------------------------------------
// Name: getBitmapImageData()
// Desc: Simply image loader for 24 bit BMP files.
//-----------------------------------------------------------------------------
void getBitmapImageData(char *pFileName, BMPImage *pImage)
{
    FILE *pFile = NULL;
    unsigned short nNumPlanes;
    unsigned short nNumBPP;
    int i;

    if ((pFile = fopen(pFileName, "rb")) == NULL)
        printf("ERROR: getBitmapImageData - %s not found.\n", pFileName);

    // Seek forward to width and height info
    fseek(pFile, 18, SEEK_CUR);

    if ((i = fread(&pImage->width, 4, 1, pFile)) != 1)
        printf("ERROR: getBitmapImageData - Couldn't read width from %s.\n ", pFileName);

    if ((i = fread(&pImage->height, 4, 1, pFile)) != 1)
        printf("ERROR: getBitmapImageData - Couldn't read height from %s.\n ", pFileName);

    if ((fread(&nNumPlanes, 2, 1, pFile)) != 1)
        printf("ERROR: getBitmapImageData - Couldn't read plane count from %s.\n", pFileName);

    if (nNumPlanes != 1)
        printf("ERROR: getBitmapImageData - Plane count from %s.\n ", pFileName);

    if ((i = fread(&nNumBPP, 2, 1, pFile)) != 1)
        printf("ERROR: getBitmapImageData - Couldn't read BPP from %s.\n ", pFileName);

    if (nNumBPP != 24)
        printf("ERROR: getBitmapImageData - BPP from %s.\n ", pFileName);

    // Seek forward to image data
    fseek(pFile, 24, SEEK_CUR);

    // Calculate the image's total size in bytes. Note how we multiply the
    // result of (width * height) by 3. This is becuase a 24 bit color BMP
    // file will give you 3 bytes per pixel.
    int nTotalImagesize = (pImage->width * pImage->height) * 3;

    pImage->data = (char *)malloc(nTotalImagesize);

    if ((i = fread(pImage->data, nTotalImagesize, 1, pFile)) != 1)
        printf("ERROR: getBitmapImageData - Couldn't read image data from %s.\n ", pFileName);

    //
    // Finally, rearrange BGR to RGB
    //

    char charTemp;
    for (i = 0; i < nTotalImagesize; i += 3)
    {
        charTemp = pImage->data[i];
        pImage->data[i] = pImage->data[i + 2];
        pImage->data[i + 2] = charTemp;
    }
}

/*Função para Carregar uma imagem .BMP */
void CarregaTexturas()
{
    BMPImage textura;

    /* Define quantas texturas serão usadas no programa  */
    glGenTextures(MAX_NO_TEXTURES, texture_id); /* 1 = uma textura; */
                                                /* texture_id = vetor que guardas os números das texturas */

    int i;
    for (i = 0; i < MAX_NO_TEXTURES; i++)
    {
        getBitmapImageData(filenameArray[i], &textura);
        glBindTexture(GL_TEXTURE_2D, texture_id[i]);
        glTexImage2D(GL_TEXTURE_2D, 0, 3, textura.width, textura.height, 0, GL_RGB, GL_UNSIGNED_BYTE, textura.data);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    }
}

/* **********************************************************************
  void initTexture(void)
        Define a textura a ser usada

 ********************************************************************** */
void initTexture(void)
{

    /* Habilita o uso de textura bidimensional  */
    glEnable(GL_TEXTURE_2D);
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE);

    /*Carrega os arquivos de textura */
    //  CarregaTextura("tunnelTexture.bmp");
    // CarregaTextura("tex2.bmp");
    CarregaTexturas();
}

void init(void)
{
    glEnable(GL_COLOR_MATERIAL);
    glClearColor(0.0f, 0.0f, 0.0f, 0.0f); // define a cor de fundo
    glEnable(GL_DEPTH_TEST);              // habilita o teste de profundidade

    // glShadeModel(GL_FLAT);
    glShadeModel(GL_SMOOTH);
    glEnable(GL_NORMALIZE);

    glMatrixMode(GL_MODELVIEW); // define que a matrix é a model view
    glLoadIdentity();           // carrega a matrix de identidade
    gluLookAt(4.0, 2.0, 1.0,    // posição da câmera
              0.0, 0.0, 0.0,    // para onde a câmera aponta
              0.0, 1.0, 0.0);   // vetor view-up

    glMatrixMode(GL_PROJECTION); // define que a matrix é a de projeção
    glLoadIdentity();            // carrega a matrix de identidade
    // glOrtho(-2.0, 2.0, -2.0, 2.0, 2.0, 8.0); //define uma projeção ortogonal
    gluPerspective(45.0, 1.0, 2.0, 8.0); // define uma projeção perspectiva
    // glFrustum(-2.0, 2.0, -2.0, 2.0, 2.0, 8.0); //define uma projeção perspectiva simétrica
    // glFrustum(-2.0, 1.0, -1.0, 2.0, 2.0, 8.0); //define uma projeção perspectiva obliqua
    glViewport(0, 0, 500, 500);

    // lightning();
}

void cubo(float size_X, float size_Y, float size_Z, float translate_X, float translate_Y, float translate_Z, int texture)
{

    glTranslatef(translate_X, translate_Y, translate_Z);

    GLfloat n[6][3] =
        {
            {-1.0, 0.0, 0.0},
            {0.0, 1.0, 0.0},
            {1.0, 0.0, 0.0},
            {0.0, -1.0, 0.0},
            {0.0, 0.0, 1.0},
            {0.0, 0.0, -1.0}};
    GLint faces[6][4] =
        {
            {0, 1, 2, 3},
            {3, 2, 6, 7},
            {7, 6, 5, 4},
            {4, 5, 1, 0},
            {5, 6, 2, 1},
            {7, 4, 0, 3}};
    GLfloat v[8][3];
    GLint i;
    // Cordenada em x
    v[0][0] = v[1][0] = v[2][0] = v[3][0] = -size_X / 2;
    v[4][0] = v[5][0] = v[6][0] = v[7][0] = size_X / 2;
    // Cordenada em y
    v[0][1] = v[1][1] = v[4][1] = v[5][1] = -size_Y / 2;
    v[2][1] = v[3][1] = v[6][1] = v[7][1] = size_Y;

    // Cordenada em z
    v[0][2] = v[3][2] = v[4][2] = v[7][2] = -size_Z / 2;
    v[1][2] = v[2][2] = v[5][2] = v[6][2] = size_Z / 2;

    for (i = 5; i >= 0; i--)
    {
        glBindTexture(GL_TEXTURE_2D, texture_id[texture]);
        glBegin(GL_QUADS);
        glNormal3fv(&n[i][0]);
        glTexCoord2f(0.0f, 0.0f);
        glVertex3fv(&v[faces[i][0]][0]);
        glTexCoord2f(1.0f, 0.0f);
        glVertex3fv(&v[faces[i][1]][0]);
        glTexCoord2f(1.0f, 1.0f);
        glVertex3fv(&v[faces[i][2]][0]);
        glTexCoord2f(0.0f, 1.0f);
        glVertex3fv(&v[faces[i][3]][0]);
        glEnd();
    }
}

void displayFunc()
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); // limpa o buffer

    glMatrixMode(GL_MODELVIEW); // define que a matrix é a de modelo

    glPushMatrix();
    glRotatef(angleX, 1.0, 0.0, 0.0);
    glRotatef(angleY, 0.0, 1.0, 0.0);
    cubo(1.0, 1.3, 1.0, 0.0, 0.0, 0.0, 2);
    
    cubo(0.5, 1.0, 1.0, 0.5, -1.3, 0.0, 1);

    cubo(0.5, 1.0, 1.0, -1.0, 0.0, 0.0, 1);

    cubo(0.5, 1.0, 0.5, 0.5, 2.2, 0.0, 3);

    
    cubo(0.5, 1.0, 0.3, 0.5, -0.7, 0.0, 3);

    cubo(0.5, 1.0, 0.3, -1.0, 0.0, 0.0, 3);
    glPopMatrix();

    glFlush(); // força o desenho das primitivas
}

void rotacoes(int key, int x, int y)
{
    switch (key)
    {
    case GLUT_KEY_UP:
        angleX += 15;
        break;
    case GLUT_KEY_DOWN:
        angleX -= 15;
        break;
    case GLUT_KEY_LEFT:
        angleY -= 15;
        break;
    case GLUT_KEY_RIGHT:
        angleY += 15;
        break;
    default:
        break;
    }
    glutPostRedisplay();
}

void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
    case '1':
        glBindTexture(GL_TEXTURE_2D, texture_id[0]);
        break;
    case '2':
        glBindTexture(GL_TEXTURE_2D, texture_id[1]);
        break;
    case '3':
        glBindTexture(GL_TEXTURE_2D, texture_id[2]);
        break;
    case '4':
        glBindTexture(GL_TEXTURE_2D, texture_id[3]);
        break;
    case '5':
        glBindTexture(GL_TEXTURE_2D, texture_id[4]);
        break;
    default:
        break;
    }
    glutPostRedisplay();
}

int main(int argc, char *argv[])
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowPosition(50, 50);
    glutInitWindowSize(500, 500);
    glutCreateWindow("Textura");
    glutDisplayFunc(displayFunc);
    glutSpecialFunc(rotacoes);
    glutKeyboardFunc(keyboard);
    init();
    initTexture();
    glutMainLoop();
    return 0;
}