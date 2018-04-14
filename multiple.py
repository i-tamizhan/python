gpu_count = input("\nEnter the No of nvdia 1060's :")
gpu_cost = 26000
total_gpu_cost = gpu_count * gpu_cost

use_rate = input("Enter the Use Rate:")
use_rate = float(use_rate /100.0)


gpu_power = use_rate * 86.4 * gpu_count

board_cost = 11000
board_count = (gpu_count / 6) + 1
total_board_cost = board_count * board_cost

psu_cost = 5000
psu_count = (gpu_count / 3) + 1
total_psu_cost = psu_count * psu_cost

cpu_count = board_count
ram_count = board_count
hdd_count = board_count


eth = 3305.66 * use_rate
eth = eth - (0.03 * eth)
#eth_oc = eth_oc - (0.03 * eth_oc)
#eth_oc = 3824.02

zec = 3984.92 * use_rate
zec = zec - (0.03 * zec)
#zec_oc = 


total_revenue_eth = gpu_count * eth
total_revenue_zec = gpu_count * zec

riser_cost = gpu_count * 400

cpu_cost = 4000
ram_cost = 3000
hdd_cost = 1500

total_cpu_cost = cpu_count * cpu_cost
total_ram_cost = ram_count * ram_cost
total_hdd_cost = hdd_count * hdd_cost

total_power = gpu_power + board_count * 50 + 200

total_cost = total_gpu_cost + total_psu_cost + total_board_cost + total_ram_cost + total_cpu_cost + total_hdd_cost

print "\nNvdia 1060 count:",gpu_count
print "Power Used :",total_power

print "Use Rate:",use_rate
print "\nTotal cost : {0} + {1} unit power cost + Internet Cost".format(total_cost,total_power)
print "Total Ethereum Revenue Generated :",total_revenue_eth
print "Total Zcash Revenue Generated :",total_revenue_zec
print "\n"