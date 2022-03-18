#WAS to print the sum of  1 t0 n number 
x=int(input("Enter Number:"))
y=1
sum=0
while(y<=x):
    sum=sum+y
    y=y+1
    print("The sum of {} to {} is {}".format(1,x,sum))
