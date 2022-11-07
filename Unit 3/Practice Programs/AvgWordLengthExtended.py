t,x,l,s,r,q=0,0,0,0,"","" 
while True:
    w=input("Enter word: ")
    if (w==""):
        break
    x+=1
    t+=len(w)
    m=len(w) 
    if (m<s):
        s=m
        q=w
    elif (m>l):
        l=m
        r=w
print("Average is {}, total characters {}, longest word {} and shortest word {}.".format(t/x,t,r,q)) 