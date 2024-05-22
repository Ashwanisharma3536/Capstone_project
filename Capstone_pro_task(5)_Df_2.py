import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
plt.style.use('dark_background')
# pd.set_option('display.max_rows',None)
# pd.set_option('display.max_columns',None)
df=pd.read_csv("E:\\Excel sheet\\Eduonix_projects\\Road-Accidents-India-Analysis"
               "\\accident_Databases\\Persons_killed_due_to_Non-use_of_Safety_Device_2016.csv")
print(df.shape)
# print(df.head())
# print(df.describe())
# print(df.info())
print(df.isnull().sum().sum())
print(df.isnull().sum())

                               # Task 5
# male_percentage = sum(df['Non-wearing of Helmet - Male'])*100/sum(df['Non-wearing of Helmet - Total'])
# female_percentage = sum(df['Non-wearing of Helmet - Female'])*100/sum(df['Non-wearing of Helmet - Total'])
# print(round(male_percentage,2))
# print(round(female_percentage,2))

