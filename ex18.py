def print_all(*arg):
  n=0
  while n<len(arg):
	print "arg%d: %s"%(n+1,str(arg[n]))
	n+=1
print_all(1)