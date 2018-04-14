import matplotlib.pyplot as plt
nvdia_count = input("\nEnter the No of nvdia 1060's :")
nvdia_cost = 26000
total_nvdia_cost = nvdia_count * nvdia_cost

use_rate = input("Enter the Use Rate:")
use_rate = float(use_rate /100.0)

################################################################################
#	Range CALCULATION (TOTAL NO OF VALUES TO BE PLOTTED IN GRAPH)
#_range = input("Enter the Range :")
_range = 20
_range = _range + 1
if _range % 2 == 0:
	_range = _range + 1

################################################################################
nvdia_power = use_rate * 86.4 * nvdia_count
board_cost = 19500

################################################################################
# if either amd or nvdia goes beyond 8 board count increases
board_count = (nvdia_count / 16) + 1
#board_count = (nvdia_count / 19) + 1 if driver supports
total_board_cost = board_count * board_cost

################################################################################
# if either amd or nvdia  power goes beyond the power of psu psu cost increases
psu_cost = 5000
psu_count = (nvdia_count / 3) + 1
total_psu_cost = psu_count * psu_cost

cpu_count = board_count
ram_count = board_count
hdd_count = board_count

eth = 3305.66 * use_rate
eth = eth - 0.03 * eth

zec = 3984.92 * use_rate
zec = zec - 0.03 * zec

total_revenue_eth = nvdia_count * eth
total_revenue_zec = nvdia_count * zec

riser_cost = nvdia_count * 400

cpu_cost = 4000
ram_cost = 3000
hdd_cost = 1500

total_cpu_cost = cpu_count * cpu_cost
total_ram_cost = ram_count * ram_cost
total_hdd_cost = hdd_count * hdd_cost

total_power = nvdia_power + board_count * 50 + 200

total_cost = total_nvdia_cost + total_psu_cost
+ total_board_cost + total_ram_cost + total_cpu_cost + total_hdd_cost

###############################################################################################
#	POWER CALCULATION
#units = input("\nEnter the No. of units consumed:")
units = total_power
amount = 0
temp = 0

if units > 100 and units <= 200:
	temp = units - 100
	amount = temp * 1.5
	amount = amount + 20

if units > 200 and units <= 500:
	temp = units - 100
	amount = 100 * 2
	temp = temp - 100
	amount = amount + temp * 3
	amount = amount + 30

if units > 500:
	temp = units - 100
	amount = 100 * 3.5
	temp = temp - 300
	amount = amount + 300 * 4.6
	temp = temp - 100
	amount = amount + temp * 6.6
	amount = amount + 50
#print "\nNo of Units Consumed :",units
#print "\nPower Cost :",amount

###############################################################################################
#OUTPUT SCREEN
print "\nNvdia 1060 count:",nvdia_count
print "Power Used :",total_power
print "Power Cost :",amount
print "Use Rate:",use_rate
print "\nTotal cost : {0} + {1} unit power cost + Internet Cost".format(total_cost,total_power)
print "Total cost : {0} + {1}  + Internet Cost".format(total_cost,amount)
total_cost = total_cost + amount
print "Total cost : {0} + Internet Cost".format(total_cost)
print "\nTotal Ethereum Revenue Generated : {0} / month".format(total_revenue_eth)
print "Total Zcash  Revenue  Generated  : {0} / month".format(total_revenue_zec)
print "\n"

##############################################################################################
#PAYBACK
payback_eth = int(total_cost) / int(total_revenue_eth)
payback_zec = int(total_cost) / int(total_revenue_zec)
payback_eth = payback_eth + 1
payback_zec = payback_zec + 1
print "Ethereum Payback : {0} months".format(payback_eth)
print "Zcash Payback : {0} months".format(payback_zec)
print "\n"

##############################################################################################
#PLOTTING
arr_total_cost = []
arr_eth_revenue = []
arr_zec_revenue = []
for i in range(_range):
	arr_total_cost.append(total_cost)
	arr_eth_revenue.append(total_revenue_eth * i+1)
	arr_zec_revenue.append(total_revenue_zec * i+1)

plt.plot(arr_total_cost)
plt.plot(arr_eth_revenue)
plt.plot(arr_zec_revenue)
plt.show()
