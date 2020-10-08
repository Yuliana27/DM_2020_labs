import pandas as pd
import KN311Лаврик2 as vz
import matplotlib.pyplot as plt


def date(df_column):  
    df_column = df_column.radd('2019-')
    df_column = pd.to_datetime(df_column, format='%Y-%d.%b').apply(lambda x: x.strftime(r'%d.%m.%Y'))    
    return df_column

def time(df_column):  
    df_column = pd.to_datetime(df_column).apply(lambda x: x.strftime(r'%H:%M:%S'))
    return df_column

def to_int(df_column, x):
    df_column = pd.to_numeric(df_column.str[:x], downcast='integer')
    return df_column

def to_float(df_column):
    df_column = pd.to_numeric(df_column.str.replace(',', '.'))
    return df_column

def function_parse(df):
    df['day/month'] = date(df['day/month'])
    df['Time'] = time(df['Time'])
    df['Wind Speed'] = to_int(df['Wind Speed'], -4)
    df['Wind Gust'] = to_int(df['Wind Gust'], -4)
    df['Humidity'] = to_int(df['Humidity'], -1)
    df['Pressure'] = to_float(df['Pressure'])
    return df

dataframe = pd.read_csv('DATABASE.csv', delimiter=';')

function_parse(dataframe) 

print('Enter number of graphs :') 
number_of_graphs=int(input())
print('Enter name(-s) of column(-s): ') 
columns=[]
for i in range(number_of_graphs):
    column=input() 
    columns.append(column)

print('\n')    
print('If you want to review data for a specific day, enter desired day in the format d.m.y (or enter No)\nP.S. date interval: 16.07.2019-13.08.2019')
answer=input()
if answer=='No':    
    dataframe.set_index('day/month', inplace=True)
    for i in columns:
        vz.data_for_wholeperiod(dataframe, i)
    vz.create()
else:
    dataframe2 = dataframe.loc[dataframe['day/month'] == answer]
    dataframe2.set_index('Time', inplace=True)
    for i in columns:
        vz.data_for_specificday(dataframe2, i)
    vz.create()  


#dataframe['Temperature'].plot.hist(alpha=0.5)
#dataframe['Temperature'].plot.box()
#dataframe['Wind Gust'].plot.bar()
