X=int(input('Enter any number : '))
Y=int(input('Enter any number : '))
Z=int(input('Enter any number : '))
if(X>Y):
    if(Y>Z):
        print("X is a maximum number.")
    else:
        print("Z is a maximum number.")
if(Y>Z):
    print("Y is a maximum number.")
else:
   print("Zis a maximum number.")
