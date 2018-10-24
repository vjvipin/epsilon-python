
import pandas as pd
import numpy as np
ser1 = pd.Series(data=[1,2,3,4,5], index=list('abcde'))
ser2 = pd.Series(data=[11,22,33,44,55], index=list('abcde'))
# compbine series to make DF
df = pd.DataFrame({'A':ser1, 'B':ser2})

# create a DF of random numbers
df = pd.DataFrame(data=np.random.randint(1,10,size=(10,10)), index=list('ABCDEFGHIJ'), columns=list('abcdefghij'))

# loading CSV
hr_data = pd.read_csv('https://raw.githubusercontent.com/zekelabs/data-science-complete-tutorial/master/Data/HR_comma_sep.csv.txt')

#print(hr_data)
hr_data.info()
hr_data.head()
hr_data.tail()
hr_data.describe()
hr_data.salary.value_counts()

#Accessing subset of data - rows, columns, filters¶
#Get all columns with categorical values

cat_cols_data = hr_data.select_dtypes('object')
cat_cols_data.head()
#rename column names
hr_data.rename(columns={'sales':'department'},inplace=True)
hr_data.columns
hr_data[['satisfaction_level','last_evaluation','number_project']].head()


hr_data_itr = pd.read_csv('https://raw.githubusercontent.com/zekelabs/data-science-complete-tutorial/master/Data/HR_comma_sep.csv.txt', chunksize=5000)

for hr_data in hr_data_itr:
    print (hr_data.info())



movie_data = pd.read_json('https://raw.githubusercontent.com/zekelabs/data-science-complete-tutorial/master/Data/movie.json.txt')

print(movie_data)
#Access data by index values
movie_data.loc['Scarface']
movie_data.loc['Scarface':'Vertigo']
movie_data.iloc[1]
movie_data.iloc[1:4]
# Filtering rows based on conditions

movie_data[ (movie_data['Adam Cohen'] > 3)]
movie_data[ ((movie_data['Adam Cohen'] > 3) & (movie_data['David Smith'] > 4))]

