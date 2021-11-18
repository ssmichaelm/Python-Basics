# Michael Moreland - Smoothstack, Python basics 7; 11/18/2021

import pandas as pd

df = pd.read_csv('2_pandas_Salaries.csv')

#1. Check and display the head of the DataFrame.
print("\n1. Check and display the head of the DataFrame")
print(df.head().to_string())

#2. Use the .info() method to find out how many entries there are.
print("\n2. Use the .info() method to find ouw how many entries there are")
print(f"verbose=False\n{df.info(verbose=False)}\n")
print(f"verbose=True\n{df.info(verbose=True)}")

#3. What is the average of first 10000 items in BasePay?
print("\n3. What is the average of first 10000 items in BasePay?")
temp = df['BasePay'].head(10000).mean()
print(f"Average of first 10000 items in BasePay: {temp}\n")

#4. What is the highest amount of TotalPayBenefits in the dataset?
print("\n4. What is the highest amount of TotalPayBenefits in the dataset?")
tpbmax = df['TotalPayBenefits'].max()
print(f"Highest amount in TotalPayBenefits: {tpbmax}\n")

#5. What is the job title of JOSEPH DRISCOLL?
print("\n5. What is the job title of JOSEPH DRISCOLL?")
temp = df.set_index('EmployeeName').loc['JOSEPH DRISCOLL']
print(f"Joseph Driscoll's job title: {temp['JobTitle']}\n")

#6. How much does JOSEPH DRISCOLL make (including benefits)?
print("\n6. How much does JOSEPH DRISCOLL make (including benefits)?")
print(f"Joseph Driscoll makes: {temp['TotalPayBenefits']}\n")

#7. What is the name of highest paid person (including benefits)?
print("\n7. What is the name of highest paid person (including benefits)?")
temp = df.set_index('TotalPayBenefits')
print(f"Highest paid person: {temp.loc[tpbmax]['EmployeeName']}\n")

#8. What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?
print("\nWhat is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?")
print(f"Lower paid person: {temp.loc[df['TotalPayBenefits'].min()]['EmployeeName']}")
print(f"{temp.loc[df['TotalPayBenefits'].min()]['EmployeeName']} has negative pay, implying he is in debt.\n")

#9. What was the average (mean) TotalPay of all employees per year? (2011-2014)?
print("\n9. What was the average (mean) TotalPay of all employees per year? (2011-2014)?")
temp = df.groupby(['Year'])['TotalPay'].mean()
print(f"Average TotalPay of all employees yearly:\n{temp}\n")

#10. How many unique job titles are there?
print("\n10. How many unique job titles are there?")
temp = df['JobTitle'].nunique()
print(f"Unique job titles: {temp}\n")

#11. What are the top 7 most common jobs?
print("\n11. What are the top 7 most common jobs?")
temp = df['JobTitle'].value_counts().head(7)
print(f"Top 7 most common jobs:\n{temp}\n")

#12. How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?)
print("\n12. How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?)")
temp = (df[df['Year'] == 2013]['JobTitle'].value_counts() == 1).sum()
print(f"Job Titles with only one occurrence in 2013: {temp}\n")

#13. How many people have the word Chief in their job title? (This is pretty tricky)
print("\n13. How many people have the word Chief in their job title? (This is pretty tricky)")
temp = (df['JobTitle'].apply(lambda s: ('chief' in s.lower()))).sum()
print(f"People who have the word 'chief' in their job title: {temp}\n")

#14. Is there a correlation between length of the Job Title string and Salary?
print("\n14. Is there a correlation between length of the Job Title string and Salary?")
print("There is not a correlation between the job title length and salary.")