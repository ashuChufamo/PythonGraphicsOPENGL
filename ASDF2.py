''' Empty openGl window example'''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
glutInit("Hello,world")
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
glutInitWindowSize(400,400)
glutCreateWindow("Hello,world")
glClearColor(0.,0.,0.,1.)
glutMainLoop()
