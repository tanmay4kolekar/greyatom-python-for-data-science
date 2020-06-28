# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
census=np.concatenate((data,new_record),axis=0)
print("*/"*50)
print("Census is:",census)

age=np.array([])
for i in range(0,len(census)):
    age=np.append(age,census[i][0])
print("*/"*50)
print("Age is:",age)

max_age=age.max()
print("Max age is:",max_age )

min_age=age.min()
print("Min age is:",min_age )

age_mean=age.mean()
print("Mean age is:",age_mean)

age_std=np.std(age)
print("Std Deviation is:",age_std)

race_0=np.array([])
for i in range(0,len(census)):
    if(census[i][2]==0):
        race_0=np.append(race_0,census[i][2])

race_1=np.array([])
for i in range(0,len(census)):
    if(census[i][2]==1):
        race_1=np.append(race_1,census[i][2])

race_2=np.array([])
for i in range(0,len(census)):
    if(census[i][2]==2):
        race_2=np.append(race_2,census[i][2])

race_3=np.array([])
for i in range(0,len(census)):
    if(census[i][2]==3):
        race_3=np.append(race_3,census[i][2])

race_4=np.array([])
for i in range(0,len(census)):
    if(census[i][2]==4):
        race_4=np.append(race_4,census[i][2])

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

print("*/"*50)
print("race_0 length is:",len_0)
print("race_1 length is:",len_1)
print("race_2 length is:",len_2)
print("race_3 length is:",len_3)
print("race_4 length is:",len_4)

if(min(len_0,len_1,len_2,len_3,len_4)==len_0):
    minority_race=0
elif(min(len_0,len_1,len_2,len_3,len_4)==len_1):
    minority_race=1
elif(min(len_0,len_1,len_2,len_3,len_4)==len_2):
    minority_race=2
elif(min(len_0,len_1,len_2,len_3,len_4)==len_3):
    minority_race=3
elif(min(len_0,len_1,len_2,len_3,len_4)==len_4):
    minority_race=4

print("*/"*50)
print("minority  race is :",minority_race)

senior_citizens=np.array([])
count=0
for i in census:
    if i[0]>60:
        senior_citizens=np.concatenate((senior_citizens,i),axis=0)
        count+=1

#print("Senior citz are:",senior_citizens)
senior_citizens=senior_citizens.reshape(count,8)
print("/*"*25)
print("NEW Senior citz are:",len(senior_citizens))

working_hours_sum=0
for i in range(0,len(senior_citizens)):
    working_hours_sum+=senior_citizens[i][6]
        
print("/*"*25)
print("working_hours_sum is:",working_hours_sum)

senior_citizens_len=len(senior_citizens)
print("length of SeniorCitizens is:",senior_citizens_len)

avg_working_hours=np.divide(working_hours_sum,senior_citizens_len)
print("avg_working hours",avg_working_hours)

high=[]
count=0
for i in census:
    if i[1]>10:
        high.append(i)
        count+=1
print("/*"*25)
high=np.asarray(high)
print("High:",len(high))

low=[]
count=0
for i in census:
    if i[1]<=10:
        low.append(i)
        count+=1
print("/*"*25)
low=np.asarray(low)
print("LOW:",len(low))

pay_high=0
for i in range(0,len(high)):
   pay_high=pay_high+high[i][7]
print("Pay_high",pay_high)
avg_pay_high=pay_high/len(high)
print("AVG High PAy",avg_pay_high)

pay_low=0
for i in range(0,len(low)):
   pay_low=pay_low+low[i][7]
print("Pay_high",pay_low)
avg_pay_low=pay_low/len(low)
print("AVG Low PAy",avg_pay_low)
#Code starts here




