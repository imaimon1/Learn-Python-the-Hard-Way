people = 30
cars = 40 
buses = 15 

if cars > people:
	print "we should use cars"
elif cars < people:
	print "we should not take cars"

if buses > cars:
	print "too many buses"
elif buses< cars:
	print "too many cars"
else:
	print "we cant decide"

if people > buses:
	print "Alright, lets just take buses"
else:
	print "lets just stay home"