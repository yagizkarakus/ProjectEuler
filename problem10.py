sum = 0
for num in range (2,(2*(10**6))):
    if all(num%i!=0 for i in range(2,int((num)**(1/2))+1)):
       sum += num
       
    
print(sum)