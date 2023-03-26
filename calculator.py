'''Create Calculator Using Function in Python
Also add Name Initial In comment above the code'''


#T
def add(n_1,n_2):
    return n_1 + n_2

def Sub(a,b):           #Vaidik _ 
    return a - b

num_1=int(input("Enter No1:- "))
num_2=int(input("Enter No2:- "))

print("Please Chose +,-,*,/ below or E for exit")

operator=input()
match operator:
    case ("+"):
        result=add(num_1,num_2)
        print(result)
#Change The Case Below According To the Above Case
    case ("-"):
        result= Sub(num_1,num_2)
        print(result)
    case ("+"):
        result=add(num_1,num_2)
        print(result)
    case ("+"):
        result=add(num_1,num_2)
        print(result)
    


