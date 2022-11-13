text="Assignment 3-3 is due period 4 on 15/11/2022"

for i in range(len(text)):
    if text[i]>="0" and text[i]<='9':
        text=text[:i]+'*'+text[i+1:]
print(text)