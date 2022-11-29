# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:43:12 2022

@author: Burcu Özdemir
"""

import sqlite3
def selectOperasyonlari():
    connection = sqlite3.connect("chinook.db")

# cursor = connection.execute("""select FirstName,LastNAme
#                             from customers where city='Paris' or city='Berlin'
#                             order by FirstName desc""")

# for row in cursor:
#     print("First Name= " + row[0])
#     print("Last Name= " + row[1])
#     print("************")
    

# cursor = connection.execute("""select city,count(*) from Customers group by city
#                             having count(*)>1 order by count(*) desc""")

# for row in cursor:
#     print("City= " + row[0])
#     print("Count= " + str(row[1]))
#     print("************")

    cursor = connection.execute("""select FirstName,LastName from customers where
                            FirstName like 'a%' """)

    for row in cursor:
        print("FirstName= " + row[0])
        print("LastName= " + row[1])
        print("************")
    
    connection.close()
    
selectOperasyonlari()

def insertCustomer():
    connection = sqlite3.connect("Chinook.db")
    connection.execute(""" insert into customers (firstName,lastName,city,email) 
                       values ('Ömer','Özdemir','Ankara','omer2198@gmail.com')""")
    connection.commit()
    connection.close()
    
# insertCustomer()
def updateCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute(""" update customers set city= 'istanbul' where city = 'Ankara' """)
   
    connection.commit()
    connection.close()
# updateCustomer()
    
def deleteCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute(""" Delete from customers where city = 'İzmir' """)
    
    connection.commit()
    connection.close()
# deleteCustomer()

def joinOperasyonlari():
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute(""" select albums.Title, artists.Name from 
                                artists inner join albums
                                on artists.ArtistId = albums.ArtistId """)
    for row in cursor:
        print("Title = "+ row[0] + "*****" + "Name = " + row[1])
    connection.close()
joinOperasyonlari()