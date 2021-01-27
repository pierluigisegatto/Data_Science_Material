# get_ipython().getoutput("pip install ipython-sql ")


get_ipython().run_line_magic("load_ext", " sql")


# Enter the connection string for your Db2 on Cloud database instance below
# get_ipython().run_line_magic("sql", " ibm_db_sa://my-username:my-password@my-hostname:my-port/my-db-name")
get_ipython().run_line_magic("sql", " ibm_db_sa://")


# type in your query to retrieve list of all tables in the database for your db2 schema (username)
get_ipython().run_line_magic("sql", " select TABSCHEMA, TABNAME, CREATE_TIME from SYSCAT.TABLES where TABSCHEMA='RDZ36675'")


get_ipython().run_line_magic("sql", " select * from SYSCAT.TABLES where TABNAME = 'SCHOOLS'")


# type in your query to retrieve the number of columns in the SCHOOLS table
get_ipython().run_line_magic("sql", " select count(*) from SYSCAT.COLUMNS where TABNAME = 'SCHOOLS'")


# type in your query to retrieve all column names in the SCHOOLS table along with their datatypes and length
get_ipython().run_line_magic("sql", " select COLNAME, TYPENAME, LENGTH from SYSCAT.COLUMNS where TABNAME = 'SCHOOLS'")


get_ipython().run_line_magic("sql", " select * from SCHOOLS limit(5)")


get_ipython().run_line_magic("sql", " select count(*) from SCHOOLS where \"Elementary, Middle, or High School\" = 'ES'")


get_ipython().run_line_magic("sql", " select MAX(Safety_Score) AS MAX_SAFETY_SCORE from SCHOOLS")


get_ipython().run_line_magic("sql", " select Name_of_School, Safety_Score from SCHOOLS where \")
  Safety_Score= (select MAX(Safety_Score) from SCHOOLS)


get_ipython().run_line_magic("sql", " select Name_of_School, AVERAGE_STUDENT_ATTENDANCE from SCHOOLS order by \")
  AVERAGE_STUDENT_ATTENDANCE desc nulls last LIMIT(10)


get_ipython().run_line_magic("sql", " SELECT Name_of_School, Average_Student_Attendance  \")
     from SCHOOLS \
     order by Average_Student_Attendance \
     fetch first 5 rows only


#Use the REPLACE() function to replace 'get_ipython().run_line_magic("'", " with ''")
#See documentation for this function at: 
# https://www.ibm.com/support/knowledgecenter/en/SSEPGG_10.5.0/com.ibm.db2.luw.sql.ref.doc/doc/r0000843.html

get_ipython().run_line_magic("sql", " SELECT Name_of_School, REPLACE(Average_Student_Attendance, '%', '') \")
     from SCHOOLS \
     order by Average_Student_Attendance \
     fetch first 5 rows only


get_ipython().run_line_magic("sql", " SELECT Name_of_School, Average_Student_Attendance  \")
     from SCHOOLS \
     where CAST ( REPLACE(Average_Student_Attendance, 'get_ipython().run_line_magic("',", " '') AS DOUBLE ) < 70 \")
     order by Average_Student_Attendance


get_ipython().run_line_magic("sql", " select Community_Area_Name, sum(College_Enrollment) AS TOTAL_ENROLLMENT \")
   from SCHOOLS \
   group by Community_Area_Name 


get_ipython().run_line_magic("sql", " select Community_Area_Name, sum(College_Enrollment) AS TOTAL_ENROLLMENT \")
   from SCHOOLS \
   group by Community_Area_Name \
   order by TOTAL_ENROLLMENT asc \
   fetch first 5 rows only


get_ipython().run_cell_magic("sql", " ", """-- For this solution to work the CHICAGO_SOCIOECONOMIC_DATA table as created in the last lab of Week 3 should already exist
select hardship_index 
   from chicago_socioeconomic_data CD, schools CPS 
   where CD.ca = CPS.community_area_number 
      and college_enrollment = 4368
""")


get_ipython().run_line_magic("sql", " select ca, community_area_name, hardship_index from chicago_socioeconomic_data \")
   where ca in \
   ( select community_area_number from schools order by college_enrollment desc limit 1 )
