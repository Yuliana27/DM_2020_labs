# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def data_for_wholeperiod(df, column):
    if  column == 'Precip.' or column == 'Precip Accum':
        df[column].plot(color = 'red')
        plt.ylabel(column)
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(color = 'black',linewidth = 0.5)  
    elif column == 'Dew Point':
        df[column].plot.area()
        plt.ylabel(column)
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(color = 'black',linewidth = 0.5)
    else:
        plt.scatter(x = df.index.values ,y = df[column], label=column)
        plt.xticks(rotation=45)
        plt.ylabel(column)
        plt.legend()
        plt.grid(color = 'black',linewidth = 0.5)
        
def data_for_specificday(df,column):
    if column == 'Dew Point' or column == 'Humidity':
        df[column].plot.area()
        plt.ylabel(column)
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(color = 'black',linewidth = 0.5)
    elif column == 'Wind' or column == 'Condition':
        plt.scatter(x = df.index.values ,y = df[column], label=column)
        plt.xticks(rotation=45)
        plt.ylabel(column)
        plt.grid(color = 'black',linewidth = 0.5)
        plt.legend()
    elif column == 'Wind Speed':
        df[column].plot.bar()
        plt.ylabel(column)
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(color = 'black',linewidth = 0.5)
    elif column == 'Wind Gust':
        df[column].plot.bar(color = 'green')
        plt.ylabel(column)
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(color = 'black',linewidth = 0.5)
        #plt.ylim(bottom=0)
    else:
        df[column].plot()
        plt.ylabel(column)
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(color = 'black',linewidth = 0.5)
        #plt.ylim(bottom=0)
    
def create():
    plt.show()
