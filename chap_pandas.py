# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 11:39:01 2020

@author: user
"""

# ch-10: pandas

import pandas as pd
import numpy as np
import random as r
import string as s

def createcust(N):

    custid = r.sample(range(1000,9999),N)
    phone = r.sample(range(6000000000,9999999999),N)
    gender = ['m']*45 + ['f']*55
    r.shuffle(gender)
    
    chars = list(s.ascii_letters)
    r.shuffle(chars)
    
    # for the convenience, fix the length of name=5
    
    name=[]; email=[]; city=[]; age=[]; gender=[]
    
    domain=['@gmail.com','@yahoo.co.in','@hotmail.com','@mycompany.in',
            '@imarticus.com','@infy.in','@buisness.org']
    
    l_city=['pune','mumbai','chennai','delhi','banglore','kolkata','ahmedabad','jaipur']
    
    for i in range(N):
        rnd = r.randint(0,46)
        cname=''.join(chars[rnd:rnd+5])
        name.append(cname)
      
        # email
        rnd = r.randint(0,len(domain)-1)
        email.append(cname+domain[rnd])
      
        # city
        rnd = r.randint(0,len(l_city)-1)
        city.append(l_city[rnd])
      
        # age
        age.append(r.randint(18,100))
    
    
    # create the dictionary
    d_data={'custid':custid, 'name':name,
                 'age':age,'phone':phone,
                 'email':email,'city':city}
    

    # converting the dictionary into dataframe
    df_data = pd.DataFrame(d_data)

    return(df_data)


# function call to create the customer
customer = createcust(100)

## dimensions of data
customer.shape

# to get the 1st and last 'n' records
customer.head(10)
customer.tail(10)

# get the column names 
customer.columns

# get the data types of the columns
customer.dtypes

## adding new column to pandas
#1) add new column 'gender' with the value 'M' and 'F'

gender = ["M"]*45 + ["F"]*55
r.shuffle(gender)                       # shuffle for random M amd F

customer['gender'] = gender
print(customer)


''' ex1)  Create 2 new columns 
 1) balance -> range(10000,500000) -> decimals=1
 2) credit score -> range(1,800) -> integer'''

import numpy as np

customer['balance'] = np.round(np.random.uniform(10000,500000,100),1)     # uniform for float
customer['credit_score'] = np.random.randint(1,800,100)

print(customer)

                        OR

import random as r

balance = r.sample(range(10000,500000),100)
credit_score = r.sample(range(1,800),100)

customer['balance'] = balance
customer['credit_score'] = credit_score

print(customer)



''' ex2) create column acct_type
# CURR -> current account, SVNG -> saving account, RECR -> recurring diposite, INR -> INR account, DMAT -> demat account, TRD -> trading account
# link every customer with 1 of these account'''

acct_type = ["CURR"]*20 + ["SVNG"]*20 + ["RECR"]*10 + ["INR"]*10 + ["DMAT"]*20 + ["TRD"]*20
r.shuffle(acct_type)

customer['acct_type'] = acct_type
print(customer)
               
                    OR
                    
                    
                    
                    

'''EX3) create 2 more columns '''

#   1) sr_citz -> Y/N

sr_citz = ["Y"]*55 + ["N"]*45
r.shuffle(sr_citz)
customer['sr_citz'] = sr_citz
print(customer)

#  2) priv_cust -> N 

customer['priv_cust'] = 'N'
print(customer)

customer.columns




### remove the columns from pandas

## 1st create some dummy columns
customer['alpha'] = -1
customer['beta'] = 1
customer['descr'] = 'bank customer' 

print(customer)
                                                            # opposite to numpy
customer = customer.drop(['alpha','beta','descr'],axis=1)   # in pandas axis=1 -> column
print(customer)


## rearranging the columns in a particular sequence

cols = ['custid','name','age','sr_citz','gender','phone','email','email','city','acct_type','balance','credit_score','priv_cust']

customer = customer[cols]

customer.head(4)


## summarise the dataset (numeric column)

customer.describe()

## index in pandas


'''# to have the column name as the row id instead of the default number '''
# 'custid' will be new index; and it will not be the part of the column

customer = customer.set_index('custid')
print(customer)
customer.columns             # now custid is not column it becomes row id


# to reset the index

customer =  customer.reset_index()
print(customer)

# to have the 'custid' as the both index and column

customer = customer.set_index('custid',drop=False)
print(customer)


### reset the 'custid' back  

customer = customer.set_index('custid',drop=True)
print(customer)

## change the index name when it is a column name

customer =  customer.reset_index()     # 1st need to reset index (convert row index into column)

customer.index
customer.index.name = "SR.NO"
print(customer)

# to reset the row index
customer = customer.drop(['SR.NO'],axis=1)



'''### adding multiple columns to the dataframe(pandas)
1) cust_since-> 1-20 (numbers in years)
2) cards -> integer(0-4)'''
    
 
c_since = np.random.randint(1,20,100)    
cc = np.random.randint(0,5,100)

customer = customer.join(pd.DataFrame({'cust_since':c_since,'cards':cc}))

print(customer)





customer
# adding multiple column to the dataframe

csince=np.random.randint(1,20,100)
cc=np.random.randint(0,5,100)

customer=customer.join(pd.dataframe({'cust_since':csince,'cards':cc}))

# check the dataframe
customer.head(10)

# adding new rows to pandas
newcust=createcust(75)
newcust.head(5)

# merge the newcust with the existing customers
customer = customer.append(newcust,ignore_index=True)
customer.tail(10)

# check the dimension of the dataframe.this will show the updated count
customer.shape

# write pandas into a csv file
#index=FALSE is to suppress the row number as a column in the file
customer.to_csv("mybankcustomer.csv",index=False)


customer.to_csv("mybankcustomer.csv")

import os
os.getcwd()

help(customer.to_csv)


###########################################

# create pandas from the csv

import panda as pd

# if the file is present in the default workingb directory, then the file cqn be read directly.
# else,specify the full path of the file

path="f:/work/mybankcustomers"
customer=pd.read_csv(path)

customer.head(10)

# check the datatype
customer.dtypes

# how to access a single columns of pandas
customer.custid
customer['custid']

# change the data type
customer.crscore = customer.crscore.astype('int32')
customer.cards = customer.cards.astype('int32')

# select query on pandas
# 1) select * from customer
print(customer)


# ii) select custid,name,age from customer
customer[['custid','name','age']]


# iii) select cards, cust_since,gender,balance from customer
cols=['gender','balance','cards','cust_since']
customer[cols]



# SELECT with conditions [WHERE clause]
# select all the male customers
# select * from customers where gender = "m"


customer[customer.gender=="m"]

# select personal details of all femail customers
# select <> where gender = "f"

cols=['name','age','phone','email','city','gender']
customer[cols][customer.gender=="f"]

# get the account details of senior citizens
cols=['name','acc_type','balance','crscore','cards','age']
customer[cols][customer.age>60]

# how to identify nulls
# returns the count of rows that have null values for each column

customer.isnull().sum()



# get all customers whose acc type is null
customer[customer.acctype.isnull()]

# get customer data where crscore is not null 
customer[customer,crscore.notnull()]

# get the row numbers
customer[customer.cards.isnull()]

# multiple condition
# and/or/not
'''
select * from customer
where city = 'pune' and balance > 25000
'''
# customer.city.unique()
# AND
customer[(customer.city=='pune') & (customer.balance>25000)]
#OR
# select <> from customer where cards > 3 or crscore < 200
cols=['name','cards','crscore','age']
customer[cols][(customer.cards>3) | (customer.crscore<200)]

# NOT !=
# get all the customers whose acct type includes everything except INR
cols=['name','age','acctype','gender']
customer[cols][customer.acctype!='INR']


# GROUP BY
# find the average bank balance of male and female customers
customer.groupby('gender').balance.mean()

# find the average credit score based on the account type
customer.groupby('acctype').crscore.mean()

# IN operator
# get customer details of custid=15454,45686,10318 use some random id from the dataset

custid=[15454,45686,10318]
customer[customer.custid.isin(custid)]

# sorting the dataset
# sort the data by cust id
customer.sort_values('custid')

# sort by multiple column
cols = ['custid','crscore','balance']
customer[cols].sort_values(['crscore','balance'])

# descending order (set ascending = False)
customer.sort_values('custid',ascending=False)

# unique values of a column
customer.city.unique()

# update pandas
# update the nulls
customer.isnull().sum()

# senior citizens
# update customer set sr_citz = "N" WHERE
customer.sr_citz[customer.sr_citz.isnull()] = "N"

# verify the change  -- this should return 0 rows
customer.sr_citz[customer.sr_citz.isnull()]

# cc11 = customer.copy()

import numpy as np
customer.isnull().sum()

##2) updates cards
customer.cards[customer.cards.isnull()] = 0

# verify changes
customer.isnull().sum()

# to save the file into csv (excel)
customer.to_csv("mybankcustomers.csv")

## update the remaining null columns

#3) update gender
 
customer.gender[customer.gender.isnull()] = ["M"]*40 + ["F"]*35 
customer.gender = ["M"]*100 + ["F"] *75


#4) update cust_since
customer.cust_since[customer.cust_since.isnull()] = np.random.randint(1,20,75)

#5) update priv_cust
customer.priv_cust[customer.priv_cust.isnull()] = "N"

#6) update balance
customer.balance[customer.balance.isnull()] = np.round(np.random.uniform(10000,500000,75),1)

#7) update credit_score
customer.credit_score[customer.credit_score.isnull()] = np.random.randint(1,800,75)
  
#8) update acct_type
customer.acct_type[customer.acct_type.isnull()] = ["CURR"]*15 + ["SVNG"]*15 + ["RECR"]*15 + ["INR"]*10 + ["DMAT"]*10 + ["TRD"]*10


# ----------------4/12/2020--------------------

# change the data types

customer.credit_score = customer.credit_score.astype('int32')
customer.cards = customer.cards.astype('int32')

# check the result
customer.dtypes

# more updates
customer


# sr_citz should be "y" for ages > 60; else it is "N"

customer.sr_citz[customer.age>60] = "Y"
customer.sr_citz[customer.age<=60] = "N"
customer.head(25)

# update the privilege customer
# privilege customers are those who have a balance of more than 300000 and a credit score of more than 700


customer.priv_cust[(customer.balance>300000) & (customer.credit_score>800)] = "Y"
 
# verify the change
customer[customer.priv_cust == "Y"]

# used to describe the data customer.balance.describe() function
customer.balance.describe()

# describe the columns of type 'object'
# count(*) - GROUP BY
# gender
customer.gender.value_counts()

# privcust
customer.priv_cust.value_counts()

# acctype
customer.acct_type.value_counts()

# city
customer.city.value_counts()
#srcitz
customer.sr_citz.value_counts()


# update the first 10 customers with the proper names

'sriram','yash','ravindra','jayesh','saloni','shubham','ajit','abhishek','bansi','saurabh',
'nishita'

7800 3397 9722
5976 2791 7432
6025 4177 2449 
9033 2075

customer.name[customer.custid==7800] = 'sriram'
customer.name[customer.custid==3397] = 'yash'
customer.name[customer.custid==9722] = 'ravindra'
customer.name[customer.custid==5976] = 'jayesh'
customer.name[customer.custid==2791] = 'saloni'
customer.name[customer.custid==2222] = 'shubham'
customer.name[customer.custid==2647] = 'ajit'
customer.name[customer.custid==8657] = 'abhishek'
customer.name[customer.custid==1858] = 'bansi'
customer.name[customer.custid==3442] = 'saurabh'
customer.name[customer.custid==2164] = 'nishita'

customer.head(11)


# get the customer id, name, email

cols = ['custid','name','email']
customer[cols].head(11)

# email updatation with the customer name

custids = [7800,3397,9722,5976,2791,2222,2647,8657,1858,3442,2164]
names = customer.name[customer.custid.isin(custids)]
email = customer.email[customer.custid.isin(custids)]


for i in range(len(custids)):
    cid = custids[i]
    cname = names[i]
    em = cname+"@"+email[i].split("@")[1]
    customer.email[customer.custid==cid] = em
    
    print(em)
    
# index (row numbers) : getting the row numbers of pandas

rowids = customer[customer.balance < 25000].index
print(rowids)

# query the pandas using the row number as filter
customer[customer.index.isin(rowids)]

# select the customer details whose row ids is 55
customer[customer.index==55]


# other ways to access pandas
# iloc, loc

# first row all columns
customer.iloc[0]

# select the first 5 rows  and all columns
customer.loc[0:5]

# select rows and columns
# first 10 rows, and first 4 columns
customer.iloc[0:10,0:4]

# all rows first 5 columns
customer.iloc[:,0:5]

# subset
smalldata = customer.iloc[:,0:5]
print(smalldata)

'''
# assignments for practice

# 1) create 2 lists of integers that have 1,2 and 3 digits.multiply every
    1digit num of list 1 with every 1digit num of list 2
    2digit num of list 1 with every 2digit num of list 2
    3digit num of list 1 with every 3digit num of list 2
'''
lis1 = [1,2,3]
lis2 = [1,2,3]
for i in range(0):
    print(
    lis1[0] * lis2[0]
    lis1[1] * lis2[1]
    lis1[2] * lis2[2]
    )



'''
# 2) create a list of 2 numbers (about 20 numbers)
     add every number with its adjacent number and display the result
     eg: [1,2,3,4,5]
     result: 1+2=3; 2+3=5; 3+4=7: 4+5=9
'''
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y= [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
x.index[0]+


'''
# 3) from a list/tuple of numbers/string, find the number/string that occurs the maximum
'''






'''
# 4) write a function to convert an integer into indian currency format
    eg: 1000->1,000  10000->10,000  546100->5,46,100 etc
'''
currency = [1000,10000,546100]



def indiancurr(num):
    curr=""
    num = str(num)
    l = len(num)
    
    if(l < 4):
        return(num)
    else:
        curr = num[1-3:]
        num = num[0:1-3]
        l = len(num)
        
        while(l>0):
            curr = num[1-2:]+"," + curr
            num = num[0:1-2]
            l=len(num)
            
            return(curr)

indiancurr(145678919)


# write a python function to check if an input is palindrom

# write a python function to convert centigrade to farenheit and vice versa


