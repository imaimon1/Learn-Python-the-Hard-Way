print " you enter a dark room with two doors. Doyou go through door one or door two?"
door = raw_input(">")

if door=="1":
	print "Giant bear eating cheesecake. what do you do?"
	print "1. take cake"
	print "2. scream at bear"
	
	bear = raw_input(">")
	
	if bear == "1":
		print "bear eats face. you die "
	elif bear == "2":
		print "bear eats leg. you die"
	else:
		print "well %s is better you live" % bear
elif door == "2":
	print " you stare into cthululu's abyss"
	print "1. blueberrys?"
	print "2. yellow rainjacket?"
	print "3. singing revolvers?"
	insanity = raw_input(">")
	if insanity == "1" or insanity == "2":
		print "you survive but your mind is cthulu's"
	else:
		print "insanity kills you cthulus is mildly annoyed you win"
else:
	print "you die"