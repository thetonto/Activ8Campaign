


import pyodbc
import time
import logging

logging.basicConfig(level=logging.INFO)

server = 'westerly'
database = 'Activ8Live'
username = 'activ8'
password = 'activ8'

cnxn = pyodbc.connect('DSN=activ8cclive;UID=activ8;PWD=activ8')
cursor = cnxn.cursor()
sql = "SELECT PersonType, Title, FirstName, LastName, EMailAddress, FirstJoinedDate, IsCancelled, CancelledDate, DateOfBirth, Sex, ClientID, ClientCategory, DateLastModified FROM Client WHERE (EMailAddress <> '') AND (NOT (ClientID IN (SELECT OwnerID FROM CFieldVal WHERE (CustomFieldID = '{27220B0A-BCDA-4A63-B9ED-B70ABE30FA06}') AND (ValueAsBoolean = 1))))"

print(sql)
cursor.execute(sql)

print(cursor.description)

row = cursor.fetchone()
while row:
    print(row.FirstName)
    row = cursor.fetchone()