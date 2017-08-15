from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" %(from_file, to_file)

in_file = open(from_file).read()

print "the input file is %d bytes long" % len(in_file)

print "does the output file exist? %r" % exists(to_file)
raw_input("hit return to continue or CTR-C to exist")
open(to_file,'w').write(in_file)
print "done"
#out_file.close()