import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_table('gal_#2041.txt', delim_whitespace=True)
df.columns = ['x','y','uJAVA', 'gSDSS', 'iSDSS', 'zSDSS', 'J0378', 'J0395',
             'J0410', 'J0430', 'J0515', 'J0660', 'J0861', 'rSDSS']

df[df.iSDSS > 0.0].head()
df[(df.gSDSS - df.rSDSS) > 0.].head()
df['uJAVA'].describe()
df['uJAVA'][df.uJAVA > 0.2].describe()


df2 = df.ix[:,:2]
#OU
df2 = df.ix[:, ('x','y')]

df3 = df.ix[:,('rSDSS','gSDSS', 'iSDSS', 'zSDSS')]
#OU
df3 = df.ix[:,(13,3,4,5)]

df3.head()

#o join() eh a opcao correta, pois iremos unir dois dataframes que nao possuem
#colunas em comum.
df4 = df2.join(df3)


df5 = df.ix[:,(0,1,3)]
#OU
df5 = df.ix[:, ('x','y', 'gSDSS')]

df6 = df.ix[:,('x','y','rSDSS','iSDSS', 'zSDSS')]
#OU
df6 = df.ix[:,(0,1,13,4,5)]

#o merge() eh a opcao correta, pois iremos unir dois dataframes que possuem
#coluna(s) em comum
df7 = pd.merge(df5,df6)
