# -*- coding: utf-8 -*-
"""Copy of nit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vJzqCm7K7eOl4SyMsZ1B5wDpPTHRfF-N
"""

import csv
with open('employee_file2.csv') as csv_file:#open the file and save in csv_file
    csv_reader = csv.reader(csv_file,delimiter=',')#read and store in csv_reader
    line_count = 0
    for row in csv_reader:#using loops to read entire file
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')#to display heading
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')#to display entries
            line_count += 1
    print(f'Processed {line_count} lines.')#no of lines proceeded in file

import csv
#opens file in write mode
with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']#headings for file
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()#write the headings for fieldname given
    writer.writerow({'emp_name': 'gokul', 'dept': 'ise', 'birth_month': 'september'})#write entries in specific heading
    writer.writerow({'emp_name': 'arthi', 'dept': 'IT', 'birth_month': 'september'})
    writer.writerow({'emp_name': 'Sanjana', 'dept': 'IT', 'birth_month': 'February'})
    writer.writerow({'emp_name': 'Nithu', 'dept': 'cse', 'birth_month': 'october'})
    writer.writerow({'emp_name': 'sri', 'dept': 'ise', 'birth_month': 'october'})
    writer.writerow({'emp_name': 'pradeep', 'dept': 'ise', 'birth_month': 'june'})
    n=int(input("how many entries you need to make :"))
    for i in range(0,n):#no of entries neede to be entered by user to save in file
      writer.writerow({'emp_name': input("enter the name:"), 'dept':input("enter the dept:"), 'birth_month':input("enter the month:")})

import csv
import pandas as pd#importing pandas
col_list = ["emp_name", "dept","birth_month"]#headings in file
name=input("enter the detail you need to know :")#name we need to be check
df = pd.read_csv("employee_file2.csv", usecols=col_list)#read the file as dataframe
flag=0
 
 
for i in range(len(df)):
  #print(df.loc[i,"emp_name"])
  flag=flag+1
  if(name==df.loc[i, "emp_name"]):#check the name in employee column using dataframe location
    print("it is in",flag,"th row",end=" ")
    print("1st column")
  if(name==df.loc[i, "dept"]):#check the department  in dept column using dataframe location
    print("it is in",flag,"th row",end=" ")
    print("2nd column")
  if(name==df.loc[i, "birth_month"]):#check the month in birth  column using dataframe location
    print("it is in",flag,"th row",end=" ") 
    print("3rd column")

!jupyter nbconvert nit.ipynb