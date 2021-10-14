#!/usr/bin/env python
# coding: utf-8

# In[13]:


import glob
import re

Filelist = glob.glob('C:/Users/ASM_5/Downloads/Bootcamp Project/SEER_1973_2014_TEXTDATA/incidence/yr*/RESPIR.TXT') 
Resp = open("RESPIR.csv","w")
print('Disease,Age,Year_at_Diagnosis,Gender,Grade,Marital_Status,Primary_Site,Race,Regional_Nodes_Examined,Regional_Nodes_Positive,Summary_Stage,tumor_size,Survivability',file=Resp)

for file in Filelist:  #looping through the SEER files   
        infile = open(file,"r") #read-only each file 
        for line in infile: # loop line by line in each file 

            disease = line[52:57] #code in ICDO
            age = line[24:27] # Age at diagnosis
            year_at_diagnosis = line[38:42] 
            gender = line[23]
            grade = line[57]
            marital_status = line[18]
            primary_site = line[42:46]
            race = line[19:21]                 
            regional_nodes_examined = line[70:72]
            regional_nodes_positive = line[68:70]
            summary_stage = line[266]
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
                print(disease,',',age,',',year_at_diagnosis,',',gender,',',grade,',',marital_status,',',primary_site,',',race,',',regional_nodes_examined,',',regional_nodes_positive,',',
                      summary_stage,',',tumor_size,',',survivability,file=Resp)
        infile.close()


Resp.close()


# In[12]:


# import glob

# import re

# def ICDO_dictionary():
#     d = {}
#     infile = open("C:/Users/ASM_5/Downloads/Bootcamp Project/icdo3.txt","r")
#     for line in infile: 
#         r = re.search("(\d+/\d+)\s+(.+)",line)
#         if (r) :
#             code = r.group(1) 
#             code = code.replace("/","")
#             disease = r.group(2) 
#             disease=disease.rstrip()
#             disease = disease.lower()
#             d[code] = disease

#     infile.close()
#     return d

# def MS_dictionary():
#     m= {}
#     infile = open("C:/Users/ASM_5/Downloads/Bootcamp Project/marital_status.txt","r")
#     for line in infile:
#         r = re.search("(\d)\s+(.+)",line)
#         if (r) :
#             code = r.group(1)
#             ms = r.group(2)
#             ms = ms.rstrip()
#             ms = ms.lower()
#             m[code] = ms
#     infile.close()
#     return m

# def Grade_dictionary():
#     g = {} 
#     infile = open("C:/Users/ASM_5/Downloads/Bootcamp Project/grade.txt","r") 
#     for line in infile: 
#         r = re.search("(\d)\s+(.+)",line) 
#         if (r) :
#             code = r.group(1)
#             grade = r.group(2)
#             grade = grade.replace(",","")
#             grade = grade.replace(";"," ")
#             grade = grade.lstrip()
#             grade = grade.rstrip()
#             grade = grade.lower()
#             g[code] = grade

#     infile.close()
#     return g

# def Race_dictionary():
#     R = {} 
#     infile = open("C:/Users/ASM_5/Downloads/Bootcamp Project/race.txt","r") 
#     for line in infile:
#         r = re.search("(\d\d)\s+(.+)",line) 
#         if (r) :
#             code = r.group(1)
#             race = r.group(2)
#             race = race.replace(",","-")
#             race = race.rstrip()
#             race = race.lower()
#             R[code] = race

#     infile.close()
#     return R

# def Summary_dictionary():
#     s = {}
#     infile = open("C:/Users/ASM_5/Downloads/Bootcamp Project/summary_stage.txt","r")  
#     for line in infile:
#         r = re.search("(\d)\s+(.+)",line) 
#         if (r) :
#             code = r.group(1)
#             summary = r.group(2)
#             summary = summary.replace(",","")
#             summary = summary.replace("/","-")
#             summary = summary.rstrip()
#             summary = summary.lower()
#             s[code] = summary

#     infile.close()
#     return s

# def main():
    
#     filelist = glob.glob("C:/Users/ASM_5/Downloads/Bootcamp Project/SEER_1973_2014_TEXTDATA/incidence/yr*/RESPIR.TXT")

