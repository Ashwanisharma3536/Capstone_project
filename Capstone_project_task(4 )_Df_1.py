import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
plt.style.use('dark_background')
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
df=pd.read_csv("E:\\Excel sheet\\Eduonix_projects\\Road-Accidents-India-Analysis\\accident_Databases\\Details_of_road_accident_deaths_by_situation_state_2014.csv")
print(df.shape)
# print(df.head())
# print(df.describe())
# print(df.info())
print(df.isnull().sum())

                                     # task 4    ( Done in excel file also)
# print(sum(df['Offenders (Driver/Pedestrian) Died_Male']))
# print(sum(df['Offenders (Driver/Pedestrian) Died_Female']))
# print(sum(df['Offenders (Driver/Pedestrian) Died_Transgender']))
# print(sum(df['Offenders (Driver/Pedestrian) Died_Total']))
# print(sum(df['Victims Died_Male']))
# print(sum(df['Victims Died_Female']))
# print(sum(df['Victims Died_Transgender']))
# print(sum(df['Victims Died_Total']))
#

#



plt.show()