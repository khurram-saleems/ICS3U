file=input("Enter name of file: ")
if (file.endswith(".txt")==False):
    file+=".txt"
wishList=open(file,"w")
while True:
    wishListData=input("Enter data to write to the file ('STOP' to exit): ")
    if (wishListData=='STOP'):
        break
    print(wishListData,file=wishList)
wishList.close()