#     outfile_1 = open("RESPIR.csv","w") 
#     outfile_2 = open("RESPIR_STR.csv","w")
    
#     print('Disease,Age,Year_at_Diagnosis,Gender,Grade,Marital_Status,Primary_Site,Race,Regional_Nodes_Examined,Regional_Nodes_Positive,Summary_Stage,tumor_size,Survivability',file=outfile_1) 
#     print('Disease,Age,Year_at_Diagnosis,Gender,Grade,Marital_Status,Primary_Site,Race,Regional_Nodes_Examined,Regional_Nodes_Positive,Summary_Stage,tumor_size,Survivability',file=outfile_2) 


#     disease_di = ICDO_dictionary() 
#     grade_di = Grade_dictionary()  
#     marital_status_di = MS_dictionary()  
#     race_di = Race_dictionary()  
#     summary_stage_di = Summary_dictionary()  

#     for file in filelist:   
#         infile = open(file,"r") 
#         for line in infile: # 

#             disease = line[52:57] #code in ICDO
#             if disease in disease_di: #If the disease in disease dictionary
#                 disease_name = disease_di[disease].replace(',','')
#             else:
#                 disease_name = disease

#             age = line[24:27]
#             year_at_diagnosis = line[38:42] 

#             gender = line[23]
#             if gender == '1':
#                   gender_name = 'Male'
#             elif gender == '2':
#                   gender_name = 'Female'

#             grade = line[57]
#             if grade in grade_di: 
#                 grade_name = grade_di[grade]
#             else:
#                 grade_name = grade
                
#             marital_status = line[18]
#             if marital_status :
#                 marital_status_name = marital_status_di[marital_status]
#             else:
#                 marital_status_name = marital_status
                
#             primary_site = line[42:46]

#             race = line[19:21] 
#             if race in race_di: 
#                 race_name = race_di[race]
#             else:
#                 race_name = race
                
#             regional_nodes_examined = line[70:72]
#             regional_nodes_positive = line[68:70]
 
#             summary_stage = line[266]
#             if summary_stage in summary_stage_di: 
#                 summary_stage_name = summary_stage_di[summary_stage]
#             else:
#                 summary_stage_name = summary_stage

#             tumor_size = line[273]

#             cause_of_death = line[254:259] 
#             survival_month = int(line[300:304]) 
#             vital_status_recode = line[264] 

#             if (survival_month >= 60) and (vital_status_recode == '1'):
#                 survivability = "Survival"
#             else:
#                 if (survival_month < 60) and (cause_of_death == '22010' or cause_of_death == '22020' or cause_of_death == '22030' or cause_of_death == '22050'or cause_of_death ==  '22060'):
#                     survivability = "Not_Survival"
#                 else:
#                     survivability = "Died_of_other_cause"
                    
#             if (year_at_diagnosis >= '2008' and year_at_diagnosis <= '2012') and (survivability != "Died_of_other_cause"):
#                 print(disease_name,',',age,',',year_at_diagnosis,',',gender_name,',',grade_name,',',marital_status_name,',',primary_site,',',race_name,',',regional_nodes_examined,',',regional_nodes_positive,',',summary_stage_name,',',tumor_size,',',survivability,file=outfile_1)
#                 print(disease,',',age,',',year_at_diagnosis,',',gender,',',grade,',',marital_status,',',primary_site,',',race,',',regional_nodes_examined,',',regional_nodes_positive,',',summary_stage,',',tumor_size,',',survivability,file=outfile_2)
                
#         infile.close()

#     outfile_1.close()
#     outfile_2.close()






# In[14]:


import pandas as pd

df = pd.read_csv('C:/Users/ASM_5/Downloads/Bootcamp Project/RESPIR.csv')
df.shape


# In[15]:


df


# In[16]:



df_size = df.groupby(['Survivability']).size().reset_index(name='counts')
df_size = pd.DataFrame(df_size)
df_size


# In[7]:


get_ipython().system('pip install pandas_profiling')


# In[18]:


from pandas_profiling import ProfileReport
profile = ProfileReport(df)
profile

