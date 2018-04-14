import matplotlib.pyplot as plt
amount = input("Enter the amount : ")
count = input("Enter the no. of people : ")
_range = input("Enter the range :")
interest = 0.025
array = []
revenue = []
profit = 0
i_amount = 0
for i in range(_range):
	i_amount = 30000  + i_amount + (i+1) * 0.025 * amount * 10
	array.append(i_amount)
	profit = profit + 2500 * (i+1)
	revenue.append(profit)
	print "amount for {0}	is 	{1} 	profit 	{2} ".format(i+1,array[i],revenue[i])

plt.plot(revenue)
plt.plot(array)
plt.ylabel('Rs.')
plt.xlabel('Months')
plt.show()




