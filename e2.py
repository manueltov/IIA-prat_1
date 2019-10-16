##Fibonacci

x = 4000000 - 2
#x = 10 - 2
save = [1, 2]
while x>0 :
    c = save[0] + save[1]
    save[0] = save[1]
    save[1] = c
    save.append(c)
    x -= 1

sum = 0
num = 0
for idx in range(len(save)):
    num = save[idx]
    if num%2==0 :  #is even
        sum += num

#print(save)
print("SUM: ",sum)
#SUM:  42
