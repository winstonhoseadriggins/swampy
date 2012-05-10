FILES = do_four.py 	grid.py 	polygon.py \
Wanderer.py Highway.py color_list.py    spiral.py \
lumpy_diag05.py color_space.py          koch.py  \
pi.py 	words.txt  birthday.py  wordlist.py reverse_pair.py  \
interlock.py  rotate.py  rotate_pairs.py  structshape.py \
anagram_sets.py  metathesis.py  reducible.py \
analyze_book.py analyze_book2.py analyze_book3.py markov.py \
cartalk1.py  cartalk2.py  cartalk3.py  \
button_demo.py  draggable_demo.py   pack_demo.py \
canvas_demo.py  image_demo.py       pil_demo.py \
circle_demo.py  menubutton_demo.py  widget_demo.py \
remote_object.py	MathServer.py 	MathClient.py \
thread.py	Subject.py	Observer.py	Modifier.py \
Popup.py	PopupDemo.py	PopupServer.py	PopupClient.py \
Threader.py	Threader_soln.py	Card.py	PokerHand.py \
Shape.py	Poker.py	PokerExam.py \
flower.py	letters.py	typewriter.py   pie.py \
Time1.py	Time1_soln.py \
Point1.py	Point1_soln.py


DOCS = remote_object.html

DEST = /home/downey/public_html/greent/thinkpython/code

code:
	rsync -a $(FILES) $(DEST)
	rsync -a $(DOCS) $(DEST)
	chmod -R o+r $(DEST)/*

docs:
	pydoc -w remote_object

