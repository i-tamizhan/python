import matplotlib.pyplot as plt


profit_month = 0
profit = []
payable = []
payable_month = 0
net_profit = []
user_get = 0
user_profit = 0
invest = input("Enter the amount payable per month:")
count = invest / 20000
profit_payable =0
#_range = input("Enter the Range:")
for i in range(32):
	profit_month = 3000 * i * count
	profit.append(profit_month)
	
for i in range(17):
	payable_month = 1500 * i * count
	payable.append(payable_month)

for i in range(32):
	if (i < 17):
		net_profit.append(i * 1500 * count)	
	else :
		net_profit.append(i * 3000 * count)	 

self_profit = profit_month - profit_payable
user_profit = 1500 * count * 17
user_get = user_profit - invest

print "Total profit = {0}".format(profit_month)
print "Total paid = {0}".format(payable_month)
print "Net Profit = {0}".format(self_profit)
print "User Profit = {0}".format(user_profit)
print "User Gets = {0}  in 17 Months".format(user_get)
plt.plot(profit)
plt.plot(payable,'--')
plt.plot(net_profit,'.')
plt.ylabel('Rs.')
plt.xlabel('Months')
plt.grid('true')
plt.show()

