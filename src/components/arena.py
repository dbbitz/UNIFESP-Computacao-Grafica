def draw_arena():
    glPushMatrix()
    glColor3f(1, 0, 0)
    glTranslatef(0, 0, 0)
    glScalef(2, 1, 2)
    glutSolidCube(2)
    glPopMatrix()