#Q1 sample lists

mainlist=[]

altitude=[100,120,115,130,125]
voltage=[12.2,12.5,12.7,11.5,12.3]
temperature=[28.0,29.0,28.5,29.5,30.5]

print("\n")

def maxval(l):
    result=max(l)
    return result


def minval(l):
    result=min(l)
    return result


def avgval(l):
    result = sum(l)/len(l)
    return result

def numberofelements(l):
    result=len(l)
    return result


print("\n")



print("Enter the list you want to analyze: \n1. Altitude \n2. Voltage \n3. Temperature")
choice=int(input("Enter your choice: "))




if choice==1:
    print("You have selected Altitude list \n")
    print(altitude)
    print("The maximum value is: ",maxval(altitude))
    print("The minimum value is: ",minval(altitude))
    print("The average value is: ",avgval(altitude))
    print("The number of elements is: ",numberofelements(altitude))




elif choice==2:
    print("You have selected Voltage list \n")
    print(voltage)
    print("The maximum value is: ",maxval(voltage))
    print("The minimum value is: ",minval(voltage))
    print("The average value is: ",avgval(voltage))
    print("The number of elements is: ",numberofelements(voltage))

    print("\n")


    threshhold=float(input("Enter maximum threshold voltage:"))
    safe=unsafe=0
    for volt in voltage:
        if volt>threshhold:
            unsafe+=1
        else:
            safe+=1
    print("Number of safe voltage readings: ",safe)
    print("Number of unsafe voltage readings: ",unsafe)




elif choice==3:
    print("You have selected Temperature list \n")
    print(temperature)
    print("The maximum value is: ",maxval(temperature))
    print("The minimum value is: ",minval(temperature))
    print("The average value is: ",avgval(temperature))
    print("The number of elements is: ",numberofelements(temperature))

    print("\n")



    safe_temp=float(input("Enter safe limit for temperature analysis: "))
    for temp in temperature:
        if temp>safe_temp:
            print("Warning: Temperature exceeds safe limit of ",safe_temp,"C. Current temperature: ",temp,"C")
        else:
            print("Temperature is within safe limit of ",safe_temp,"C. Current temperature: ",temp,"C")





else:
    print("Invalid choice. Please select a valid option.")