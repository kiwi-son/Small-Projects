import pandas as pd
from pymongo import MongoClient
from datetime import datetime
from datetime import datetime
dt=datetime.now()
client=MongoClient("mongodb://localhost:27017/")
db=client['Shiftschedule']
name=input("Enter your name")
if name in db.list_collection_names():
    print("Collection already exists")

else:
    db.create_collection(name)
    print("Collection created")
    coll=db[name]
    emp=int(input("Enter your employee no."))
    df=pd.read_excel("shift.xlsx",sheet_name=-1)
    pos=df[(df.iloc[:,1]==name) & (df.iloc[:,2]==emp)].index.tolist()
    if len(pos)==0:
        print("Entered wrong details")
    else:
        a=pos[0]
        shift=""
        l=df.iloc[a,10:]
        for i,j in enumerate(l):
            if j!='L' and j!='//':
                shift=j
                col1=df.iloc[:,i+10]
                k=col1[col1==shift].index.to_list()
                manpower=[]
                for b in k:
                    print(df.iloc[b,1], i+1)
                    manpower.append(df.iloc[b,1])
                data={
                "date": datetime(dt.year, dt.month,i+1),
                "manpower": manpower,
                "shift":shift
                }
                coll.insert_one(data)