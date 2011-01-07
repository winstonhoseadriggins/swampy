#!/usr/bin/python

def animal() :
  # start with a singleton
  root = Tree("bird")

  # loop until the user quits
  while 1 :
    print
    if not yes("Are you thinking of an animal? ") : break

    # walk the tree
    tree = root
    while tree.getLeft() != None :
      prompt = tree.getCargo() + "? "
      if yes(prompt):
        tree = tree.getRight()
      else:
        tree = tree.getLeft()

    # make a guess
    guess = tree.getCargo()
    prompt = "Is it a " + guess + "? "
    if yes(prompt) :
      print "I rule!"
      continue

    # get new information
    prompt  = "What is the animal\'s name? "
    animal  = raw_input(prompt)
    prompt  = "What question would distinguish a %s from a %s? "
    question = raw_input(prompt % (animal,guess))

    # add new information to the tree
    tree.setCargo(question)
    prompt = "If the animal were %s the answer would be? "
    if yes(prompt % animal) :
      tree.setLeft(Tree(guess))
      tree.setRight(Tree(animal))
    else :
      tree.setLeft(Tree(animal))
      tree.setRight(Tree(guess))

def yes(ques) :
  from string import lower
  ans = lower(raw_input(ques))
  return (ans[0:1] == 'y')

animal




