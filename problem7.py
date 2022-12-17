num = 1
counter = 0
flag = True
while flag:
    num+=1
    if all(num%i!=0 for i in range(2,int((num)**(1/2))+1)):
       counter += 1 
       
    if (counter == 10001):
        flag = False
    
print(num)