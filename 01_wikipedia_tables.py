import pandas as pd

pd.set_option('display.max_columns', None)
link = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
lst_sp500 = pd.read_html(link)
print('pd.read_html type: ', type(lst_sp500))
print('lst_sp500 len: ', len(lst_sp500))
df_sp500 = lst_sp500[0]
df_sp500_changes = lst_sp500[1]
print('shape: list[0]={}, list[1]={}'.format(df_sp500.shape, df_sp500_changes.shape))
print('df_sp500.info-->')
print(df_sp500.info())
print('\ndf_sp500.head--> \n{}'.format(df_sp500.head(5)))
# print('\ndf_sp500.sample--> \n{}'.format(df_sp500.sample(5)))
# df_sp500_changes.columns = df_sp500_changes.columns.map('_'.join)
print('df_sp500_changes.info-->')
print(df_sp500_changes.info())
print('\ndf_sp500_changes.sample--> \n{}'.format(df_sp500_changes.sample(5)))

link = 'https://en.wikipedia.org/wiki/Global_Industry_Classification_Standard'
lst_gics = pd.read_html(link)
print('pd.read_html type: ', type(lst_gics))
print('lst_gics len: ', len(lst_gics))
df_gics = lst_gics[0]
print('df_gics.info-->')
print(df_gics.info())
print('\ndf_gics.head--> \n{}'.format(df_gics.head(5)))
