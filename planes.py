#Assigning variables
tsph=[]
tspf=[]
fsph=[]
fspf=[]
hph=[]
hpf=[]
#Task 1: Work out maximum income
print('''Code for each type of plane:
      2-seater plane: 2sp
      4-seater plane: 4sp
      Historic plane: hp
      ''')
nof=int(input("Enter the number of flights you would like to inquire: "))
for i in range (0,nof):
    dur=int(input("Enter duration of flight, in mins: "))
    if dur == 30:
        print("Maximum number of flights in a day: 10")
        print("")
        pln=input("Enter type of plane: ")
        if pln == "2sp":
            print("Maximum income in a day: $1000")
        elif pln == "4sp":
            print("Maximum income in a day : $1200")
        elif pln== "hp":
            print("Maximum income in a day: $3000")
        print("")
    if dur == 60:
                print("Maximum number of flights in a day: 7")
                print("")
                pln=input("Enter type of plane: ")
                if pln == "2sp":
                    print("Maximum income in a day: $1050")
                elif pln == "4sp":
                    print("Maximum income in a day : $1400")
                elif pln== "hp":
                    print("Maximum income in a day: $3500")
                print("")
#Task 2: Record bookings
tsph=[8,9]
print(tsph)
        
