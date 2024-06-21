z=int(input("Enter Queue Size :"))
queue = []
front=0
rear=-1
print("Queue :\n1. Enqueue \n2. Dequeue \n3. Front \n4. Rear \n5. IsEmpty \n6. IsFull \n7. Exit\n")
while True:
    a=int(input("Enter ur Choice : "))
    if(a==1) :
        if(z>rear+1):
            b=int(input("INPUT : "))
            queue.append(b)
            rear += 1
        else:
            print("Full")
    elif(a==2) :
        if(rear>-1):
            print(queue.pop(0))
            rear -= 1
        else:
            print("Empty")
    elif(a==3) :
        if(rear>-1):
            print(queue[front])
        else:
            print("Empty")
    elif(a==4) :
        if(rear>-1):
            print(queue[rear])
        else:
            print("Empty")
    elif(a==5) :
        if(rear>-1):
            print("Not Empty")
        else:
            print("Empty")
    elif(a==6) :
        if(z>rear+1):
            print("Not Full")
        else:
            print("Full")
    elif(a==7) :
        print("Exiting..... ")
        break
    else:
        print("Invalid Choice!")
