import pandas as pd

read_file = pd.read_excel (r'C:\Users\91982\Downloads\covid_all_data.xlsx')
read_file.to_csv (r'D:\NSE DATA\covid_data_project.csv', index = None, header=True)