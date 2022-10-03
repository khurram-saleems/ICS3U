mark=float(input("Enter mark: "))
mark_out_of=float(input("Enter what total mark is out of: "))
percentage=mark/mark_out_of*100
print("Your mark was {:.1%}!".format(percentage)) 