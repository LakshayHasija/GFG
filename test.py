import pandas as pd
from ydata_profiling import ProfileReport as pp
dic={}
for i in range(1,11):
    l=[]
    for j in range((i*10)-9,(i*10)+1):
        # print(i,j)
        l.append(j)
    # print(l)
    dic[i]=l
    print(dic)
    # l.clear()
    print(dic)

df=pd.DataFrame(dic)
profile = pp(df, title="Pandas Profiling Report", explorative=True)

# Save the report to an HTML file
profile.to_file("profile_report.html")