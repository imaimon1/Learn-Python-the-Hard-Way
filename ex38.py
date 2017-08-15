ten_things = "apples oranges crows telephone light sugar"
print "not ten things"

stuff = ten_things.split(' ')
more_stuff  = ["day", "night", "song","frisbee"]

while len(stuff) !=10:
	next_one=more_stuff.pop()
	print "adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." %len(stuff)
print "there we go: ", stuff

print "let's do some things with stuiff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])