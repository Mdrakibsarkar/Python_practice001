#1+1/2+1/3+1/4+.....+1/n:
n=int(input("Enter last term:"))
sum=0
for x in range(1,n+1,1):
    sum=sum+1/x
print(sum)