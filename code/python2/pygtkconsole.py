#!/usr/bin/env python
# -*- Mode: python; c-basic-offset: 4 -*-
#
# Interactive PyGtk Console, Johan Dahlin 2002
#

import os
import signal
import sys
import string
from code import InteractiveInterpreter, InteractiveConsole

import gtk
from gtk import TRUE, FALSE

# For compatibility, instead of using GDK.INPUT_READ or
# gtk.gdk.INPUT_READ depending on the PyGtk version
GDK_INPUT_READ = 1

class Mainloop(InteractiveInterpreter):
    def __init__(self, read_fd, pid):
        InteractiveInterpreter.__init__(self)
        self._rfd = os.fdopen(read_fd, 'r')
        self.pid = pid
        
        gtk.input_add(read_fd, GDK_INPUT_READ, self.input_func)

    def read_message(self):
        length = ord(self._rfd.read(1))
        return self._rfd.read(length)

    def input_func(self, fd, cond):
        data = self.read_message()
        more = self.runsource(data)
        if more:
            signal_id = signal.SIGUSR1
        else:
            signal_id = signal.SIGUSR2
            
        # Now when we're done, notify the console (parent process)
        os.kill(self.pid, signal_id)
        return TRUE

    def run(self):
        gtk.mainloop()
        
class Console(InteractiveConsole):
    def __init__(self, write_fd, pid):
        InteractiveConsole.__init__(self)
        self._wfd = os.fdopen(write_fd, 'w')
        self.pid = pid
        
        # Listen on SIGUSR1, SIGUSR2
        signal.signal(signal.SIGUSR1, self.signal_handler)
        signal.signal(signal.SIGUSR2, self.signal_handler)

    def signal_handler(self, sig_id, frame):
        # We receive different signals depend on if
        # we have more data in the buffer to interpret
        if sig_id == signal.SIGUSR1:
            self.more = 1
        elif sig_id == signal.SIGUSR2:
            self.more = 0
    
    def send_message(self, message):
        self._wfd.write('%c%s' % (len(message), message))
        self._wfd.flush()

    def interact(self, banner=None):
        InteractiveConsole.interact(self, banner)
        # Die parent die
        os.kill(self.pid, 9)
        
    def runsource(self, source, filename):
        self.send_message(source)
        # wait for notification from parent
        signal.pause()

        return self.more
        
class GtkInterpreter(Console):
    def __init__(self):
        rfd, wfd = os.pipe()

        parent_pid = os.getpid()
        child_pid = os.fork()
        if not child_pid:
            g = Mainloop(rfd, parent_pid)
            g.run()
        else:
            Console.__init__(self, wfd, child_pid)

def interact():
    try:
        import readline
        import rlcompleter
        readline.parse_and_bind('tab: complete')
    except ImportError:
        pass
    
    gi = GtkInterpreter()
    gi.push("from gtk import *")

    python_version = string.split(sys.version)[0]
    try:
	pygtk_version = string.join(map(str, gtk.pygtk_version), '.')
	gtk_version = string.join(map(str, gtk.gtk_version), '.')
    except:
	pygtk_version = '0.6.x'
	gtk_version = '1.2.x'

    banner = """Python %s, PyGTK %s (Gtk+ %s)
Interactive console to manipulate GTK+ widgets.""" % (python_version,
       pygtk_version,
       gtk_version)
    gi.interact(banner)
    
if __name__ == '__main__':
    interact()
