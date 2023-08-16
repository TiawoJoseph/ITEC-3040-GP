import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# We are going to need to compare everything that we are doing for patients with hear disease against the patients that don't have heart disease to see the difference.
#Heat_Disease_Symptoms = Patients without heart disease (1)
#No_Heart_Disease_Symptoms = Patients with heart disease (2)

#Read the data in
df = pd.read_csv('ITEC3040A2_DS.csv')


print('///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
print('///////////////////////////////////////////////////  Patients Without Heart Disease  //////////////////////////////////////////////')
print('///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')


#Print the full table of attributes but only for the people with heart disease

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



#Average, Max, Min cholesterol
Cholesterol=Heart_Disease_Symptoms
Age_CH = Cholesterol.iloc[:,4]
Average_CH=Age_CH.mean()
Max_CH =Age_CH.max()
Min_CH = Age_CH.min()
print('Avg, Max, Min Cholesterol  ', Average_CH, Max_CH, Min_CH)


#Average, Ma... Resting ECG
# ECG=Heart_Disease_Symptoms[Heart_Disease_Symptoms['Sex'] == 0]
#  = ECG.iloc[:,5]
# Average_CH=Age_CH.mean()
# Max_CH =Age_CH.max()
# Min_CH = Age_CH.min()
# print('Avg, Max, Min Cholesterol  ', Average_CH, Max_CH, Min_CH)



# #Average, Ma... Max Heart Rate
# Cholesterol=Heart_Disease_Symptoms[Heart_Disease_Symptoms['Sex'] == 0]
# Age_CH = Cholesterol.iloc[:,5]
# Average_CH=Age_CH.mean()
# Max_CH =Age_CH.max()
# Min_CH = Age_CH.min()
# print('Avg, Max, Min Cholesterol  ', Average_CH, Max_CH, Min_CH)


# Thal=Heart_Disease_Symptoms[Heart_Disease_Symptoms['Sex'] == 0]
# Age_CH = Cholesterol.iloc[:,5]
# Average_CH=Age_CH.mean()
# Max_CH =Age_CH.max()
# Min_CH = Age_CH.min()
# print('Avg, Max, Min Cholesterol  ', Average_CH, Max_CH, Min_CH)

# NUMBER OF EXCERSICE INDUCED ANGIA 
Angina = Heart_Disease_Symptoms[Heart_Disease_Symptoms['Angina'] == 1]
print(Angina)

Not_Angina = Heart_Disease_Symptoms[Heart_Disease_Symptoms['Angina'] == 0]
print(Not_Angina)

print('///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
print('///////////////////////////////////////////////////  Patients With Heart Disease  /////////////////////////////////////////////////')
print('///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')

#Printing the full table of attributes but only for those who dont have heart disease 
No_Heart_Disease_Symptoms = df[df['Absence/Presence'] == 2]
print(No_Heart_Disease_Symptoms)

#Average age of the people who don't have heart disease
Age1 = No_Heart_Disease_Symptoms.iloc[:,0]
Average1 = Age1.mean()
Min1 = Age1.min()
Max1 = Age1.max()
print('This is the average of the people with heart attacks in this dataset')
print(Average1)

#Max age of the people have don't heart disease 
print('This is the max age of the people with heart attacks in this dataset')
print(Max1)

#Min age of the people that don't have heart disease 
print('This is the min age of the people with heart attacks in this dataset')
print(Min1)


#Count of men 
Men1=  No_Heart_Disease_Symptoms[No_Heart_Disease_Symptoms['Sex'] == 1]
print('These are all of the men')
print(Men1)
#Count of Women 
Women1=  No_Heart_Disease_Symptoms[No_Heart_Disease_Symptoms['Sex'] == 0]
print('These are all of the Women')
print(Women1)

Age_Women1 = Women1.iloc[:,0]
Average_Women1=Age_Women1.mean()
Max_Women1 =Age_Women1.max()
Min_Women1 = Age_Women1.min()
print('WOMEN AGES (Avg, Max, Min):  ', Average_Women1, Max_Women1, Min_Women1)
#Average, Max, Min age of Men to don'tget heart disease 
Age_Men1 = Men1.iloc[:,0]
Average_Men1=Age_Men1.mean()
Max_Men1 =Age_Men1.max()
Min_Men1 = Age_Men1.min()
print('MEN AGES (Avg, Max, Min): ', Average_Men1, Max_Men1, Min_Men1)


# Number of people that have chest pain 1
Chest_Pain_One1 = No_Heart_Disease_Symptoms[No_Heart_Disease_Symptoms['Chest Pain Type'] == 1]
print("These are all individuals with Chest Pain 1")
print(Chest_Pain_One1)
total_rows1 = Chest_Pain_One1.shape[0]
print('total number of people: ', total_rows1)
# Number of people that have chest pain 2
Chest_Pain_Two1 = No_Heart_Disease_Symptoms[No_Heart_Disease_Symptoms['Chest Pain Type'] == 2]
print("These are all individuals with Chest Pain 2")
print(Chest_Pain_Two1)
total_rows2 = Chest_Pain_Two1.shape[0]
print('total number of people: ', total_rows2)
# Number of people that have chest pain 3
Chest_Pain_Three1 = No_Heart_Disease_Symptoms[No_Heart_Disease_Symptoms['Chest Pain Type'] == 3]
print("These are all individuals with Chest Pain 3")
print(Chest_Pain_Three1)
total_rows3 = Chest_Pain_Three1.shape[0]
print('total number of people: ', total_rows3)
# Number of people that have chest pain 4
Chest_Pain_Four1 = No_Heart_Disease_Symptoms[No_Heart_Disease_Symptoms['Chest Pain Type'] == 4]
print("These are all individuals with Chest Pain 4")
total_rows4 = Chest_Pain_Four1.shape[0]
print(Chest_Pain_Four1)
print('total number of people: ', total_rows4)


Blood_Pressure_HD1 = No_Heart_Disease_Symptoms.iloc[:,3]
print(Blood_Pressure_HD1)
#Max BP
Max_BP1 = Blood_Pressure_HD1.max()
#Min BP 
Min_BP1 = Blood_Pressure_HD1.min()
#Average BP
AVG_BP1 = Blood_Pressure_HD1.mean()
print('Max BP: ', Max_BP1, 'Min Bp: ', Min_BP1, 'AVG BP: ', AVG_BP1)


#Fasting BP 0 [6]
BP_LessThan1 = No_Heart_Disease_Symptoms[No_Heart_Disease_Symptoms['Fasting BP']==0]
print('Blood Pressure is less than 120')
print(BP_LessThan1)
#FASTING BP  1 count

BP1 = No_Heart_Disease_Symptoms[No_Heart_Disease_Symptoms['Fasting BP']==1]
BP_Total1 = BP1.shape[0]
print('Blood Pressure is greater than 120')
print(BP_Total1)

#MIN [MIN HEART RATE]
Min_HeartRate1 = No_Heart_Disease_Symptoms.iloc[:,7]
Minimum_HR1 =Min_HeartRate1.min()
print('Thia is the min heart rate: ', Minimum_HR1)
#MAX [MIN HEART RATE]
Max_HeartRate1 = No_Heart_Disease_Symptoms.iloc[:,7]
Maximum_HeartRate1 =Max_HeartRate1.max()
print('Thia is the max heart rate: ', Maximum_HeartRate1)
# NUMBER OF EXCERSICE INDUCED ANGIA 
Angina1 = No_Heart_Disease_Symptoms[No_Heart_Disease_Symptoms['Angina'] == 1]
print('Patients with Induced Angina')
print(Angina1)

Not_Angina1 = No_Heart_Disease_Symptoms[No_Heart_Disease_Symptoms['Angina'] == 0]
print('Patients without Induced Angina')
print(Not_Angina1)

#Thal levels 
Thal =No_Heart_Disease_Symptoms.iloc[:,12]
print('heart disease patients with thal: ')
print(Thal.shape[0])
Thal1 = No_Heart_Disease_Symptoms[No_Heart_Disease_Symptoms['Thal'] == 3]
print('Patients with Thal = 3 : ')
print(Thal1.shape[0])

Thal6 = No_Heart_Disease_Symptoms[No_Heart_Disease_Symptoms['Thal'] == 6]
print('Patients with Thal = 6 : ')
print(Thal6.shape[0])

Thal7 = No_Heart_Disease_Symptoms[No_Heart_Disease_Symptoms['Thal'] == 7]
print('Patients with Thal = 7 : ')
print(Thal7.shape[0])

#No heart disease patients 
ThalN =Heart_Disease_Symptoms.iloc[:,12]
print('non heart disease patients with thal: ')
print(ThalN.shape[0])
Thal1N = Heart_Disease_Symptoms[Heart_Disease_Symptoms['Thal'] == 3]
print('Patients with Thal = 3 : ')
print(Thal1N.shape[0])

Thal6N = Heart_Disease_Symptoms[Heart_Disease_Symptoms['Thal'] == 6]
print('Patients with Thal = 6 : ')
print(Thal6N.shape[0])

Thal7N = Heart_Disease_Symptoms[Heart_Disease_Symptoms['Thal'] == 7]
print('Patients with Thal = 7 : ')
print(Thal7N.shape[0])


Correlation1=Heart_Disease_Symptoms.corr()
print(Correlation1)

correlation_with_target = df.corr()['Absence/Presence']
sorted_correlations = correlation_with_target.abs().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(x=sorted_correlations.index, y=sorted_correlations.values, palette='coolwarm')
plt.xticks(rotation=90)
plt.ylabel('Correlation with Absence/Presence')
plt.title('Correlation of Attributes with Absence/Presence of Heart Disease')
plt.tight_layout()
plt.show()



Correlation2=No_Heart_Disease_Symptoms.corr()
print(Correlation2)
Correlation3=df.corr()
print(Correlation3)