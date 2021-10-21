sir="ABRACADABRA"
print(sir)
for i in range(0,len(sir)):
    x=ord(sir[i])
    y=ord(sir[i+1])
    if ((x!=77) and (y!=65)):
            ord(chr(sir[i]))=84
            ord(chr(sir[i+1]))=65
    print(sir[i],end=' ')
