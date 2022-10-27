y,d,rte=0,1000,0.06
for x in range(10):
    y+=1
    interest=rte*d
    ib=d
    d+=interest
    print(y,"${:.2f} ${:.2f} ${:.2f}".format(interest,ib,d))