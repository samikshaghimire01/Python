import pandas as pd
import numpy as np

# 1️ Drop columns with >20% missing
def qn1():
    df = pd.DataFrame({
        "A":[1,2,np.nan,np.nan],
        "B":[1,2,3,4],
        "C":[np.nan,np.nan,np.nan,4]
    })
    thresh = 0.8*len(df)
    df_clean = df.dropna(axis=1, thresh=thresh)
    print("Q1:\n", df_clean)


# 2️ Groupby transform to percentage of group total
def qn2():
    df = pd.DataFrame({
        "Group":["X","X","Y","Y"],
        "Value":[10,30,20,80]
    })
    df['Percent'] = df['Value'] / df.groupby('Group')['Value'].transform('sum') * 100
    print("Q2:\n", df)


# 3️ Reshape wide to long using melt
def qn3():
    df = pd.DataFrame({
        "ID":[1,2],
        "Math":[80,90],
        "Science":[70,85]
    })
    long = pd.melt(df, id_vars='ID', var_name='Subject', value_name='Marks')
    print("Q3:\n", long)


# 4️ Extract day of week from datetime & find highest average sales
def qn4():
    df = pd.DataFrame({
        "Date": pd.to_datetime(["2024-01-01","2024-01-02","2024-01-03","2024-01-01"]),
        "Sales":[100,150,200,50]
    })
    df['Weekday'] = df['Date'].dt.day_name()
    avg_sales = df.groupby('Weekday')['Sales'].mean()
    best_day = avg_sales.idxmax()
    print("Q4 Weekday with highest avg sales:", best_day)


# 5️ Merge DataFrames with different column names
def qn5():
    df1 = pd.DataFrame({"EmpID":[1,2],"Name":["A","B"]})
    df2 = pd.DataFrame({"ID":[1,2],"Salary":[50000,60000]})
    merged = pd.merge(df1, df2, left_on='EmpID', right_on='ID')
    print("Q5:\n", merged)


# 6️ Bin age into labeled groups
def qn6():
    df = pd.DataFrame({"Age":[5,15,25,65]})
    bins = [0,12,19,59,100]
    labels = ['Child','Teen','Adult','Senior']
    df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)
    print("Q6:\n", df)


# 7️ Detect and remove duplicates on subset
def qn7():
    df = pd.DataFrame({
        "Name":["A","B","A","C"],
        "Age":[20,21,20,22]
    })
    df_clean = df.drop_duplicates(subset=['Name'])
    print("Q7:\n", df_clean)


# 8️ Apply custom function to grouped DataFrame
def qn8():
    df = pd.DataFrame({
        "Group":["X","X","Y","Y"],
        "Value":[10,30,20,80]
    })
    def rng(x): return x.max() - x.min()
    df_range = df.groupby('Group')['Value'].apply(rng)
    print("Q8:\n", df_range)


# 9️ Pivot table & reverse using stack
def qn9():
    df = pd.DataFrame({
        "Dept":["IT","IT","HR","HR"],
        "Gender":["M","F","M","F"],
        "Salary":[50000,60000,55000,65000]
    })
    pivot = pd.pivot_table(df, values="Salary", index="Dept", columns="Gender")
    stacked = pivot.stack()
    print("Q9 Pivot:\n", pivot)
    print("Stacked:\n", stacked)


# 0️ Chain 4 Pandas operations
def qn10():
    df = pd.DataFrame({
        "Dept":["IT","IT","HR","HR","IT","HR"],
        "Employee":["A","B","C","D","E","F"],
        "Salary":[50000,60000,55000,65000,70000,72000]
    })
    result = (df[df['Salary']>55000]      
                .groupby('Dept')           
                ['Salary']                 
                .agg(['mean','max'])      
                .sort_values('mean', ascending=False))  
    print("Q10:\n", result)

qn1()
qn2()
qn3()
qn4()
qn5()
qn6()
qn7()
qn8()
qn9()
qn10()