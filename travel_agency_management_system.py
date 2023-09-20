#creating database
import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="12345678",
)
print(mydb)
mycursor=mydb.cursor()
mycursor.execute("create database travel_agency")
print("successfully database created")

#creating new table
import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="12345678",
	database="travel_agency",
)

mycursor=mydb.cursor()
mycursor.execute("create table world_tourist_data(flight_name varchar(200),name varchar(100),age int,address varchar(200),covid_test varchar(100),time int,start varchar(200),end varchar(200))")
print("successfully table created")

#creating tourist data
import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="12345678",
	database="travel_agency"
)
print(mydb)
mycursor=mydb.cursor()

#insert data
#add data into table
sql="insert into world_tourist_data(flight_name,name,age,address,covid_test,time,start,end) values (%s,%s,%s,%s,%s,%s,%s,%s)"
flight_name=input("enter flight name:")
name=input("enter tourist name:")
age=int(input("enter tourist age:"))
address=input("enter address:")
test=input("THE TEST IS:")
time=float(input("timing:"))
starting_point=input("starting point:")
to=input("ending point:")
val1=(flight_name,name,age,address,test,time,starting_point,to)
if test =="negative":
	print("the test is negative you can go")
else:
	print("the test is positive, so you can’t go")
mycursor.execute(sql,val1)
mydb.commit()
print("data saved successfully")

#add another data into table
sql="insert into world_tourist_data(flight_name,name,age,address,covid_test,time,start,end) values (%s,%s,%s,%s,%s,%s,%s,%s)"
flight_name=input("enter flight name:")
name=input("enter tourist name:")
age=int(input("enter tourist age:"))
address=input("enter address:")
test=input("THE TEST IS:")
time=float(input("timing:"))
starting_point=input("starting point:")
to=input("ending point:")
val2=(flight_name,name,age,address,test,time,starting_point,to)
if test =="negative":
	print("the test is negative,you can go")
else:
	print("the test is positive, so you can’t go")
mycursor.execute(sql,val2)
mydb.commit()
print("data saved successfully")

#add another data into table
sql="insert into world_tourist_data(flight_name,name,age,address,covid_test,time,start,end) values (%s,%s,%s,%s,%s,%s,%s,%s)"
flight_name=input("enter flight name:")
name=input("enter tourist name:")
age=int(input("enter tourist age:"))
address=input("enter address:")
test=input("THE TEST IS:")
time=float(input("timing:"))
starting_point=input("starting point:")
to=input("ending point:")
val3=(flight_name,name,age,address,test,time,starting_point,to)
if test =="negative":
	print("the test is negative,you can go")
else:
	print("the test is positive,so you can’t go")
mycursor.execute(sql,val3)
mydb.commit()
print("data saved successfully")

#add another data into table
sql="insert into world_tourist_data(flight_name,name,age,address,covid_test,time,start,end) values (%s,%s,%s,%s,%s,%s,%s,%s)"
flight_name=input("enter flight name:")
name=input("enter tourist name:")
age=int(input("enter tourist age:"))
address=input("enter address:")
test=input("THE TEST IS:")
time=float(input("timing:"))
starting_point=input("starting point:")
to=input("ending point:")
val4=(flight_name,name,age,address,test,time,starting_point,to)
if test =="negative":
	print("the test is negative,you can go")
else:
	print("the test is positive,so you can’t go")
mycursor.execute(sql,val4)
mydb.commit()
print("data saved successfully")

#add another data into table
sql="insert into world_tourist_data(flight_name,name,age,address,covid_test,time,start,end) values (%s,%s,%s,%s,%s,%s,%s,%s)"
flight_name=input("enter flight name:")
name=input("enter tourist name:")
age=int(input("enter tourist age:"))
address=input("enter address:")
test=input("THE TEST IS:")
time=float(input("timing:"))
starting_point=input("starting point:")
to=input("ending point:")
val5=(flight_name,name,age,address,test,time,starting_point,to)
if test =="negative":
	print("the test is negative,you can go")
else:
	print("the test is positive,so you can’t go")
mycursor.execute(sql,val5)
mydb.commit()
print("data saved successfully ")

#add another data into table
sql="insert into world_tourist_data(flight_name,name,age,address,covid_test,time,start,end) values (%s,%s,%s,%s,%s,%s,%s,%s)"
flight_name=input("enter flight name:")
name=input("enter tourist name:")
age=int(input("enter tourist age:"))
address=input("enter address:")
test=input("THE TEST IS:")
time=float(input("timing:"))
starting_point=input("starting point:")
to=input("ending point:")
val6=(flight_name,name,age,address,test,time,starting_point,to)
if test =="negative":
	print("the test is negative,you can go")
else:
	print("the test is positive,so you can’t go")
mycursor.execute(sql,val6)
mydb.commit()
print("data saved successfully")

#add data into table
sql="insert into world_tourist_data(flight_name,name,age,address,covid_test,time,start,end) values (%s,%s,%s,%s,%s,%s,%s,%s)"
flight_name=input("enter flight name:")
name=input("enter tourist name:")
age=int(input("enter tourist age:"))
address=input("enter address:")
test=input("THE TEST IS:")
time=float(input("timing:"))
starting_point=input("starting point:")
to=input("ending point:")
val7=(flight_name,name,age,address,test,time,starting_point,to)
if test =="negative":
	print("the test is negative,you can go")
else:
	print("the test is positive,so you can’t go")
mycursor.execute(sql,val7)
mydb.commit()
print("data saved successfully")

#add another data into table
sql="insert into world_tourist_data(flight_name,name,age,address,covid_test,time,start,end) values (%s,%s,%s,%s,%s,%s,%s,%s)"
flight_name=input("enter flight name:")
name=input("enter tourist name:")
age=int(input("enter tourist age:"))
address=input("enter address:")
test=input("THE TEST IS:")
time=float(input("timing:"))
starting_point=input("starting point:")
to=input("ending point:")
val8=(flight_name,name,age,address,test,time,starting_point,to)
if test =="negative":
	print("sorry,the test is negative,you can go")
else:
	print("the test is positive,so you can’t go")
mycursor.execute(sql,val8)
mydb.commit()
print("data saved successfully")

#add another data into table
sql="insert into
world_tourist_data(flight_name,name,age,address,covid_test,time,start,end) values (%s,%s,%s,%s,%s,%s,%s,%s)"
flight_name=input("enter flight name:")
name=input("enter tourist name:")
age=int(input("enter tourist age:"))
address=input("enter address:")
test=input("THE TEST IS:")
time=float(input("timing:"))
starting_point=input("starting point:")
to=input("ending point:")
val9=(flight_name,name,age,address,test,time,starting_point,to)
if test =="negative":
	print("the test is negative,you can go")
else:
	print("the test is positive,so you can’t go")
mycursor.execute(sql,val9)
mydb.commit()
print("data saved succssfully")

#add another data into table
sql="insert into world_tourist_data(flight_name,name,age,address,covid_test,time,start,end) values (%s,%s,%s,%s,%s,%s,%s,%s)"
flight_name=input("enter flight name:")
name=input("enter tourist name:")
age=int(input("enter tourist age:"))
address=input("enter address:")
test=input("THE TEST IS:")
time=float(input("timing:"))
starting_point=input("starting point:")
to=input("ending point:")
val10=(flight_name,name,age,address,test,time,starting_point,to)
if test =="negative":
	print("the test is negative,you can go")
else:
	print("the test is positive,so you can’t go")
mycursor.execute(sql,val10)
mydb.commit()
print("data saved successfully")
