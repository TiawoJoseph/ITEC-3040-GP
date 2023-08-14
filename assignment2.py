import pandas as pd
import numpy as np


# We are going to need to compare everything that we are doing for patients with hear disease against the patients that don't have heart disease to see the difference.


#Read the data in
df = pd.read_csv('ITEC3040A2_DS.csv')

#Print the full table of attributes but only for the people with heart disease
print('Symptoms among people who have heart disease')
Heart_Disease_Symptoms = df[df['Absence/Presence'] == 1]
print(Heart_Disease_Symptoms)


#Average age of the people who have heart disease
Age = Heart_Disease_Symptoms.iloc[:,0]
Average = Age.mean()
Min = Age.min()
Max = Age.max()
print('This is the average of the people with heart attacks in this dataset')
print(Average)

#Max age of the people have heart disease 
print('This is the max age of the people with heart attacks in this dataset')
print(Max)

#Min age of the people that have heart disease 
print('This is the min age of the people with heart attacks in this dataset')
print(Min)



#Count of men 
Men=  Heart_Disease_Symptoms[Heart_Disease_Symptoms['Sex'] == 1]
print('These are all of the men')
print(Men)
#Count of Women 
Women=  Heart_Disease_Symptoms[Heart_Disease_Symptoms['Sex'] == 0]
print('These are all of the Women')
print(Women)

#Average, Max, Min age of women to get heart disease 
Age_Women = Women.iloc[:,0]
Average_Women=Age_Women.mean()
Max_Women =Age_Women.max()
Min_Women = Age_Women.min()
print('WOMEN AGES (Avg, Max, Min):  ', Average_Women, Max_Women, Min_Women)
#Average, Max, Min age of Men to get heart disease 
Age_Men = Men.iloc[:,0]
Average_Men=Age_Men.mean()
Max_Men =Age_Men.max()
Min_Men = Age_Men.min()
print('MEN AGES (Avg, Max, Min): ', Average_Men, Max_Men, Min_Men)

# Number of people that have chest pain 1
Chest_Pain_One = Heart_Disease_Symptoms[Heart_Disease_Symptoms['Chest Pain Type'] == 1]
print("These are all individuals with Chest Pain 1")
print(Chest_Pain_One)
total_rows = Chest_Pain_One.shape[0]
print('total number of people: ', total_rows)
# Number of people that have chest pain 2
Chest_Pain_Two = Heart_Disease_Symptoms[Heart_Disease_Symptoms['Chest Pain Type'] == 2]
print("These are all individuals with Chest Pain 2")
print(Chest_Pain_Two)
total_rows = Chest_Pain_Two.shape[0]
print('total number of people: ', total_rows)
# Number of people that have chest pain 3
Chest_Pain_Three = Heart_Disease_Symptoms[Heart_Disease_Symptoms['Chest Pain Type'] == 3]
print("These are all individuals with Chest Pain 3")
print(Chest_Pain_Three)
total_rows = Chest_Pain_Three.shape[0]
print('total number of people: ', total_rows)
# Number of people that have chest pain 4
Chest_Pain_Four = Heart_Disease_Symptoms[Heart_Disease_Symptoms['Chest Pain Type'] == 4]
print("These are all individuals with Chest Pain 4")
total_rows = Chest_Pain_Four.shape[0]
print(Chest_Pain_Four)
print('total number of people: ', total_rows)


Blood_Pressure_HD = Heart_Disease_Symptoms.iloc[:,3]
print(Blood_Pressure_HD)
#Max BP
Max_BP = Blood_Pressure_HD.max()
#Min BP 
Min_BP = Blood_Pressure_HD.min()
#Average BP
AVG_BP = Blood_Pressure_HD.mean()
print('Max BP: ', Max_BP, 'Min Bp: ', Min_BP, 'AVG BP: ', AVG_BP)

#Fasting BP 0 [6]
BP_LessThan = Heart_Disease_Symptoms[Heart_Disease_Symptoms['Fasting BP']==0]
print(BP_LessThan)
#FASTING BP  1 count

BP = Heart_Disease_Symptoms[Heart_Disease_Symptoms['Fasting BP']==1]
BP_Total = BP.shape[0]
print(BP_Total)

#MIN [MIN HEART RATE]
Min_HeartRate = Heart_Disease_Symptoms.iloc[:,7]
Minimum_HR =Min_HeartRate.min()
print('Thia is the min heart rate: ', Minimum_HR)
#MAX [MIN HEART RATE]
Max_HeartRate = Heart_Disease_Symptoms.iloc[:,7]
Maximum_HeartRate =Max_HeartRate.max()
print('Thia is the max heart rate: ', Maximum_HeartRate)
# NUMBER OF EXCERSICE INDUCED ANGIA 
Angina = Heart_Disease_Symptoms[Heart_Disease_Symptoms['Angia'] == 1]
print(Angina)

Not_Angina = Heart_Disease_Symptoms[Heart_Disease_Symptoms['Angia'] == 0]
print(Not_Angina)

print('///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
print('///////////////////////////////////////////////////  Patients Without Heart Disease  //////////////////////////////////////////////')
print('///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')

#Printing the full table of attributes but only for those who dont have heart disease 
No_Heart_Disease_Symptoms = df[df['Absence/Presence'] == 2]
print(No_Heart_Disease_Symptoms)

