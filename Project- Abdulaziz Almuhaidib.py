#!/usr/bin/env python
# coding: utf-8

# In[141]:


import glob
import re

# Filelist = glob.glob('C:/Users/ASM_5/Downloads/Bootcamp Project/SEER_1973_2014_TEXTDATA/incidence/yr*/RESPIR.TXT') 
# Resp = open("RESPIR.csv","w")
# print('Disease,Age,Year_at_Diagnosis,Gender,Grade,Marital_Status,Primary_Site,Race,Regional_Nodes_Examined,Regional_Nodes_Positive,Summary_Stage,tumor_size,Survivability',file=Resp)

# for file in Filelist:  #looping through the SEER files   
#         infile = open(file,"r") #read-only each file 
#         for line in infile: # loop line by line in each file 

#             disease = line[52:57] #code in ICDO
#             age = line[24:27] # Age at diagnosis
#             year_at_diagnosis = line[38:42] 
#             gender = line[23]
#             grade = line[57]
#             marital_status = line[18]
#             primary_site = line[43:46]
#             race = line[19:21]                 
#             regional_nodes_examined = line[70:72]
#             regional_nodes_positive = line[68:70]
#             summary_stage = line[266]
#             tumor_size = line[273]
#             cause_of_death = line[254:259] 
#             survival_month = int(line[300:304]) 
#             vital_status_recode = line[264] 

#             if (survival_month >= 60) and (vital_status_recode == '1'):
#                 survivability = 0
#             else:
#                 if (survival_month < 60) and (cause_of_death == '22010' or cause_of_death == '22020' or cause_of_death == '22030' or cause_of_death == '22050'or cause_of_death ==  '22060'):
#                     survivability = 1
#                 else:
#                     survivability = "Died_of_other_cause"
                    

#             if (year_at_diagnosis >= '2008' and year_at_diagnosis <= '2012') and (survivability != "Died_of_other_cause"):
#                 print(disease,',',age,',',year_at_diagnosis,',',gender,',',grade,',',marital_status,',',primary_site,',',race,',',regional_nodes_examined,',',regional_nodes_positive,',',
#                       summary_stage,',',tumor_size,',',survivability,file=Resp)
#         infile.close()


# Resp.close()


# In[2]:


ICDO_dictionary = {}
infile = open("C:/Users/ASM_5/Downloads/Bootcamp Project/icdo3.txt","r")
for line in infile: 
    r = re.search("(\d+/\d+)\s+(.+)",line)
    if (r) :
        code = r.group(1) 
        code = code.replace("/","")
        disease = r.group(2) 
        disease=disease.rstrip()
        disease = disease.lower()
        ICDO_dictionary[code] = disease

infile.close()


# In[3]:


MS_dictionary= {}
infile = open("C:/Users/ASM_5/Downloads/Bootcamp Project/marital_status.txt","r")
for line in infile:
    r = re.search("(\d)\s+(.+)",line)
    if (r) :
        code = r.group(1)
        ms = r.group(2)
        ms = ms.rstrip()
        ms = ms.lower()
        MS_dictionary[code] = ms
infile.close()


# In[4]:


Grade_dictionary = {} 
infile = open("C:/Users/ASM_5/Downloads/Bootcamp Project/grade.txt","r") 
for line in infile: 
    r = re.search("(\d)\s+(.+)",line) 
    if (r) :
        code = r.group(1)
        grade = r.group(2)
        grade = grade.replace(",","")
        grade = grade.replace(";"," ")
        grade = grade.lstrip()
        grade = grade.rstrip()
        grade = grade.lower()
        Grade_dictionary[code] = grade

infile.close()


# In[6]:


Race_dictionary = {} 
infile = open("C:/Users/ASM_5/Downloads/Bootcamp Project/race.txt","r") 
for line in infile:
    r = re.search("(\d\d)\s+(.+)",line) 
    if (r) :
        code = r.group(1)
        race = r.group(2)
        race = race.replace(",","-")
        race = race.rstrip()
        race = race.lower()
        Race_dictionary[code] = race

infile.close()


# In[7]:


Summary_dictionary = {}
infile = open("C:/Users/ASM_5/Downloads/Bootcamp Project/summary_stage.txt","r")  
for line in infile:
    r = re.search("(\d)\s+(.+)",line) 
    if (r) :
        code = r.group(1)
        summary = r.group(2)
        summary = summary.replace(",","")
        summary = summary.replace("/","-")
        summary = summary.rstrip()
        summary = summary.lower()
        Summary_dictionary[code] = summary

infile.close()


# In[8]:


filelist = glob.glob("C:/Users/ASM_5/Downloads/Bootcamp Project/SEER_1973_2014_TEXTDATA/incidence/yr*/RESPIR.TXT")

outfile = open("RESPIR_1.csv","w") 

print('Disease,Age,Year_at_Diagnosis,Gender,Grade,Marital_Status,Primary_Site,Race,Regional_Nodes_Examined,Regional_Nodes_Positive,Summary_Stage,tumor_size,Survivability',file=outfile) 

disease_di = ICDO_dictionary
grade_di = Grade_dictionary  
marital_status_di = MS_dictionary 
race_di = Race_dictionary  
summary_stage_di = Summary_dictionary  

