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
    
    #Nonagon
    glVertex2f(0.0,-1.25)
    glVertex2f(-0.8,-0.96)
    glVertex2f(-1.23,-0.22)
    glVertex2f(-1.08,0.62)
    glVertex2f(-0.43,1.17)
    glVertex2f(0.43,1.17)
    glVertex2f(1.08,0.63)
    glVertex2f(1.23,-0.22)
    glVertex2f(0.8,-0.96)

    glEnd()
    glFlush()

    return
  
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
    glutInitWindowSize(400, 400)
    glutCreateWindow("Nonagon")
    glClearColor(0, 1.53, 1.53, 1)
    glutDisplayFunc(polygon)
    init()
    glutMainLoop()

main()



