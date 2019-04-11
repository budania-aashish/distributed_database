#importing mysql connector 
import mysql.connector

#having a list of all the distributed databases 
databases=['mydatabase1','mydatabase2','mydatabase3','mydatabase4']

#connecting to each of the seperate database 
for x in range(len(databases)):
	#for all the databases
	#connecting them one by one 
	#assumed to be the operation in paraller 
	#pragma omp can be used usig python paraller libraries to work in the distributed environment 
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="",
	  database=databases[x]
	)
	mycursor = mydb.cursor()
	#query processing 
	#queries
	query1='SELECT c1, c2, c3, c4 FROM t_main'+str(x+1)+' limit 10'
	query2='SELECT c2, c3 FROM t_main' + str(x+1) + ' WHERE length(c2)>length(c1)'
	sql=query1
	#print(sql)
	#executing the query on server 
	mycursor.execute(sql)
	#extracting the infromation in the form of a list 
	myresult = mycursor.fetchall()
	#success message 
	if(len(myresult)) > 0 :
		print("\nCongrats! This is the data from the server ",str(x+1))
		print()	
		for x in myresult:
		  print(x)
	else :
		print("You have achieved nothing other than an empty set from database"+str(x+1))
		print()
	myresult=[]
	print()