for file in filelist:   
    infile = open(file,"r") 
    for line in infile: 

        disease = line[52:57] #code in ICDO
        if disease in disease_di: #If the disease in disease dictionary
            disease_name = disease_di[disease].replace(',','')
        else:
            disease_name = disease

        age = line[24:27]
        year_at_diagnosis = line[38:42] 

        gender = line[23]
        if gender == '1':
            gender_name = 'Male'
        elif gender == '2':
            gender_name = 'Female'

        grade = line[57]
        if grade in grade_di: 
            grade_name = grade_di[grade]
        else:
            grade_name = grade
                
        marital_status = line[18]
        if marital_status :
            marital_status_name = marital_status_di[marital_status]
        else:
            marital_status_name = marital_status
                
        primary_site = line[42:46]

        race = line[19:21] 
        if race in race_di: 
            race_name = race_di[race]
        else:
            race_name = race
                
        regional_nodes_examined = line[70:72]
        regional_nodes_positive = line[68:70]
 
        summary_stage = line[266]
        if summary_stage in summary_stage_di: 
            summary_stage_name = summary_stage_di[summary_stage]
        else:
            summary_stage_name = summary_stage

        tumor_size = line[273]

        cause_of_death = line[254:259] 
        survival_month = int(line[300:304]) 
        vital_status_recode = line[264] 

        if (survival_month >= 60) and (vital_status_recode == '1'):
            survivability = "Survival"
        else:
            if (survival_month < 60) and (cause_of_death == '22010' or cause_of_death == '22020' or cause_of_death == '22030' or cause_of_death == '22050'or cause_of_death ==  '22060'):
                survivability = "Not_Survival"
            else:
                survivability = "Died_of_other_cause"
                    
        if (year_at_diagnosis >= '2008' and year_at_diagnosis <= '2012') and (survivability != "Died_of_other_cause"):
            print(disease_name,',',age,',',year_at_diagnosis,',',gender_name,',',grade_name,',',marital_status_name,',',primary_site,',',race_name,',',regional_nodes_examined,',',regional_nodes_positive,',',summary_stage_name,',',tumor_size,',',survivability,file=outfile)
                
    infile.close()

outfile.close()


# In[64]:


import pandas as pd

df = pd.read_csv('C:/Users/ASM_5/Downloads/Bootcamp Project/RESPIR_1.csv')
df.shape


# In[65]:


df


# In[89]:


df['Primary_Site'].value_counts()


# In[66]:


df.isnull().sum()


# In[67]:


df_size = df.groupby(['Survivability']).size().reset_index(name='counts')
df_size = pd.DataFrame(df_size)
df_size


# In[68]:


import matplotlib.pyplot as plt
plt.bar(df_size['Survivability'],df_size['counts'])


# In[69]:


df_Summary_Stage = df.groupby(['Summary_Stage','Survivability']).size().reset_index(name='counts')
df_Summary_Stage


# In[70]:


df_Summary_Stage_NS = df_Summary_Stage.reset_index().pivot(columns='Survivability', index='Summary_Stage', values='counts')
df_Summary_Stage_NS


# In[71]:


df_Summary_Stage_NS['total']=df_Summary_Stage_NS.sum(axis=1)
df_Summary_Stage_NS


# In[72]:


df_Summary_Stage_NS['percentage'] = (df_Summary_Stage_NS[' Survival']/df_Summary_Stage_NS['total'])*100
df_Summary_Stage_NS.reset_index( inplace=True)
df_Summary_Stage_NS


# In[73]:


plt.barh(df_Summary_Stage_NS['Summary_Stage'],df_Summary_Stage_NS['percentage'])


# In[76]:


df_Grade_NS = df.groupby(['Grade','Survivability']).size().reset_index(name='counts')
df_Grade_NS


# In[77]:


df_Grade_NS = df_Grade_NS.reset_index().pivot(columns='Survivability', index='Grade', values='counts')
df_Grade_NS


# In[78]:


df_Grade_NS['total']=df_Grade_NS.sum(axis=1)
df_Grade_NS


# In[79]:


df_Grade_NS['percentage'] = (df_Grade_NS[' Survival']/df_Grade_NS['total'])*100
df_Grade_NS.reset_index( inplace=True)
df_Grade_NS


# In[80]:


plt.barh(df_Grade_NS['Grade'],df_Grade_NS['percentage'])


# In[75]:


from pandas_profiling import ProfileReport
profile = ProfileReport(df)
profile


# In[90]:


df.shape


# In[92]:


# one hot encouding 
dfe = pd.get_dummies(df)
dfe.shape


# In[113]:


df.head()


# In[143]:


dfn = pd.read_csv('C:/Users/ASM_5/Downloads/Bootcamp Project/RESPIR.csv')


# In[125]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import seaborn as sn
import matplotlib.pyplot as plt


# In[144]:


#Random Forest
X = dfn[['Disease', 
        'Age',
        'Year_at_Diagnosis',
        'Gender',
        'Grade',
        'Marital_Status',
        'Primary_Site',
        'Race',
        'Regional_Nodes_Examined',
        'Regional_Nodes_Positive',
        'Summary_Stage',
        'tumor_size']]

y = dfn['Survivability']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)


# In[145]:


clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)


# In[148]:


print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))


# In[150]:


#KNN
from sklearn.neighbors import KNeighborsClassifier

X = dfn[['Disease', 
        'Age',
        'Year_at_Diagnosis',
        'Gender',
        'Grade',
        'Marital_Status',
        'Primary_Site',
        'Race',
        'Regional_Nodes_Examined',
        'Regional_Nodes_Positive',
        'Summary_Stage',
        'tumor_size']]

y = dfn['Survivability']


# In[153]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[154]:


knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))


# In[156]:


#cross valdiation 
from sklearn.model_selection import cross_val_score

knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
print(scores)


# In[157]:


scores.mean()


# In[162]:


clf = RandomForestClassifier()
scores_RF = cross_val_score(clf, X_train, y_train, cv=10)

print (scores_RF)


# In[163]:


scores_RF.mean()

