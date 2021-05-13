from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
def init():
      #glClearColor(0.0, 0.5, 0.0, 0.1)
      glClearColor(1.0, 0.5, 0.0, 0.1)  #pleasing
      glClearColor(0.1, 0.2, 0.0, 1.0)
      
      gluOrtho2D(-10.0, 10.0, -10.0, 10.0)#question 5
def plotpoints():
      glClear(GL_COLOR_BUFFER_BIT)
      glColor3f(1.0, 1.0, 1.0)#glColor3f(1.0,0.0,0.0) # question 2
      #glPointSize(9.0)#question 3, question 6, 6.1
      
      #question 10#glLineWidth(3.0)#question 8
      
      glBegin(GL_LINES)#8.2     #glBegin(GL_LINE_STRIP)# QUESTION 7.2     #glBegin(GL_LINES)# QUESTION  7  #glBegin(GL_POINTS) # QUESTION 6
      #glVertex2f(0.0, 0.0)
      #glVertex2f(-0.8,0.8)#question 4                                #QUESTION 7
      #glVertex2f(-0.9,0.5)
      #glVertex2f(4.2,5.0)#question 4.2, 5.2

      
      
##      glVertex2f(0.0,0.0)
##      glVertex2f(3.0,0.0)
##      glVertex2f(3.0,0.0)
##      glVertex2f(3.0,4.0)                     #6.2
##      glVertex2f(3.0,4.0)
##      glVertex2f(0.0,4.0)
##      glVertex2f(0.0,4.0)
##      glVertex2f(.0,0.0)

##      glVertex2f(0.0,0.0)
##      glVertex2f(3.0,0.0)
##      glVertex2f(3.0,0.0)               #6.3
##      glVertex2f(1.5,1.5)
##      glVertex2f(1.5,1.5)
##      glVertex2f(0.0,0.0)
      
      
##      glVertex2f(2.5,0.0)
##      glVertex2f(-2.5,0.0)                          #question 9
##      glVertex2f(0.0,1.732050807)
      
      glVertex2f(0.0,10.0)
      glVertex2f(0.0,-10.0)                   #question 10
      glVertex2f(-10.0,0.0)
      glVertex2f(10.0,0.0)
      glEnd()
##      glPointSize(3.0)
##      glColor3f(1.0, 0.0, 0.0)
##      glBegin(GL_POINTS)
##      
##      glVertex2f(2.0,2.0)                           #question 12
##      glVertex2f(-2.0,2.0)
##
##      
##      glEnd()

      glColor3f(0.0, 0.0, 0.0)
      glBegin(GL_LINES)
      glVertex2f(10.0,10.0)
      glVertex2f(-10.0,-10.0)                 
     
      glEnd()

      glPointSize(3.0)
      glColor3f(1.0, 0.0, 0.0)
      glBegin(GL_POINTS)
      glVertex2f(5.0,3.0)
      glVertex2f(3.0,5.0)                 
     
      glEnd()
      
      glFlush()# memory to screen flush


def main():
      glutInit(sys.argv)#Intialize glut, listen command lne
      glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)#single mode for single layer
      glutInitWindowSize(500,500)#size 
      glutInitWindowPosition(50,50)#position
      glutCreateWindow("Coordinate system with Central Origin")
      glutDisplayFunc(plotpoints)#call
      #glutDisplayFunc(left)
      init()#to stay on the screen long
      glutMainLoop()
main()
