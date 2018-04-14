amount = input("Enter the Amount:")
rate = 4
count = amount / 20000
div = count * 1500
_range = (amount /div) + 1
cost = 0
print "div{0}",format(div)
for i in (_range):
	cost = amount * rate
	amount = amount - ( count * 1500)

print "Total Cost :{0}".format(cost)
