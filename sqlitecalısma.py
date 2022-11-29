# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 12:06:02 2022

@author: Burcu Özdemir
"""

import sqlite3
def selectoperasyonlari():
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute(""" select FirstName,lastName from customers where FirstName like 'c%' """)    
    
    for row in cursor:
        print("FirstName= " + row[0])
        print("LastName= " + row[1])
        print("*******************")  
    connection.close()
selectoperasyonlari()                  

# import sqlite3
# def selectOperasyonlari():
#     connection = sqlite3.connect("chinook.db")
#     cursor = connection.execute(""" select FirstName,lastName from customers where FirstName like '%r' """)
    
#     for row in cursor:
#         print("FirstName = " + row[0])
#         print("LastName = " + row[1])
#         print("*****************")
#     connection.close()
    
# selectOperasyonlari()

# def updateCustomer():
#     connection = sqlite3.connect("chinook.db")
#     connection.execute(""" update customers set city = 'İzmir' where city= 'istanbul' """)
    
#     connection.commit()
#     connection.close()
# updateCustomer()

# import sqlite3
#     connection = sqlite3
def joinOperasyonlari():
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute(""" select albums.Title, artists.Name from 
                                artists inner join albums
                                on artists.ArtistId = albums.ArtistId """)
                                
    for row in cursor:
        print("Title = " + row[0]+ "****" + "Name= " + row[1])
    connection.close()
joinOperasyonlari()