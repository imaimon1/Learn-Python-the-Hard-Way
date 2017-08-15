from sys import argv

script, username = argv
prompt = ">"

print "hello my name is %s and you are %s" %(script, username)
print "do you like me %s?" %(username)
like=raw_input(prompt)

print "are you real %s" %(username)
you_exist= raw_input(prompt)
print "am I real?"
me_exist = raw_input(prompt)

print """ you said the following about liking me: %s
and %s on you being real
and claim %s on me being real""" %(like, you_exist, me_exist)