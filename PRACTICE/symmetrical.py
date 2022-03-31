#Input any String  and Create New String From Middle Three Character
x=(input("Enter string:"))
l=len(x)
print("Symmetrical String" if x[0:l//2]==x[l//2:] else "Asymmetrical String") 

