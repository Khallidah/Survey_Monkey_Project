#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import os


# In[22]:


pwd=os.getcwd()


# In[28]:


dataset=pd.read_excel("C:\\Users\idris\Documents\Data - Survey Monkey Output Edi.xlsx", sheet_name="Edited_Data")


# In[29]:


dataset


# In[31]:


dataset_modified=dataset.copy()
dataset_modified


# In[32]:


columns_to_drop = ['Start.Date', 'End.Date', 'Email.Address', 'First.Name', 'Last.Name', 'Custom.Data.1']
columns_to_drop


# In[33]:


dataset_modified = dataset_modified.drop(columns=columns_to_drop)


# In[34]:


dataset_modified


# In[35]:


id_vars = list(dataset_modified.columns)[:8]
value_vars = list(dataset_modified.columns)[8: ]


# In[36]:


dataset_melted = dataset_modified.melt(id_vars=id_vars, value_vars=value_vars, var_name="Question + Subquestion", value_name="Answers")


# In[37]:


dataset_melted


# In[38]:


questions_import = pd.read_excel("C:\\Users\idris\Documents\Data - Survey Monkey Output Edi.xlsx", sheet_name="Questions")


# In[39]:


questions_import


# In[40]:


questions = questions_import.copy()
questions.drop(columns=["Raw Questions", "Sub Questions", "Subquestions"], inplace=True)


# In[41]:


questions


# In[52]:


dataset_merged = pd.merge(left=dataset_melted, right=questions, how="left", left_on="Question + Subquestion", right_on="Question + Subquestion")
print("Original Data", len(dataset_merged))
print("Merged Data", len(dataset_merged))


# In[53]:


dataset_merged


# In[50]:


respondents = dataset_merged[dataset_merged["Answers"].notna()]
respondents = respondents.groupby("Questions")["Respondent.ID"].nunique().reset_index()
respondents.rename(columns={"Respondent.ID":"Respondents"}, inplace=True)
respondents


# In[57]:


dataset_merged_two = pd.merge(left=dataset_merged, right=respondents, how="left", left_on="Questions", right_on="Questions")
print("Original Data", len(dataset_merged))
print("Merged Data", len(dataset_merged_two))
dataset_merged_two


# In[59]:


same_answer = dataset_merged #  [dataset_merged["Answers"].notna()]
same_answer = same_answer.groupby(["Question + Subquestion", "Answers"])["Respondent.ID"].nunique().reset_index()
same_answer.rename(columns={"Respondent.ID":"Same Answer"}, inplace=True)
same_answer


# In[62]:


dataset_merged_three = pd.merge(left=dataset_merged_two, right=same_answer, how="left", left_on=["Question + Subquestion", "Answers"], right_on=["Question + Subquestion", "Answers"])
dataset_merged_three["Same Answer"].fillna(0, inplace=True)
print("Original Data", len(dataset_merged_two))
print("Merged Data", len(dataset_merged_three))
dataset_merged_three


# In[63]:


output = dataset_merged_three.copy()
output.rename(columns={"Identify.which.division.you.work.in....Response":"Division Primary", "Identify.which.division.you.work.in....Other.(please.specify)":"Division Secondary", 
   "Which.of.the.following.best.describes.your.position.level?...Response":"Position", "Which.generation.are.you.apart.of?...Response":"Generation", 
   "Please.select.the.gender.in.which.you.identify....Response":"Gender", "Which.duration.range.best.aligns.with.your.tenure.at.your.company?...Response":"Tenure", 
   "Which.of.the.following.best.describes.your.employment.type?...Response":"Employment"}, inplace=True)
output


# In[76]:


output_file_path = r"C:\Users\idris\OneDrive\Documents\Output Data.xlsx"


# In[79]:


output.to_excel(output_file_path, index=False)


# In[ ]:




