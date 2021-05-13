from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

axrng = 1.5


def init():
  glClear(GL_COLOR_BUFFER_BIT)
  #glClearColor(0.0, 0.0, 0.0, 1.0)
  glColor3ub(255, 255, 255)
  # Dimensions of the screen
  # Make axrng larger and see what happens!
  gluOrtho2D(-axrng, axrng, -axrng, axrng)

def polygon():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
   
    #Pentagon
    glVertex2f(0.0, -1.25)
    glVertex2f(-1.19, -0.39)
    glVertex2f(-0.73, 1.01)
    glVertex2f(0.73, 1.01)
    glVertex2f(1.19, -0.39)
   
    glEnd()
    glFlush()

    return
  
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
    glutInitWindowSize(400, 400)
    glutCreateWindow("Pentagon")
    glClearColor(0, 1.53, 1.53, 1)
    glutDisplayFunc(polygon)
    init()
    glutMainLoop()

main()



