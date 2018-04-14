gpu_count = input("Enter the No of nvdia 1060's :")
gpu_power = 86.4 * gpu_count
psu_cost = 3500

use_rate = input("Enter the Use Rate:")
use_rate = float(use_rate /100.0)

eth = 3305.66 * use_rate
eth = eth - 0.03 * eth

zec = 3984.92 * use_rate
zec = zec - 0.03 * zec

total_revenue_eth = gpu_count * eth
total_revenue_zec = gpu_count * zec

riser_cost = gpu_count * 400

total_power_used =250 + 33.12 + use_rate * gpu_power 
total_cost = psu_cost + riser_cost

print "\nNvdia 1060 count:",gpu_count
print "Power Used :",total_power_used
print "Use Rate:",use_rate
print "\nTotal cost : {0} + {1} unit power cost + Internet Cost".format(total_cost,total_power_used)
print "Total Ethereum Revenue Generated :",total_revenue_eth
print "Total Zcash Revenue Generated :",total_revenue_zec
print "\n"
print"Read how to create and secure a wallet\n"
