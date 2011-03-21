FILES = Wanderer.py Highway.py color_list.py imdb.py spiral.py \
lumpy_diag05.py color_space.py \
button_demo.py  draggable_demo.py   pack_demo.py \
canvas_demo.py  image_demo.py       pil_demo.py \
circle_demo.py  menubutton_demo.py  widget_demo.py \
remote_object.py	MathServer.py 	MathClient.py \
thread.py	Subject.py	Observer.py	Modifier.py \
Popup.py	PopupDemo.py	PopupServer.py	PopupClient.py

DOCS = remote_object.html

DEST = /home/downey/public_html/greent/thinkpython/code

code:
	rsync -a $(FILES) $(DEST)
	rsync -a $(DOCS) $(DEST)
	chmod -R o+r $(DEST)/*

docs:
	pydoc -w remote_object

