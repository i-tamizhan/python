import matplotlib.pyplot as plt
cost = 28000
revenue = []
profit = 0
payback = []
for i in range(13):
	profit = profit + 2500
	print "profit ",profit
	revenue.append(profit)
for i in range(15):
	payback.append(28000)


plt.plot(revenue)
plt.plot(payback)
plt.ylabel('Rs.')
plt.xlabel('Months')
plt.show()
