n = int(input("Enter the range:"))
li=[]
for i in range (2, n+1):
    for j in range (1, i+1):
        
        rem = i % j
        if rem == 0:
            li.append(j)
               
    if len(li) == 2:
        print(i, end=" ")
    li.clear()