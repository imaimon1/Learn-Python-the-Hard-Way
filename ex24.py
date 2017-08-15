print "lets practice everything"
print "you\'d need to know\'bout escapes with \\ that do \n newlines and \t tabs"

poem = """ 
\tThis is a haiku\n it is not worth reading through 
it's last line has four too many syllables
"""
print "============="
print poem
print "============="

five = 10-2 +3-6
print "this should be five %d" % five

def secret_formula(started):
	jelly_beans = started*50
	jars = jelly_beans / 1000
	crates = jars/100
	return jelly_beans, jars, crates

start_point =10000
beans, jars, crates= secret_formula(start_point)
print "we can have %d beans if we start with %d" %(beans, start_point)
start_point/=10
beans, jars, crates= secret_formula(start_point)
print "we can have %d beans if we start with %d" %(beans, start_point)