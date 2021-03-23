from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

def f(x,y):
    return sqrt(abs(-x**2 - y**2 - 1.5**2))

M, N = 100, 100
x0, y0 = -2, -2
xf, yf = 2, 2
dx, dy = (xf - x0)/M, (yf - y0)/N
ax, ay, az = 0, 0, 0


def mesh():
    glPushMatrix()
    glTranslate(0.0,0.0,az)
    glRotatef(ax,1.0,0.0,0.0)
    glRotatef(ay,0.0,1.0,0.0)

    
    for i in range(0, N):
        y = y0 + i*dy      
        glColor3f(1-(i/N), 0, i/N)
        glBegin(GL_QUAD_STRIP)
        for j in range(0,M):
            x = x0 + j*dx
            glVertex3f(x, y, f(x,y))
            glVertex3f(x, y+dy, f(x, y+dy))
            
        glEnd()
    
    glPopMatrix()
