from sys import argv

script, filename = argv

print "we are going to delete %s" %filename
print "use ctrl -c to stop this"
print "or return to continue"

raw_input("?")

print " opening the file"
target = open(filename, 'w')
print "truncating the file"
target.truncate()
print "now add three new lines"
line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")
print " I will write these"
target.write(line1+"\n" +line2+"\n"+line3)

print " and finally we close"
target.close()