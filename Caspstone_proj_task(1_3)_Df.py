import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
# import warnings
# warnings.filterwarnings('ignore')
# plt.style.use('dark_background')
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
df=pd.read_excel("E:\\Excel sheet\\Eduonix_projects\\Road-Accidents-India-Analysis\\accident_Databases\\roadAccStats13-16(solved).xlsx")
# print(df.head())
# print(df.shape)
# print(df.describe())
# print(df.info())
# print(df.isnull().sum())

                                     # Task 1 done in excel file

                                  # Task 2 ( Mean accisents per 1 lakh population for each year)

# print(df['Total Number of Accidents Per Lakh Population - 2013'].mean())
# print(df['Total Number of Accidents Per Lakh Population - 2014'].mean())
# print(df['Total Number of Accidents Per Lakh Population - 2015'].mean())
# print(df['Total Number of Accidents Per Lakh Population - 2016'].mean())

                     # TAsk 3 (Highest no. of accidents state and least no. of accidents state)

# for state,accidents in zip(df['States/UTs'],df['Total Number of Accidents Per Lakh Population - 2013']):
    # if accidents==max(accidents):
    #     print(f"{state}:{accidents}")
    # print(max(accidents))
# accidents_by_state=(df.groupby('States/UTs')['Total Number of Accidents Per Lakh Population - 2013'].sum())
# maxi_acc_state=accidents_by_state.idxmax()
# mini_acc_state=accidents_by_state.idxmin()
# print(maxi_acc_state)
# print(mini_acc_state)

