share_msp = 0.20
share_joe = 0.20
share_su = 0.20
share_vk = 0.00

invest_msp = 0.00
invest_joe = 0.00
invest_su = 0.00
invest_vk = 0.00

profit = 0.00

invest_msp = input("Enter Msp Investment: ")
invest_msp = invest_msp * 1.00
invest_joe = input("Enter Joe Investment: ")
invest_joe = invest_joe * 1.00
invest_su = input("Enter Subash Investment: ")
invest_su = invest_su * 1.00
invest_vk = input("Enter Vivek Investment: ")
invest_vk = invest_vk * 1.00

total_invest = invest_msp + invest_joe + invest_su + invest_vk
total_invest = total_invest * 1.00
print "\nTotal Invest : {0}".format(total_invest)
print "\nInvestments:"
print "Msp : {0}\nJoe : {1}\nSub : {2}\nViv : {3}".format(invest_msp,invest_joe,invest_su,invest_vk)

share_msp = share_msp + ((invest_msp / total_invest) * 0.40)
share_joe = share_joe + ((invest_joe / total_invest) * 0.40)
share_su = share_su + ((invest_su / total_invest) *  0.40)
share_vk = share_vk + ((invest_vk / total_invest) * 0.40)


print "\nShare :"
print "Msp : {0} %\nJoe : {1} %\nSub : {2} %\nViv : {3} %".format(share_msp * 100 ,share_joe * 100,share_su * 100,share_vk * 100)

print "\nTotal Share #==> 100 == {0} <==#%".format(share_msp * 100 + share_joe * 100+ share_su * 100 + share_vk * 100)

profit = input("\nEnter the Profit : ")
profit = profit * 1.00

print "\nMsp : {0}\nJoe : {1}\nSub : {2}\nViv : {3}".format(share_msp * profit,share_joe * profit,share_su * profit,share_vk * profit)

print "\nProfit #==>{0} == {1}<==# total".format(profit,share_msp * profit + share_joe * profit + share_su * profit + share_vk * profit)

