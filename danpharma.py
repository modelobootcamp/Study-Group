#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[2]:


# Hide warning messages in notebook
import warnings
warnings.filterwarnings('ignore')

# File to Load (Remember to Change These)
mouse_drug = "data/mouse_drug_data.csv"
clinical_trial = "data/clinicaltrial_data.csv"


# Read the Mouse and Drug Data and the Clinical Trial Data
mouse_drug_df = pd.read_csv(mouse_drug)
clinical_trial_df = pd.read_csv(clinical_trial)


# Combine the data into a single dataset
merged = pd.merge(mouse_drug_df, clinical_trial_df, on="Mouse ID", how="outer")

# Display the data table for preview
merged.head()


# In[3]:


#merged.count()


# In[4]:


#mouse_drug_df.count()


# In[5]:


#clinical_trial_df.count()


# ## Tumor Response to Treatment

# In[29]:


# Store the Mean Tumor Volume Data Grouped by Drug and Timepoint 
grouped_by_merged = merged.groupby(['Drug','Timepoint'])
mean_tumor_volume=grouped_by_merged["Tumor Volume (mm3)"].mean()

# Convert to DataFrame and reset index
mtv_df=mean_tumor_volume.to_frame()

# Preview DataFrame
#print (type (mtv_df))
mtv_df.head()


# In[ ]:





# In[70]:


# Store the Standard Error of Tumor Volumes Grouped by Drug and Timepoint
# grouped_by_merged = merged.groupby(['Drug','Timepoint'])
sem_tumor_volume=grouped_by_merged["Tumor Volume (mm3)"].sem()

# Convert to DataFrame
stv_df=sem_tumor_volume.to_frame()

# Preview DataFrame
print (type (stv_df))
stv_df.head(3)


# In[71]:


grouped_by_timeline = mtv_df.groupby(['Timepoint','Drug'])
grouped_by_timeline = grouped_by_timeline["Tumor Volume (mm3)"].mean()

# Convert to DataFrame
time_df=grouped_by_timeline.to_frame().reset_index()

# Preview DataFrame
print (type (time_df))
time_df.head(3)


# In[72]:


# Minor Data Munging to Re-Format the Data Frames using unstack
organized_df = mtv_df.unstack(level='Drug')

# Convert MultiIndex to single index to get desired drug columns
organized_df.columns = organized_df.columns.get_level_values(1)
organized_df = organized_df[['Capomulin','Infubinol','Ketapril','Placebo']]
# Preview that Reformatting worked
organized_df.head()


# In[73]:


# SEM Minor Data Munging to Re-Format the Data Frames using unstack
sem_organized_df = stv_df.unstack(level='Drug')
sem_organized_df


# In[74]:


# Convert MultiIndex to single index to get desired drug columns
sem_organized_df.columns = sem_organized_df.columns.get_level_values(1)
sem_organized_df = sem_organized_df[['Capomulin','Infubinol','Ketapril','Placebo']]
# Preview that Reformatting worked
sem_organized_df.head()


# In[87]:


# Generate the Plot (with Error Bars)
# create line graph

x_axis=organized_df.index
Capomulin_axis=organized_df['Capomulin'].values
lineplot = plt.plot(x_axis, Capomulin_axis, marker ='o', color='blue', label="Capomulin")

Capomulin_sem_axis=sem_organized_df['Capomulin'].values


Infubinol_axis=organized_df['Infubinol'].values
lineplot = plt.plot(x_axis, Infubinol_axis, marker ='o', color='R', label="Infubinol")
Infubinol_sem_axis=sem_organized_df['Infubinol'].values

Ketapril_axis=organized_df['Ketapril'].values
lineplot = plt.plot(x_axis, Ketapril_axis, marker ='o', color='G', label="Ketapril")
Ketapril_sem_axis=sem_organized_df['Ketapril'].values

Placebo_axis=organized_df['Placebo'].values
lineplot = plt.plot(x_axis, Placebo_axis, marker ='o', color='Y', label="Placebo")
Placebo_sem_axis=sem_organized_df['Placebo'].values


# In[88]:


# Setting up the plot
fig, ax = plt.subplots()

ax.errorbar(x_axis,Capomulin_axis, Capomulin_sem_axis, marker ='o', color='blue', label="Capomulin")
ax.errorbar(x_axis,Infubinol_axis, Infubinol_sem_axis, marker ='o', color='R', label="Infubinol")
ax.errorbar(x_axis,Ketapril_axis, Ketapril_sem_axis, marker ='o', color='Y', label="Ketapril")
ax.errorbar(x_axis,Placebo_axis, Placebo_sem_axis, marker ='o', color='G', label="Placebo")

#ax.set_xlim(-1, len(samples) + 1)

#ax.set_xlabel(“Sample Number”)
#ax.set_ylabel(“Proportion of People Voting Republican”)


#print(Capomulin_axis)

#print(x_axis)
# Save the Figure


# In[11]:


# Show the Figure
plt.show()


# ## Metastatic Response to Treatment

# In[12]:


# Store the Mean Met. Site Data Grouped by Drug and Timepoint 

# Convert to DataFrame

# Preview DataFrame


# In[ ]:





# In[13]:


# Store the Standard Error associated with Met. Sites Grouped by Drug and Timepoint 

# Convert to DataFrame

# Preview DataFrame


# In[ ]:





# In[14]:


# Minor Data Munging to Re-Format the Data Frames

# Preview that Reformatting worked


# In[ ]:





# In[15]:


# Generate the Plot (with Error Bars)

# Save the Figure

# Show the Figure


# In[ ]:





# ## Survival Rates

# In[16]:


# Store the Count of Mice Grouped by Drug and Timepoint (W can pass any metric)

# Convert to DataFrame

# Preview DataFrame


# In[ ]:





# In[17]:


# Minor Data Munging to Re-Format the Data Frames

# Preview the Data Frame


# In[ ]:





# In[18]:


# Generate the Plot (Accounting for percentages)

# Save the Figure

# Show the Figure
plt.show()


# In[ ]:





# ## Summary Bar Graph

# In[19]:


# Calculate the percent changes for each drug

# Display the data to confirm


# In[ ]:





# In[20]:


# Store all Relevant Percent Changes into a Tuple


# Splice the data between passing and failing drugs


# Orient widths. Add labels, tick marks, etc. 


# Use functions to label the percentages of changes


# Call functions to implement the function calls


# Save the Figure


# Show the Figure
fig.show()


# In[ ]:





# In[ ]:




