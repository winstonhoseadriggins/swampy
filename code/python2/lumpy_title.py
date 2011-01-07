#!/usr/bin/python

class TitleSlide:
    pass

import datetime
import Lumpy
lumpy = Lumpy.Lumpy()
lumpy.make_reference()
lumpy.restrict_class(TitleSlide, ['title', 'author', 'affiliation', 'date',
                                  'venue', 'email', 'lumpy_homepage'])
titleslide = TitleSlide()

titleslide.title = 'Lumpy', 'UML for Python'
titleslide.author = 'Allen B. Downey'
titleslide.affiliation = 'Olin College of Engineering'
titleslide.date = datetime.date(2006, 7, 13)
titleslide.venue = 'Boston Python Interest Group'
titleslide.email = 'downey@allendowney.com'
titleslide.lumpy_homepage = 'allendowney.com/lumpy'

lumpy.object_diagram()

