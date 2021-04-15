import OpenGL.GLUT as GLUT
import OpenGL.GLU as GLU
import OpenGL.GL as GL
from sys import argv
from math import sin, cos, pi

window_name = "Paraboloide Revolucao"

left_button = False
alpha = 0
beta = 180.0
delta_alpha = 0.5

right_button = False
delta_x, delta_y, delta_z = 0, 0, 0

down_x, down_y = 0, 0


background_color = (0, 0, 0, 0)


m, n = 20, 20
raio = 2


def f(i,j):
    
    theta = ( (pi * i) / (m -1) ) - (pi / 2)
    phi = 2*pi*j/(n-1)
    
    x = raio * cos(theta) * cos(phi)
    y = raio * sin(theta)
    z = raio * cos(theta) * sin(phi)
    
    return x, y**2, z


def figure():
    GL.glPushMatrix()

    
    GL.glTranslatef(delta_x, delta_y + 1.5, delta_z)

    
    GL.glRotatef(alpha, 0.0, 1.0, 0.0)
    
    GL.glRotatef(beta, 0.0, 0.0, 1.0)


    for i in range(round(m/2)):
        GL.glBegin(GL.GL_QUAD_STRIP)
        for j in range(n):
            GL.glColor3fv(
                ((0.1*i/(m-1)),
                0,
                1 - (0.1*i/(m-1))))

            x, y, z = f(i,j)
            GL.glVertex3f(x,y,z)
            

            GL.glColor3fv(
                ((0.1*(i+1)/(m-1)),
                0,
                1 - (1.0*(i+1)/(m-1))))
            x, y, z = f(i+1, j)
            GL.glVertex3f(x,y,z)
        GL.glEnd()



    GL.glPopMatrix()


def draw():
    global alpha, left_button, right_button

    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

    figure()

    alpha = alpha + delta_alpha

    GLUT.glutSwapBuffers()


def timer(i):
    GLUT.glutPostRedisplay()
    GLUT.glutTimerFunc(10, timer, 1)


def special_key_pressed(key, x, y):
    """
    Template.
    Use for Up, Down, Left and Right arrows.
    """
    pass


def key_pressed(key, x, y):
    global delta_alpha

    if key == b"\033":
        GLUT.glutLeaveMainLoop()

    
    elif key == b" ":
        if delta_alpha == 0:
            delta_alpha = 0.5
        else:
            delta_alpha = 0


def mouse_click(button, state, x, y):
    global down_x, down_y, left_button, right_button, delta_z

    down_x, down_y = x, y

    left_button = button == GLUT.GLUT_LEFT_BUTTON and state == GLUT.GLUT_DOWN
    right_button = button == GLUT.GLUT_RIGHT_BUTTON and state == GLUT.GLUT_DOWN

   
    if button == 3 and state == GLUT.GLUT_DOWN:
        delta_z += 1
    elif button == 4 and state == GLUT.GLUT_DOWN:
        delta_z -= 1


def mouse_move(x, y):
    global alpha, beta, down_x, down_y, delta_x, delta_y, delta_alpha


    if left_button:
        delta_alpha = 0
  
        alpha += ((x - down_x) / 4.0) * -1

        if alpha >= 360:
            alpha -= 360

        if alpha <= 0:
            alpha += 360

        
        if alpha >= 180:
            beta -= (y - down_y) / 4.0 * -1
        else:
            beta += (y - down_y) / 4.0 * -1

        if beta >= 360:
            beta -= 360

        if beta <= 0:
            beta += 360

    # Translate
    if right_button:
        delta_x += -1 * (x - down_x) / 100.0
        delta_y += (y - down_y) / 100.0

    down_x, down_y = x, y

    GLUT.glutPostRedisplay()


def main():    
    GLUT.glutInit(argv)
    GLUT.glutInitDisplayMode(
        GLUT.GLUT_DOUBLE | GLUT.GLUT_RGBA | GLUT.GLUT_DEPTH | GLUT.GLUT_MULTISAMPLE
    )

    
    screen_width = GLUT.glutGet(GLUT.GLUT_SCREEN_WIDTH)
    screen_height = GLUT.glutGet(GLUT.GLUT_SCREEN_HEIGHT)

    window_width = round(2 * screen_width / 3)
    window_height = round(2 * screen_height / 3)

    GLUT.glutInitWindowSize(window_width, window_height)
    GLUT.glutInitWindowPosition(
        round((screen_width - window_width) / 2), round((screen_height - window_height) / 2)
    )
    GLUT.glutCreateWindow(window_name)

 
    GLUT.glutDisplayFunc(draw)

    
    GLUT.glutSpecialFunc(special_key_pressed)
    GLUT.glutKeyboardFunc(key_pressed)
    GLUT.glutMouseFunc(mouse_click)
    GLUT.glutMotionFunc(mouse_move)

    GL.glEnable(GL.GL_MULTISAMPLE)
    GL.glEnable(GL.GL_DEPTH_TEST)

    GL.glClearColor(*background_color)


    GLU.gluPerspective(-45, window_width / window_height, 0.1, 100.0)
    GL.glTranslatef(0.0, 0.0, -10)

    GLUT.glutTimerFunc(10, timer, 1)
    GLUT.glutMainLoop()


if(__name__ == '__main__'):
    main()