from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys
def init():
       glClearColor(1.0, 1.0, 1.0, 1.0)
       gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
def plotfunc():
       glClear(GL_COLOR_BUFFER_BIT)
       glColor3f(0.0, 0.0, 0.0)
       glPointSize(3.0)
       #drawing the coordinate system for visual refrence
       glBegin(GL_LINES)
       glVertex2f(-5.0, 0.0)
       glVertex2f(5.0, 0.0)
       glVertex2f(0.0, 5.0)
       glVertex2f(0.0, -5.0)
       glEnd()
##       for x in arange(-5.0, 5.0, 0.1):
##             #y = x*x  # given
##             y=x**2-2 # # question 1
##             #y= x**3-3*x-1 #QUESTION 2
##             #y=x**4-5*x**3+x**2-3*x-1
##             #y=sqrt(r*r-x*x)
##             glBegin(GL_LINE_STRIP)
##             glVertex2f(x, y)
##             glEnd()
##             glFlush()

       r = 3.0
       for x in arange(-3.0, 3.0, 0.001):
             y = sqrt(r*r - x*x) 
             glBegin(GL_POINTS) 
             glVertex2f(x, y) 
             glVertex2f(-x, -y) 
             glEnd()
             glFlush()

##def plotfunc():
##       glClear(GL_COLOR_BUFFER_BIT)
##       glColor3f(0.0, 0.0, 0.0)
##       glPointSize(1.0)
##       for x in arange(-5.0, 5.0, 0.01):
##              y = x*x
##              glColor3f(0.0, 0.0, 0.0)
##              glBegin(GL_POINTS)
##              glVertex2f(x,y)
##              glEnd()
##              for a in arange(-5.0, 5.0, 0.01):
##                     if a < x*x:
##                            glColor3f(0.50,0.50,0.50)
##                            glBegin(GL_POINTS)
##                            glVertex2f(x,a)
##                            glEnd()
##       glColor3f(0.0, 0.0, 0.0)
##       glBegin(GL_LINES)
##       glVertex2f(-5.0, 0.0)
##       glVertex2f(5.0, 0.0)
##       glVertex2f(0.0, 5.0)
##       glVertex2f(0.0, -5.0)
##       glEnd()
##       glFlush()
##
def main():
       glutInit(sys.argv)
       glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
       glutInitWindowPosition(50,50)
       glutInitWindowSize(400,400)
       glutCreateWindow("Function Plotter")
       glutDisplayFunc(plotfunc)
       init()
       glutMainLoop()
main()
