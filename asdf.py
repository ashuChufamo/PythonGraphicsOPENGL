from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

axrng=0.5

def init():
      glClear(GL_COLOR_BUFFER_BIT)
      #glClearColor(0.0,0.0,0.0,1.0)
      glColor3ub(255,255,255)
      #Dimention of the screen
      #Make axrng larger and see wha happens!
      gluOrtho2D(-axrng,axrng,-axrng,axrng)

def display():
      glClear(GL_C0LOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
      glBegin(GL_POLYGON)
      glVertex2f(0.0,0.5)
      glVertex2f(0.5,-0.5)
      glVertex2f(-0.5,-0.5)
      glEnd()
      glFlush()

      return

def main():
      glutInit(sys.argv)
      glutInitDisplayMode(GLUT_RGB|GLUT_DEPTH)
      glutCreateWindow("Triangle")
      # glClearColor(1.,0.,0.,1.)#background color
      glutDisplayFunc(display)
      init()
      glutMainLoop()

main()












