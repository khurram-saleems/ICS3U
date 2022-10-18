# 10 Practice Programs 2
# Program 8: Making Money
#
# Khurram Shaikh
# Friday, October 14, 2022
#
# Prog desc

balance,newBalance,interest=1000,0,0
for x in range(1,11):
    interest+=balance*0.06
    newBalance+=interest+balance
    print("Year {}, initial balance ${:.2f}, interest ${:.2f} and new total ${:.2f}.".format(x,newBalance,interest,newBalance))