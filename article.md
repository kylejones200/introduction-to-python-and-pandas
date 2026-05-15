---
author: "Kyle Jones"
date_published: "February 28, 2025"
date_exported_from_medium: "November 10, 2025"
canonical_link: "https://medium.com/@kyle-t-jones/introduction-to-python-and-pandas-4ea7346aaf3e"
---

# Introduction to Python and Pandas Python is a widely-used high-level programming language known for its
readable syntax and versatility. It supports multiple programming...

### Introduction to Python and Pandas for Analytics 

Python is a widely-used high-level programming language known for its readable syntax and versatility. It supports multiple programming paradigms, including object-oriented, imperative, functional, and procedural programming styles. Python's dynamic typing and automatic memory management simplify development, making it a go-to language for data analysis and scientific computing.

Pandas, built on top of NumPy, is an open-source data manipulation and analysis library that offers high-performance, easy-to-use data structures like Series and DataFrames. These structures allow efficient handling of structured data, resembling columns in spreadsheets or tables in SQL databases.

Let's start by importing the necessary libraries:

```python
import pandas as pd
import numpy as np


print('Pandas Version:', pd.__version__)
```
### Basics of Python Programming 

### Getting Started with Python
Python emphasizes readable and straightforward syntax. It uses whitespace indentation instead of curly braces or keywords to define code blocks, making it intuitive and easy to learn.

Let's begin with the classic 'Hello World' example:

``` 
print('Hello World')
```

You can also use variables to store and print values:

``` 
word_to_print = "Hello World"
print(word_to_print)
```

### Data Types in Python
Python supports several basic data types:

- String: Textual data enclosed in quotes.
- Integer: Whole numbers.
- Float: Decimal numbers.
- Boolean: True or False values.
- List: Ordered and mutable collection of items.
- Dictionary: Key-value pairs.

``` 
# Strings
name = "Alice"
print(type(name))  # Output: <class 'str'>


# Integers
age = 30
print(type(age))  # Output: <class 'int'>


# Floats
height = 5.9
print(type(height))  # Output: <class 'float'>


# Lists
fruits = ['apple', 'banana', 'cherry']
print(type(fruits))  # Output: <class 'list'>


# Dictionary
person = {'name': 'Alice', 'age': 30}
print(type(person))  # Output: <class 'dict'>
```

### Control Structures
Python uses straightforward syntax for control structures like loops and conditionals.

#### If-Else Statements
``` 
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

#### For Loops and While Loops
``` 
# For Loop
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)


# While Loop
count = 0
while count < 3:
    print(count)
    count += 1
```
### Introduction to Pandas 

Pandas provides two primary data structures:

- Series: One-dimensional labeled array.
- DataFrame: Two-dimensional labeled data structure with columns of potentially different types.

### Pandas Series
A Pandas Series is like a column in a spreadsheet or a single column in a DataFrame.

```python
# Creating a Series from a list
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("Pandas Series:\n", s)
```

```python
# Creating a Series from a dictionary
d = {'a': 100, 'b': 200, 'c': 300}
s2 = pd.Series(d)
print("Series from dictionary:\n", s2)
```
### Creating Pandas DataFrames 

A DataFrame is a two-dimensional labeled data structure with columns of potentially different types.

```python
# Creating a DataFrame from a dictionary
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)
```

```python
# Creating a DataFrame from a list of dictionaries
data_list = [
    {'Name': 'Tom', 'Age': 25, 'City': 'Tokyo'},
    {'Name': 'Emma', 'Age': 31, 'City': 'Sydney'}
]
df2 = pd.DataFrame(data_list)
print("\nDataFrame from list of dicts:\n", df2)
```
### Basic DataFrame Operations 

### Selecting and Querying Data
You can select columns using bracket notation and rows using `loc` or `iloc`.

``` 
# Selecting a column
print("Ages:\n", df['Age'])


# Selecting a row by label
print(df.loc[0])


# Selecting a row by position
print(df.iloc[0])


# Querying a DataFrame
print(df.query("Age > 30"))
```
### Modifying DataFrames 

``` 
# Adding a new column
df['Salary'] = [50000, 60000, 55000, 65000]
print("\nDataFrame with new column:\n", df)


# Filtering data
high_salary = df[df['Salary'] > 55000]
print("\nHigh salary employees:\n", high_salary)


# Dropping a column
df = df.drop(columns=['Salary'])
print("\nDataFrame after dropping column:\n", df)
```
### Grouping and Aggregation 

``` 
# Grouping data and performing aggregations
avg_age_by_city = df.groupby('City')['Age'].mean()
print("\nAverage age by city:\n", avg_age_by_city)
```
### Working with DataFrames 

### File I/O
Pandas makes it easy to read and write data from various file formats.

#### Reading CSV Files
``` 
df_csv = pd.read_csv('data/MER_T02_01.csv')
print(df_csv.head())
```

#### Reading Excel Files
``` 
df_excel = pd.read_excel('data/EnergyData.xlsx', sheet_name='after2000')
print(df_excel.head())
```

#### Writing to CSV
``` 
df.to_csv("data/output.csv")
```
### Handling Missing Data 

``` 
# Check for missing values
print(pd.isnull(df))


# Drop rows with missing values
print(df.dropna(how="any"))
```
### DataFrame Functions and Transformations 

``` 
# Apply function to each row
df['Year'] = df.apply(lambda row: str(row['Age'])[:4], axis=1)


# Convert to datetime
df['Year'] = pd.to_datetime(df['Year'])


# Descriptive statistics
print(df.describe())


# Value counts
print(df['City'].value_counts())
```
### Visualization with Pandas 

Pandas integrates well with Matplotlib for quick data visualizations.

```python
import matplotlib.pyplot as plt


# Histogram
df['Age'].hist(bins=20)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()
```
### Advanced Topics 

### Joins and Merges
``` 
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3']})
df2 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7']}, index=[2, 3, 6, 7])
print(df1.join(df2, how="inner"))
```

### Copy vs. Deep Copy
``` 
df2 = df.copy(deep=True)  # Create a deep copy
```

### Pickling DataFrames
``` 
df.to_pickle("data.pkl")
df_new = pd.read_pickle("data.pkl")
```
### Conclusion 

This guide covers the fundamentals of Python and Pandas, equipping you with the tools to manipulate and analyze data efficiently. From basic operations to advanced data transformations, mastering Pandas enhances your productivity and allows you to gain deeper insights from your data.
