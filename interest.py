amount = input("\nEnter the Amount :")
interest = 0.025 * amount * 12
payable_amount = amount + interest
print "\nAmount payable :",payable_amount
gpu_revenue = 3000 * 12
final_amount = gpu_revenue - payable_amount

if final_amount > 0:
	status = "PROFIT"
else:
	status = "LOSS"
print "\n{0} Rs.{1}".format(status,final_amount)
