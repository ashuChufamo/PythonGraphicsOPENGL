# -- eyu --
# triangletransformation
import math

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

axrng = 10


def init():
#   glClear(GL_COLOR_BUFFER_BIT)
  glClearColor(0.0, 0.0, 0.0, 1.0)
  glColor3ub(255, 255, 255)
  # Dimensions of the screen
  # Make axrng larger and see what happens!
  gluOrtho2D(-axrng, axrng, -axrng, axrng)


def pointTranslate(a,b,g,h):
      a=a+g
      b=b+h
      return a,b


def pointScaling(a,b,g,h):
      a=a*g
      b=b*h
      return a,b

def pointRotate(a,b,g):
      a=a*math.cos(math.pi/2)-b*math.sin(math.pi/2)
      b=a*math.sin(math.pi/2)+b*math.cos(math.pi/2)
      print(a,b)
      return a,b
      


def display():
  glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
  glColor3f(1.0, 1.0, 1.0)
  glPointSize(1.0)
    #drawing the coordinate system for visual refrence 
  glBegin(GL_LINES)
  glVertex2f(-10.0, 0.0)
  glVertex2f(10.0, 0.0)
  glVertex2f(0.0, 10.0)
  glVertex2f(0.0, -10.0)
  glEnd()

  glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
#   void glPolygonMode(	GLenum face,
#  	GLenum mode);
 
# Parameters
# face
# Specifies the polygons that mode applies to. Must be GL_FRONT_AND_BACK for front- and back-facing polygons.

# mode
# Specifies how polygons will be rasterized. Accepted values are GL_POINT, GL_LINE, and GL_FILL. The initial value is GL_FILL for both front- and back-facing polygons.

  glPushMatrix()
  #glTranslate(2,2,0) ##glTranslate(x,y,z)
  #glRotate(90,0,0,1) ##glRotate(rotateDegree,x,y,z)
  #glScale(2,2,0)  ##glScale(x,y,z)
  glBegin(GL_POLYGON)




##  f=pointTranslate(0,2,2,2)
##  g=f[0]
##  h=f[1]
##  f=pointTranslate(2,-2,2,2)                    #translate
##  a=f[0]
##  b=f[1]
##  f=pointTranslate(-2,-2,2,2)
##  c=f[0]
##  d=f[1]

##  f=pointScaling(0,2,2,2)
##  g=f[0]
##  h=f[1]
##  f=pointScaling(2,-2,2,2)
##  a=f[0]                                                    #scaling
##  b=f[1]
##  f=pointScaling(-2,-2,2,2)
##  c=f[0]
##  d=f[1]
  
  f=pointRotate(0,2,90)
  g=f[0]
  h=f[1]
  f=pointRotate(2,-2,90)              #rotation
  a=f[0]
  b=f[1]
  f=pointRotate(-2,-2,90)
  c=f[0]
  d=f[1]








  
##  

  
  glVertex2f(-2,0)
  glVertex2f(a,b)             ##only for rotation
  glVertex2f(2,-2)

##  glVertex2f(-2,0)
##  glVertex2f(a,b)             ##for translation and scaling
##  glVertex2f(2,-2)
  
  glEnd()
  glPopMatrix()
  
  glFlush()

  
  return

def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGB |GLUT_DEPTH)
  glutInitWindowSize(400, 400)
  glutCreateWindow("Triangle")
#   glClearColor(1.,0.,0.,1.) # background color
  glutDisplayFunc(display)
  init()
  glutMainLoop()
main()

