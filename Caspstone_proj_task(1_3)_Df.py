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
df=pd.read_csv("E:\\Excel sheet\\Eduonix_projects\\Road-Accidents-India-Analysis\\accident_Databases\\roadAccStats13-16(new).csv")
# print(df.head())
# print(df.shape)
# print(df.describe())
# print(df.info())
# print(df.isnull().sum())

                                     # Task 1 done in excel file

                                        # ( Pie Chart)  ------>     # 1st method
# plt.figure(figsize=(10,12))
# labels = ['Road Acc. 2013','Road Acc. 2014','Road Acc. 2015','Road Acc. 2016']
# sizes = df.iloc[:,-4:].max().values
# colors = ['c','b','r','m']
# textpros= {'fontsize':15}
# wedgeprops = {'linewidth': 2, 'width': 1, 'edgecolor': 'k'}
# plt.pie(sizes,labels=labels,colors=colors,autopct='%0.2f%%',startangle=45,wedgeprops=wedgeprops,textprops=textpros,
#         labeldistance=1.2)
# plt.legend()
# plt.savefig('E:\Excel sheet\Eduonix_projects\Road-Accidents-India-Analysis\Dbase_image_mine\question_1.png')
# plt.show()


                                       # Task_1, 2nd Method
# plt.figure(figsize=(10,12))
# labels = ['Road Acc. 2013','Road Acc. 2014','Road Acc. 2015', 'Road Acc. 2016']
# columns = ['percentage of road acc. in 2013','percentage of road acc. in 2014',
#            'percentage of road acc. in 2015','percentage of road acc. in 2016']
# sizes = df[columns].max().values
# colors = ['c','b','r','m']
# textpros= {'fontsize':15}
# wedgeprops = {'linewidth':2,'width':1,'edgecolor':'k'}
# plt.pie(sizes,labels=labels,colors=colors,autopct='%0.2f%%',startangle=45,
#         textprops=textpros,labeldistance=1.2,wedgeprops=wedgeprops)
# plt.legend()
# plt.show()


                                  # Task 2 ( Mean accisents per 1 lakh population for each year)

# mean1 = df['Total Number of Accidents Per Lakh Population - 2014'].mean()
# mean2 = df['Total Number of Accidents Per Lakh Population - 2013'].mean()
# mean3 = df['Total Number of Accidents Per Lakh Population - 2015'].mean()
# mean4 = df['Total Number of Accidents Per Lakh Population - 2016'].mean()

                                # create pie plot
# data = [mean1,mean2,mean3,mean4]
# labels = ['Mean of Total acc./Lakh 2013','Mean of Total acc./Lakh 2014',
#           'Mean of Total acc./Lakh 2015','Mean of Total acc./Lakh 2016']
# colors = ['c','m','y','g']
# textpros= {'fontsize':8}
# wedgeprops = {'linewidth':2,'width':1,'edgecolor':'k'}
# plt.pie(data,labels=labels,colors=colors,autopct='%0.2f%%',startangle=45,
#         textprops=textpros,labeldistance=1.1,wedgeprops=wedgeprops)
# plt.legend()
# plt.savefig('E:\Excel sheet\Eduonix_projects\Road-Accidents-India-Analysis\Dbase_image_mine\question_2.png')
# plt.show()


                     # TAsk 3 (Highest no. of accidents state and least no. of accidents state)

# accidents_by_state=(df.groupby('States/UTs')['Total Number of Accidents Per Lakh Population - 2013'].sum())
# maxi_acc_state=accidents_by_state.idxmax()
# mini_acc_state=accidents_by_state.idxmin()
# print(maxi_acc_state)
# print(mini_acc_state)

accidents_by_state=(df.groupby('States/UTs')['Total Number of Accidents Per Lakh Population - 2013'].sum())
maxi_acc_state=accidents_by_state.idxmax()
mini_acc_state=accidents_by_state.idxmin()
print(maxi_acc_state)
print(mini_acc_state)
#
# high_acc = df.iloc[:,-4:].max().values
# least_acc = df.iloc[:,-4:].min().values
