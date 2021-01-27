import ibm_db


#Replace the placeholder values with the actuals for your Db2 Service Credentials
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            # e.g. "BLUDB"
dsn_hostname = "dashdb-txn-sbox-yp-lon02-02.services.eu-gb.bluemix.net"            # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_port = "50000"                    # e.g. "50000" 
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn_uid = "abc12345"                 # e.g. "abc12345"
dsn_pwd = "7dBZ3wWt9XN6+n5"                 # e.g. "7dBZ3wWt9XN6$o0J"


#Create database connection
#DO NOT MODIFY THIS CELL. Just RUN it with Shift + Enter
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )



#Lets first drop the table INSTRUCTOR in case it exists from a previous attempt
dropQuery = "drop table INSTRUCTOR"

#Now execute the drop statment
dropStmt = ibm_db.exec_immediate(conn, dropQuery)


#Construct the Create Table DDL statement - replace the ... with rest of the statement
createQuery = "create table INSTRUCTOR(id INTEGER PRIMARY KEY NOT NULL, fname Varchar(60), lname Varchar(60), City Varchar(60),CCode Char(2))"

#Now fill in the name of the method and execute the statement
createStmt = ibm_db.exec_immediate(conn, createQuery)


#Construct the query - replace ... with the insert statement
insertQuery = "INSERT INTO instructor (id,fname,lname,city,ccode) VALUES (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')"

#execute the insert statement
insertStmt = ibm_db.exec_immediate(conn, insertQuery)


#replace ... with the insert statement that inerts the remaining two rows of data
insertQuery2 = "INSERT INTO instructor (id,fname,lname,city,ccode) VALUES (2, 'Raul', 'Chong', 'Markham', 'CA'),(3,'Hima','Vasudevan','Chicago','US')"

#execute the statement
insertStmt2 = ibm_db.exec_immediate(conn, insertQuery2)


#Construct the query that retrieves all rows from the INSTRUCTOR table
selectQuery = "select * from INSTRUCTOR"

#Execute the statement
selectStmt = ibm_db.exec_immediate(conn, selectQuery)

#Fetch the Dictionary (for the first row only) - replace ... with your code
ibm_db.fetch_assoc(selectStmt)


#Fetch the rest of the rows and print the ID and FNAME for those rows
while ibm_db.fetch_row(selectStmt) get_ipython().getoutput("= False:")
   print (" ID:",  ibm_db.result(selectStmt, 0), " FNAME:",  ibm_db.result(selectStmt, "FNAME"))


#Enter your code below
stm = "UPDATE INSTRUCTOR SET city='MOOSETOWN' where fname='Rav'"
selectStmt = ibm_db.exec_immediate(conn, stm)




import pandas
import ibm_db_dbi


#connection for pandas
pconn = ibm_db_dbi.Connection(conn)


#query statement to retrieve all rows in INSTRUCTOR table
selectQuery = "select * from INSTRUCTOR"

#retrieve the query results into a pandas dataframe
pdf = pandas.read_sql(selectQuery, pconn)

#print just the LNAME for first row in the pandas data frame
pdf.LNAME[0]


#print the entire data frame
pdf


pdf.shape


ibm_db.close(conn)
