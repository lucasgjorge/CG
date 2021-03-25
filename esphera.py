from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *


n1 = 500
n2 = 500
raio = 2
a = 0


def mesh():
    glPushMatrix()
    glRotatef(a,1.0,0.0,0.0)
    glBegin(GL_POINTS)

    for i in range(0,n1):
        theta = (pi*i/(n1-1)) - (pi/2)
        for j in range(0,n2):
            phi = 2*pi*j/(n2-1)
            x = raio*cos(theta)*cos(phi)
            y = raio*sin(theta)
            z = raio*cos(theta)*cos(phi)
            glVertex3f(x,y,z)
    glEnd()
    glPopMatrix()

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    mesh()
    a+=1
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(1024,1024)
glutCreateWindow("esphera")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0,0,0,1)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10)
glutTimerFunc(10,timer,1)
glutMainLoop()