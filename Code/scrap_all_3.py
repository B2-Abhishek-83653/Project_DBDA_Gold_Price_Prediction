import pandas as pd
import numpy as np
import yfinance as yf
import time

current_date = time.strftime("%Y-%m-%d", time.localtime())
print(current_date)

one_more_month = [1, 3, 5, 7, 8, 10, 12]
# for year in range(2000,2025):
#     for month in range(1,13):
#         for day in range(1,32):
all_dates = []
for year in range(2024, 2025):
    # print(year,end=": ") #Debugging_2_4
    for month in range(1, 13):
        # print(month,end=": ") #Debugging_2_4
        for day in range(1, 32):
            one_more_day = sum(filter(lambda x: x == month, one_more_month))
            if not (one_more_day) and (day == 31):
                # print(f'{date}',end=" ") #Debugging_1_1
                break
            elif (month == 2) and (day == 30):
                break
            elif (month == 2) and (day == 29):
                if (year % 4 == 0):
                    if (year % 100 == 0):
                        if (year % 400 == 0):
                            pass
                        else:
                            break
                    else:
                        pass
                else:
                    break
            if month<10 and day<10:
                date = f'{year}-0{month}-0{day}'
            elif month<10 and not(day<10):
                date = f'{year}-0{month}-{day}'
            elif not(month < 10) and day < 10:
                date = f'{year}-{month}-0{day}'
            else:
                date = f'{year}-{month}-{day}'
            all_dates = all_dates + list([date])
            if date==current_date:
                for i in range(len(all_dates)-1):
                    df = yf.download('GC=F', all_dates[i], all_dates[i+1],interval='1h')

                    # saving the dataframe
                    print(f"{all_dates[i]}:{all_dates[i+1]}")
                    #df.to_csv('../Database/gold_rate_max.csv', mode='a', index=False, header=False)
                    df.to_csv(f'../Database/hourly_individual/{all_dates[i]}.csv', mode='a')
                print("Web Scrapping done!")
                exit(0)
            #print(f'{date}', end=" ")
            # print(day,end=" ") #Debugging_2_4
        # print() #Debugging_2_4

#print(all_dates) #Debugging #read all

# Amount of days possible
#print(len(all_dates))

# Read data

