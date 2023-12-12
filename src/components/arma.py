from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pyassimp

def load_fbx_model(file_path):
    scene = pyassimp.load(file_path)
    if not scene.meshes:
        raise Exception("O modelo não contém malhas.")
    return scene.meshes[0]

def render_fbx_model(model):
    glBegin(GL_TRIANGLES)
    for face in model.faces:
        for vertex_index in face.indices:
            vertex = model.vertices[vertex_index]
            glVertex3f(*vertex)
    glEnd()
