import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

n=int(input("Enter the number of distributed databases "))
databases=[]
for x in range(n):
	#appending all of the datasets 
	databases.append('mydatabase'+str(x+1))
#connecting to each of the seperate database 
for x in range(len(databases)):
	#print("x is ",x)
	#print("database name is ",databases[x])
	var=databases[x]
	try :
		mydb = mysql.connector.connect(
		  host="localhost",
		  user="root",
		  passwd="",
		)
		#print(mydb) #success message
		#creating an object to run the queries 
		mycursor = mydb.cursor()
		
		try :
			sql="CREATE DATABASE "+var
			mycursor.execute(sql)
			print("database created as ",var)
			try:
				mydb = mysql.connector.connect(
		 		host="localhost",
		  		user="root",
		  		passwd="",
				database=var
				)
				mycursor = mydb.cursor()
				sql="CREATE TABLE "+'t_main'+str(x+1)+" (id INT AUTO_INCREMENT PRIMARY KEY,c1 VARCHAR(100),c2 VARCHAR(100), c3 VARCHAR(100) , c4 VARCHAR(100), UNIQUE (c4))"
				print(sql)
				mycursor.execute(sql)
				print("Table created") 
			except:
				print("Table is not created")
		except :
			print("The database already exists :)")
	except:
		print("Can't be connected to the servers")
