name = "itai"
age = 21
height = 71. #inches
weight = 160. #pounds
eyes = "brown"
teeth = "white"
hair = "black"
pounds_to_kilo = .453
inches_to_centimeters = 2.54
print "Lets talk about %s" % name
print "He's %f meters tall" % (height*inches_to_centimeters/100.)
print "he's %d pounds and has %s eyes and %s hair" %(weight*pounds_to_kilo, eyes, hair)

print "If I add %d,%d,%d i get %d" %(age,height,weight,age+height+weight)
