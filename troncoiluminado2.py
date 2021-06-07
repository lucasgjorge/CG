from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import math 
import sys
import random


dist = 2

num_lados = 6


def draw_pyramid():
	altura = 4
	raio_lado = (2*math.pi)/num_lados
	raio_baixo = 2
	raio_alto = 1
	vertice_baixo = []
	vertice_alto = []

	glPushMatrix()
	glRotatef(-110,1.0,0.0,0.0)
	

	# Creating and drawing down vertices
	glBegin(GL_POLYGON)
	for i in range(0,num_lados):
		x = raio_baixo * math.cos(i*raio_lado) - dist
		y = raio_baixo * math.sin(i*raio_lado) - dist
		vertice_baixo += [ (x,y) ]
		glVertex3f(x,y,0.0)
	glEnd()

	# Creating and drawing up vertices
	glBegin(GL_POLYGON)
	for i in range(0,num_lados):
		x = raio_alto * math.cos(i*raio_lado) - dist
		y = raio_alto * math.sin(i*raio_lado) - dist
		vertice_alto += [ (x,y) ]
		
		glVertex3f(x,y,altura)
	glEnd()


	#Drawing side faces
	glBegin(GL_QUADS)
	for i in range(0,num_lados):
		glNormal3fv(calculaNormal( (vertice_baixo[i][0],vertice_baixo[i][1],0.0), (-dist,-dist,altura), (vertice_baixo[(i+1)%num_lados][0],vertice_baixo[(i+1)%num_lados][1],0.0)))
		glVertex3f(vertice_baixo[i][0],vertice_baixo[i][1],0.0)
		glVertex3f(vertice_alto[i][0],vertice_alto[i][1],altura)
		glVertex3f(vertice_alto[(i+1)%num_lados][0],vertice_alto[(i+1)%num_lados][1],altura)
		glVertex3f(vertice_baixo[(i+1)%num_lados][0],vertice_baixo[(i+1)%num_lados][1],0.0)
	glEnd()

	glPopMatrix()

def calculaNormal(a1, a2, a3):
    x = 0
    y = 1
    z = 2
    v0 = a1
    v1 = a2
    v2 = a3
    U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    draw_pyramid()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt( 10,0,0, 0,0,0,     0,1,0 )

def init():
    mat_ambient = (0, 1, 0.5, 1.0)
    mat_diffuse = (1.0, 1.0, 0.5, 1.0)
    mat_specular = (1.0, 0.5, 0.5, 1.0)
    mat_shininess = (50,)
    light_position = (5.0, 5.0, 5.0, 0.0)
    glClearColor(0.0,0.0,0.0,0.0)
    glShadeModel(GL_FLAT)
    #glShadeModel(GL_SMOOTH)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Tronco iluminado")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()