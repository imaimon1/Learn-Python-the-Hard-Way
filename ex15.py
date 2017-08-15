from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r" % filename
print txt.read()

file_again = raw_input("Type the file name again \n >")
txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()