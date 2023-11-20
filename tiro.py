import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import time
import ctypes

window_width, window_height = 800, 600
targets = []
sphere_points = []
last_target_time = 0
score = 0

def create_sphere(radius, num_segments):
    for i in range(num_segments):
        theta1 = (i / num_segments) * math.pi
        theta2 = ((i + 1) / num_segments) * math.pi

        for j in range(num_segments * 2):
            phi1 = (j / (num_segments * 2)) * 2 * math.pi
            phi2 = ((j + 1) / (num_segments * 2)) * 2 * math.pi

            x1 = radius * math.sin(theta1) * math.cos(phi1)
            y1 = radius * math.sin(theta1) * math.sin(phi1)
            z1 = radius * math.cos(theta1)

            x2 = radius * math.sin(theta1) * math.cos(phi2)
            y2 = radius * math.sin(theta1) * math.sin(phi2)
            z2 = radius * math.cos(theta1)

            x3 = radius * math.sin(theta2) * math.cos(phi2)
            y3 = radius * math.sin(theta2) * math.sin(phi2)
            z3 = radius * math.cos(theta2)

            x4 = radius * math.sin(theta2) * math.cos(phi1)
            y4 = radius * math.sin(theta2) * math.sin(phi1)
            z4 = radius * math.cos(theta2)

            sphere_points.extend([x1, y1, z1, x2, y2, z2, x3, y3, z3, x1, y1, z1, x3, y3, z3, x4, y4, z4])

def draw_sphere(x, y, z):
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, sphere_points)
    glPushMatrix()
    glTranslatef(x, y, z)
    glDrawArrays(GL_TRIANGLES, 0, len(sphere_points) // 3)
    glPopMatrix()
    glDisableClientState(GL_VERTEX_ARRAY)

def generate_target():
    x = random.uniform(-3, 3)
    y = random.uniform(-3, 3)
    z = random.uniform(-3, 3)
    targets.append((x, y, z, time.time()))

def draw_targets():
    glColor3f(1.0, 0.0, 0.0)
    current_time = time.time()
    for target in targets:
        if current_time - target[3] < 3:  # Remove após 3 segundos
            draw_sphere(target[0], target[1], target[2])

def mouse_button_callback(window, button, action, mods):
    global score
    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.RELEASE:
        x, y = glfw.get_cursor_pos(window)
        y = window_height - y
        for target in targets:
            distance = math.sqrt((x - target[0])**2 + (y - target[1])**2 + (-5 - target[2])**2)
            if distance < 0.1:
                score += 1
                print('foi')
                targets.remove(target)
                break

def draw_score():
    glColor3f(1.0, 1.0, 1.0)
    glWindowPos2f(10, window_height - 30)
    score_text = f"Score: {score}"
    for char in score_text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ctypes.c_int(ord(char)))

def main():
    global last_target_time
    if not glfw.init():
        return

    window = glfw.create_window(window_width, window_height, "Aim Training 3D", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_mouse_button_callback(window, mouse_button_callback)

    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (window_width / window_height), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

    create_sphere(0.1, 20)  # Raio da esfera e número de segmentos
    last_target_time = time.time()

    glfw.swap_interval(1)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        current_time = time.time()
        if current_time - last_target_time > 1:  # Gera alvos a cada segundo
            generate_target()
            last_target_time = current_time

        draw_targets()
        draw_score()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()



if __name__ == "__main__":
    glutInit()
    main()
