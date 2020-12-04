import pandas as pd
import re

# Setting Global Settings
"""
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
"""

path_to_csv = 'C:\dev\workspace-vscode\Python\Pandas_learning\.vscode\pokemon_data.csv'

df = pd.read_csv('{}'.format(path_to_csv))
# df = pd.read_xlsx('path/to/file')
# df = pd.read_csv('path/to/file', delimiter='\t')

"""
                                                            ::: Manipulating the Data :::

print(df.head(3))  # prints top 3 rows
print(df.columns)  # prints column headers/titles
print(df[['Name', 'Type 1', 'HP']])  # get all values of a single column
print(df['Name'][0:5])  # gets all names of pokemon 0-5
print(df[['Name', 'Type 1]])  # <-- method of returning multiple columns
print(df.iloc[69])  # get value of the 69th row
print(df.iloc[0:4])  # gets values of multiple rows
print(df.iloc[1, 1])  # gets values of the first row, first column
print(df.loc[df['Type 1'] == "Fire"])  # returns all rows where column 'Type 1' is equal to 'Fire'
print(df.describe())  # provides useful/general statistical data 
print(df.sort_values(['Type 1', 'Speed'], ascending=[1, 0]))  
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']  # Adds a new column titled 'Total', which adds values from the other columns
df = df.drop(columns=['Total'])  # Proper way to drop columns from the data set
df['Total'] = df.iloc[:, 4:10].sum(axis=1)  # more concise way of creating a new column that adds from other columns
"""

"""
                                                            ::: Saving the Data/Changes :::
df.to_csv('Modified.csv', index=False)  # save changes, index=False removes the index column which can be annoying to have
df.to_excel('Modified.xlsx', index=False)  # same as above, but saved as an excel file
df.to_csv('Modified.txt', index=False, sep='\t')  # same as above, but saved as a .txt file and denotes that the delimiter is a tab
"""

"""
                                                            ::: Filtering Data :::
df.loc[(df['Type 1'] == 'Fire') & (df['Type 2'] == 'Flying')]
df.loc[df['Name'].str.contains('^ch[a-z]*', flags=re.I, regex=True)]
"""

"""
                                                            ::: Statistics :::
df.groupby(['Type 1'])  # simple grouping method
df.groupby(['Type 1']).mean()  # simple averaging based on the grouping
df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False)  # simple averaging based on the grouping, ordered by 'Attack'
df.groupby(['Type 1', 'Type 2']).count()['#']  # simple way to count x of y of something
"""





