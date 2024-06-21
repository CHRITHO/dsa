z=int(input("Enter Stack Size :"))
stack = []
print("Stack :\n1. Push \n2. Pop \n3. Peek \n4. IsEmpty \n5. IsFull \n6. Exit\n")
while True:
    a=int(input("Enter ur Choice : "))
    if(a==1) :
        if(z>len(stack)):
            b=int(input("INPUT : "))
            stack.append(b)
        else:
            print("Full")
    elif(a==2) :
        if(len(stack)>0):
            print(stack.pop())
        else:
            print("Empty")
    elif(a==3) :
        if(len(stack)>0):
            print(stack[len(stack)-1])
        else:
            print("Empty")
    elif(a==4) :
        if(len(stack)>0):
            print("Not Empty")
        else:
            print("Empty")
    elif(a==5) :
        if(z>len(stack)):
            print("Not Full")
        else:
            print("Full")
    elif(a==6) :
        print("Exiting..... ")
        break
    else:
        print("Invalid Choice!")
