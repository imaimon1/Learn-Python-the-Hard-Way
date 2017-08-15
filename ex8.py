formater = "%r %r %r %r"

print formater % (1,2,3,4)
print formater % ('one', 'two', 'three',"four")
print formater % (True, False,True,False)
print formater % (formater, formater, formater, formater)
print formater % ("What", "who", "where", " Why")