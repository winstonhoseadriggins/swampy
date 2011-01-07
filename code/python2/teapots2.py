# teapots.py
# by Allen Downey

# The following program demonstrates features from the
# first few chapters of the Red Book.  I have lifted
# lines from lots of different examples, with the intention
# of getting it all in one place.

# The documentation for PyOpenGL, GLU and GLUT is at:

#http://pyopengl.sourceforge.net/documentation/manual/reference-GL.xml
#http://pyopengl.sourceforge.net/documentation/manual/reference-GLU.xml
#http://pyopengl.sourceforge.net/documentation/manual/reference-GLUT.xml

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from time import sleep

class Teapot:
    def __init__(self, world, size=1, orbit=5, orbit_angle=0, rot_angle=0,
                 rev_speed=1, rot_speed=2):
        self.size = size
        self.orbit = orbit
        self.orbit_angle = orbit_angle
        self.rot_angle = rot_angle
        self.rev_speed = rev_speed
        self.rot_speed = rot_speed
        self.rotation = 0
        self.revolution = 0
        world.register(self)

    def step(self):
        self.rotation = (self.rotation + self.rot_speed) % 360
        self.revolution = (self.revolution + self.rot_speed) % 360

    def display(self):

        glPushMatrix()

        z_axis = (0, 0, 1)
        rev_axis=(0, 1, 0)
        rot_axis=(0, 1, 0)
        
        glRotatef(self.orbit_angle, *z_axis)
        glRotatef(self.revolution, *rev_axis)
        glTranslatef(self.orbit, 0, 0)
        glRotatef(self.rot_angle, *z_axis)
        glRotatef(self.rotation, *rot_axis)

        glutSolidTeapot(self.size)

        glPopMatrix()


class World:
    def __init__(self, args, size=500):
        self.args = args
        self.size = size
        self.objects = []
        self.camera = Camera()
        self.set_up_gl()
        self.lights()

    def register(self, object):
        self.objects.append(object)

    def set_up_gl(self):
        # process command-line arguments
        glutInit(self.args)

        # turn on double-buffering
        # and rgb color with alpha channel
        glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGBA)

        # create the window
        glutInitWindowSize (self.size, self.size)
        glutInitWindowPosition (100, 100)
        glutCreateWindow (self.args[0])

        # clear the background
        glClearColor (1, 1, 1, 0)

        glShadeModel (GL_SMOOTH)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)

        # set up the callbacks
        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        glutKeyboardFunc(self.keyboard)
        glutMouseFunc(self.mouse)
        glutIdleFunc(self.idle)


    def lights(self):
        # put a red light on the camera
        position = self.camera.position + (0,)
        color = (1, 0, 0, 0)
        set_up_light(GL_LIGHT0, position, color)

        # put a blue light on the right
        position = (10, 0, 0, 0)
        color = (0, 0, 1, 0)
        set_up_light(GL_LIGHT1, position, color)

        # put a green light at high noon
        position = (0, 10, 0, 0)
        color = (0, 1, 0, 0)
        set_up_light(GL_LIGHT2, position, color)


    def display(self):
        # display runs whenever we have to redraw the screen

        # clear out the colors and the buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # tell GL which matrix we want to work with, and
        # set it to the identity
        glMatrixMode(GL_MODELVIEW)

        # draw a sphere at the current location, size 2
        # use 32 lines of latitude and longitude
        glutSolidSphere(2, 32, 32)

        for object in self.objects:
            object.display()

        # reveal the finished picture
        glutSwapBuffers()


    def reshape (self, w, h):
        # reshape gets invoked when the window is resized

        # change the size of the viewport
        glViewport (0, 0, w, h)
        
        # change the way the scene is projected into
        # the viewport
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        (fovy, aspect, near, far) = (60, 1, 2, 20)
        gluPerspective(fovy, aspect, near, far)

        self.camera.point()


    def keyboard(self, key, x, y):
        # keyboard in invoked when the user presses a key
        
        # quit if the user presses Control-C
        if key == chr(3):
            sys.exit(0)


    def mouse(self, button, state, x, y):
        # mouse is invoked when the user clicks the mouse
        if button == GLUT_LEFT_BUTTON:
            if state == GLUT_DOWN:
                sys.exit()
    
    def idle(self):
        for object in self.objects:
            object.step()

        # mark the scene for redisplay during the next iteration
        # of mainLoop
        glutPostRedisplay()
        sleep(0.005)

    def mainloop(self):
        glutMainLoop()


class Camera:
    def __init__(self, position=(0, 0, 10), target=(0, 0, 0), up=(0, 1, 0)):
        self.position = position
        self.target = target
        self.up = up
        
    def point(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(*self.position + self.target + self.up)


def set_up_light(name, position=(0, 0, 1, 0), color=(1, 1, 1, 1)):

    # tell GL which matrix we want, and save the current state
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    # color is in RGBA format
    light_ambient =  color
    light_diffuse =  color
    light_specular = color

    # position is in x, y, z, w format
    # if w is 0 then the light is "directional"
    # otherwise it is "positional"
    # directional is like the sun, very far away
    # positional behaves like a lamp in the scene
    light_position = position

    # turn on the lights
    # read the documentation for an explanation of the
    # different kinds of light
    glLightfv(name, GL_AMBIENT, light_ambient)
    glLightfv(name, GL_DIFFUSE, light_diffuse)
    glLightfv(name, GL_SPECULAR, light_specular)
    glLightfv(name, GL_POSITION, light_position)
    glEnable(name)

    # restore the matrix before we go
    glPopMatrix()


def main(*args):
    world = World(args)
    teapot = Teapot(world, orbit = 7.2, rot_angle = 20)
    teapot = Teapot(world, orbit = 7.2, orbit_angle = 20)
    world.mainloop()

if __name__ == "__main__":
    main(*sys.argv)
    
