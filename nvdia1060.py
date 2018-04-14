import matplotlib.pyplot as plt
cost = 28000
revenue_eth = []
revenue_zec = []
profit_eth = 0
profit_zec = 0
payback = []
for i in range(13):
	profit_eth = profit_eth + 2500
	print "profit_eth ",profit_eth
	revenue_eth.append(profit_eth)
print("")
for i in range(13):
	profit_zec = profit_zec + 3000
	print "profit_zec ",profit_zec
	revenue_zec.append(profit_zec)

for i in range(15):
	payback.append(28000)


plt.plot(revenue_eth)
plt.plot(revenue_zec,'--')
plt.plot(payback,':')
plt.ylabel('Rs.')
plt.xlabel('Months')
plt.show()
