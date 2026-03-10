
import pandas as pd

# Create a DataFrame from a dictionary
def qn1():
    data = {
        "Name": ["Samiksha", "Pranisha", "Supriya"],
        "Age": [24, 22, 24],
        "Address": [ "Balaju", "Kalanki", "Kalanki"]
    }
    df = pd.DataFrame(data)
    print("Q1:\n", df)


#  Load a CSV file and display first 5 rows
def qn2():
    df = pd.read_csv("employees.csv")  # replace with your file name
    print("Q2:\n", df.head())


# Select specific columns
def qn3():
    data = {
        "Name": ["Samiksha", "Pranisha", "Supriya"],
        "Age": [24, 22, 24],
        "Address": [ "Balaju", "Kalanki", "Kalanki"]
    }
    df = pd.DataFrame(data)
    selected = df[["Name", "Address"]]
    print("Q3:\n", selected)


# Filter rows where column value > given number
def qn4():
    data = {
        "Name": ["Samiksha", "Pranisha", "Supriya"],
        "Age": [24, 22, 24],
    }
    df = pd.DataFrame(data)
    filtered = df[df["Age"] > 23]
    print("Q4:\n", filtered)


# Add new column based on existing column
def qn5():
    data = {
        "Name": ["Samiksha", "Pranisha", "Supriya"],
        "Age": [24, 22, 24],
    }
    df = pd.DataFrame(data)
    df['Age after 2 years'] = df['Age'] + 2
    print("Q5:\n", df)


# Drop rows with missing values
def qn6():
    data = {
        "Name": [None, "Pranisha", "Supriya"],
        "Age": [24, 22, None],
    }
    df = pd.DataFrame(data)
    cleaned = df.dropna()
    print("Q6:\n", cleaned)


# Group by one column and calculate average
def qn7():
    data = {
        
        "Age": [24, 22, 24],
        "Address": [ "Balaju", "Checkpost", "Kalanki"]
    }
    df = pd.DataFrame(data)
    grouped = df.groupby('Address')['Age'].mean()
    print("Q7:\n", grouped)


# Merge two DataFrames on common column
def qn8():
    df1 = pd.DataFrame({
        "ID": [1, 2, 3],
       "Name": ["Samiksha", "Pranisha", "Supriya"],
    })

    df2 = pd.DataFrame({
        "ID": [1, 2, 3],
        "Address": [ "Balaju", "Kalanki", "Kalanki"]
    })

    merged = pd.merge(df1, df2, on="ID")
    print("Q8:\n", merged)


# Convert column to datetime format
def qn9():
    data = {
        "Date": ["2024-01-01", "2024-02-15", "2024-03-10"]
    }
    df = pd.DataFrame(data)
    df["Date"] = pd.to_datetime(df["Date"])
    print("Q9:\n", df.dtypes)


# Create pivot table
def qn10():
    data = {
    'Department': ['HR', 'HR', 'IT', 'IT', 'IT'],
    'Gender': ['M', 'F', 'M', 'F', 'M'],
    'Salary': [50000, 55000, 70000, 72000, 68000]
}

    df_salary = pd.DataFrame(data)

    pivot_table = pd.pivot_table(
    df_salary,
    values='Salary',
    index='Department',
    columns='Gender',
    aggfunc='mean'
)

    print(pivot_table)

# Call functions

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

