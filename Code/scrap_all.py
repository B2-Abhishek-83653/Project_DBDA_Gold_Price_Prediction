import pandas as pd
import numpy as np
import yfinance as yf

one_more_month=[1,3,5,7,8,10,12]
# for year in range(2000,2025):
#     for month in range(1,13):
#         for day in range(1,32):
all_dates=[]
for year in range(2000,2025):
    # print(year,end=": ") #Debugging_2_4
    for month in range(1,13):
        # print(month,end=": ") #Debugging_2_4
        for day in range(1,32):
            one_more_day = sum(filter(lambda x: x == month, one_more_month))
            if not(one_more_day)and(day==31):
                # print(f'{date}',end=" ") #Debugging_1_1
                break
            elif (month==2)and(day==30):
                break
            elif (month==2)and(day==29):
                if (year%4==0):
                    if(year%100==0):
                        if(year%400==0):
                            pass
                        else:
                            break
                    else:
                        pass
                else:
                    break
	
            date=f'{year}-{month}-{day}'
            all_dates=all_dates+list(date)
            print(f'{date}',end=" ")
            # print(day,end=" ") #Debugging_2_4
        # print() #Debugging_2_4

#Amount of data possible
#print(len(all_dates))

# Read data
#for i in range(len(all_dates)-1):
#    df = yf.download('GC=F', all_dates[i], all_dates[i+1],interval='1m')

    # saving the dataframe
#    df.to_csv('../Database/gold_rate_max.csv', mode='a', index=False, header=False)
