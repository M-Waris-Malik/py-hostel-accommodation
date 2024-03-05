hostel=[]

def reserveRoom():
    room=1
    option=""
    while room <=2:
        if option =="x" :
            break
        else:
            for i in range(1,3):
                stdRollNo=input("Enter RollNo of Student: ")
                stdName = input("Enter Name of Student: ")
                record={"RollNo":stdRollNo, "Name":stdName}
                hostel.append(record)
                print("Bed No: ",i," in Room No: ",room," reserved for student: ",stdRollNo)
                print("--------------------------------")
                print("Enter 'a' for add")
                print("Enter 'x' for exit")
                option=input("Enter option: ")
                
                if option=="a":
                    continue
                elif option=="x":
                    print("Best of luck!")
                    break
            room=room+1
        
    if room >2:
        print()
        print("Bed Not Available!")
        print()
                    
                   
def display():
    for i in hostel:
        print()
        print("RollNo of student: ",i["RollNo"]) 
        print("Name of Student: ",i["Name"])
        
             

while True:
    print("1.Reserve Room")
    print("2.Display inform of all students")
    print("0.Close")
    choice=int(input("Enter Choice: "))
    print()
    
    if choice==1:
        print()
        reserveRoom()
        print()
        
    elif choice==2:
        print()
        display()
        print()
        
    elif choice==0:
        print()
        print("Good bye!")
        print()
        break
        
    else:
        print()
        print("invalid input!")
        print()