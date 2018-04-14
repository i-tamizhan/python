import matplotlib.pyplot as plt
eth_price = input("Enter ETH price: ")
eth_reward = 3.25
#block_reward = eth_reward * eth_price
#print "debug:eth_price:{0} eth_reward:{1}".format(eth_price,eth_reward)
profit = []
day_profit = 0
g_hash_rate = input("Enter the Pool Hash rate in GH: ")
m_hash_rate = 1024 * g_hash_rate
rig_hash_rate = input("Enter the Rig hash rate in MH: ")
#print "debug:g_hash:{0} m_hash:{1} rig_hash:{2}".format(g_hash_rate,m_hash_rate,rig_hash_rate)
day_profit = (eth_reward / m_hash_rate) 
day_profit = day_profit * rig_hash_rate
print "\n[eth]:{0}\t[rs]:{1}\tday profit ".format(day_profit,day_profit * eth_price)
month_profit = day_profit * 30
print "[eth]:{0}\t[rs]:{1}\tmonth profit ".format(month_profit,month_profit * eth_price)

