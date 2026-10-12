#Q3 textfile

print("\n")

f=open("flight_log.txt","w")
f.write("Flight 001\nDrone ID: D001\nDate: 2026-10-04\nDuration: 12 minutes\nMaximum Altitude: 120 meters")
f.close()


f=open("flight_log.txt","r")
print("The flight log is as follows:\n")
print(f.read())
print("\n")
f.close()

f=open("flight_log.txt","a")
f.write("\nFlight 002\nDrone ID: D002\nDate: 2026-10-05\nDuration: 15 minutes\nMaximum Altitude: 150 meters")
f.close()

f=open("flight_log.txt","r")
print("The flight log is as follows:\n")
print(f.read())
print("\n")
f.close()
