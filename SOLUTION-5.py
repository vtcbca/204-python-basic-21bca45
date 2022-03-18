#WAS to enter any number and print from which number from 0 to 9 it is divisible.
a=int(input("Enter any number:"))
b=1
while(a<10):
    if(a%b==0):
        print("{} is divisible by {}".format(a,b))
    b=b+1
