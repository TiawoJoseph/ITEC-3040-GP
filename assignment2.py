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

# Number of people that have chest pain 2
# Number of people that have chest pain 3
# Number of people that have chest pain 4


#Max BP
#Min BP 
#Average BP

#Fasting BP MAX
#FASTING BP MIN 
#FASTING BP AVG

#MIN [MIN HEART RATE]
#MAX [MIN HEART RATE]

# NUMBER OF EXCERSICE INDUCED ANGIA 