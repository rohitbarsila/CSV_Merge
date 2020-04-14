import pandas as pd
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir('./files') if isfile(join('./files', f))]
data=[]
with pd.ExcelWriter("merge.xlsx") as writer:
    for i  in range(1,6):
        day=[]
        for df1 in onlyfiles:
            df = pd.ExcelFile( './files/'+df1)
            dfs = {sheet_name: df.parse(sheet_name) for sheet_name in df.sheet_names}
            dff=pd.DataFrame(dfs['Day'+str(i)])
            day.append(dff.loc[dff['Ignite_Id'] == df1.split('.')[0]])

        appended_df = pd.concat(day)
        appended_df.to_excel(writer, sheet_name='Day'+str(i))
    writer.save()
