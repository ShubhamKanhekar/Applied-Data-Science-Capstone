import pandas as pd
import plotly.express as px
df= pd.read_csv('spacex_launch_dash.csv')
# print(df[['Launch Site','Booster Version']].groupby('Launch Site').count())
# print(df.columns)

# print(df[['Launch Site','class']].groupby('Launch Site').mean('class').reset_index())
# print(df['Launch Site'].value_counts().reset_index())




'''
ent='VAFB SLC-4E'
temp_df= df[['Launch Site', 'class', 'Booster Version']].groupby(['Launch Site','class']).count().reset_index()
# fig=px.pie(temp_df, values=temp_df['class'], names=ent, title='Demo pie chart')
# fig.show()
# print(indexes)

print(temp_df)
indexes=[]
count=0
for i in range(temp_df.shape[0]):
    if temp_df.iloc[i,0]==ent:
        indexes.append(count)
    count+=1


print(indexes)
# print(temp_df.iloc[indexes,:])
'''


# ent='VAFB SLC-4E'
# site_df=df.loc[df['Launch Site']==ent]


print(df.loc[df['Flight Number'].isin(range(*[0,10]))])
