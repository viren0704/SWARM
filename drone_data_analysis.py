import pandas as pd
import numpy as np

data=pd.read_csv('dataset.csv')

#3.1

print(data.head())
print("\n")

print("dimensions of dataset=",data.shape)
print("\n")

print("columns of dataset=\n",data.columns)
print("\n")

print("data type of each column=\n",data.dtypes)
print("\n")

print("dataset info=\n")
print(data.info())
print("\n")

print("statistical summary of dataset=\n")
print(data.describe())
print("\n")



#3.2

print("Number of Missing values:")
print(data.isnull().sum())
print("\n")

print("Missing values:")
print(data.isnull())
print("\n")

print("Number of duplicate rows=", data.duplicated().sum())
print("\n")

print("Duplicate rows:")
print(data[data.duplicated()])
print("\n")

print(pd.to_datetime(data["Flight Date"], errors="coerce").dtype)
convert_date = pd.to_datetime(data["Flight Date"], errors="coerce")
print('\n')
print("Number of Invalid dates:", convert_date.isna().sum())
print('\n')
print("Invalid date entries:")
print(data.loc[convert_date.isna(), "Flight Date"])

print('\n')
print("-----------------------------------------------------------")
print("\n")
# print(data["Flight Date"].dropna().head(10))

print("Minimum values:")
print(data.select_dtypes(include=np.number).min())
print('\n')
print("Maximum values:")
print(data.select_dtypes(include=np.number).max())
print('\n')

print(data[data["Actual Carry Weight (kg)"]<0])
print('\n')

print(data[(data["Battery Remaining (%)"]<0) | (data["Battery Remaining (%)"]>100)])
print('\n')

print(data[data["Altitude (meters)"]<0])
print('\n')

print(data[data["Propeller Count"]<=0])
print('\n')

print(data[data["Max Carry Weight (kg)"]<=0])
print('\n')

print(data[data["Flight Duration (minutes)"]<=0])
print('\n')

print(data[data["Distance Flown (km)"]<0])
print('\n')

print(data[data["GPS Accuracy (meters)"]<=0])
print('\n')

print(data[data["Wind Speed (m/s)"]<0])
print('\n')

# print(data.select_dtypes(include=np.number).describe())
# print('\n')

# print(data.nlargest(10, "Altitude (meters)")[["Drone ID", "Altitude (meters)", "Flight Duration (minutes)", "Flight Status"]
# ].to_string(index=False))
# print('\n')

print("------------------------------------------")
print('\n')

Q1=data.select_dtypes(include=np.number).quantile(0.25)
Q3=data.select_dtypes(include=np.number).quantile(0.75)
IQR= Q3-Q1
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
print("Potential outliner counts:")
print(((data.select_dtypes(include=np.number)<lower_bound) | (data.select_dtypes(include=np.number)>upper_bound)).sum())
print('\n')

print("------------------------------------------")
print('\n')

# print(data[data["Actual Carry Weight (kg)"]<lower_bound["Actual Carry Weight (kg)"]][["Drone ID","Max Carry Weight (kg)","Actual Carry Weight (kg)","Payload Type","Notes"]].to_string(index=False))
# print('\n')


# print("------------------------------------------")
# print('\n')

#invalid dates
data["Flight Date"]=pd.to_datetime(data["Flight Date"], errors="coerce",dayfirst=True)

data.loc[data["Actual Carry Weight (kg)"]<0,"Actual Carry Weight (kg)"]=np.nan

# remove duplicates

data=data.drop_duplicates()

print("Missing values after cleaning:")
print(data.isnull().sum())
print("Shape=",data.shape)

print("------------------------------------------")
print('\n')

#save

data.to_csv("cleaned_drone_data.csv",index=False)
print("Cleaned dataset saved")
print('\n')
