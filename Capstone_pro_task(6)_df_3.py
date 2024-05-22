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
df=pd.read_csv("E:\\Excel sheet\\Eduonix_projects\\Road-Accidents-India-Analysis\\accident_Databases\\accidents03-16(solved).csv")
print(df.shape)
# print(df.head())
# print(df.describe())
# print(df.info())
print(df.isnull().sum())


                         # Solved in excel sheet