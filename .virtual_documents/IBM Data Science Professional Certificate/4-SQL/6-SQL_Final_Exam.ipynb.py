get_ipython().getoutput("pip install ipython-sql")


get_ipython().run_line_magic("load_ext", " sql")


# Remember the connection string is of the format:
# get_ipython().run_line_magic("sql", " ibm_db_sa://my-username:my-password@my-hostname:my-port/my-db-name")
# Enter the connection string for your Db2 on Cloud database instance below
get_ipython().run_line_magic("sql", " ibm_db_sa://")


get_ipython().run_line_magic("sql", " select TABSCHEMA, TABNAME, CREATE_TIME from SYSCAT.TABLES where TABSCHEMA='RDZ36675'")


# Rows in Crime table
get_ipython().run_line_magic("sql", " select count(*) AS TOT_NUMBER_OF_CRIMES from CHICAGO_CRIME_DATA")


get_ipython().run_line_magic("sql", " select * from CHICAGO_CRIME_DATA fetch first 10 rows only")


get_ipython().run_line_magic("sql", " select * from CHICAGO_CRIME_DATA LIMIT 10")


get_ipython().run_line_magic("sql", " select count(*) AS CRIMES_INVOLVING_ARREST from CHICAGO_CRIME_DATA where ARREST = 'TRUE'")


get_ipython().run_line_magic("sql", " select distinct(primary_type) from CHICAGO_CRIME_DATA where location_description = 'GAS STATION'")


get_ipython().run_line_magic("sql", " select * from CENSUS_DATA limit 2")


get_ipython().run_line_magic("sql", " select distinct(community_area_name) from CENSUS_DATA \")
    where community_area_name LIKE 'Bget_ipython().run_line_magic("'", "")


get_ipython().run_line_magic("sql", " select * from CHICAGO_PUBLIC_SCHOOLS limit 5")


get_ipython().run_line_magic("sql", " select name_of_school, healthy_school_certified from CHICAGO_PUBLIC_SCHOOLS \")
    where (community_area_number BETWEEN 10 AND 15) \
    and healthy_school_certified = 'Yes'



get_ipython().run_line_magic("sql", " select AVG(safety_score) AS AVERAGE_SAFETY_SCORE from CHICAGO_PUBLIC_SCHOOLS")


get_ipython().run_line_magic("sql", " select community_area_name, avg(college_enrollment) AS college_enrollment from CHICAGO_PUBLIC_SCHOOLS \")
    group by community_area_name order by college_enrollment desc \
    fetch first 5 rows only


get_ipython().run_line_magic("sql", " select community_area_name, safety_score from CHICAGO_PUBLIC_SCHOOLS \")
    where safety_score = (select MIN(safety_score) from CHICAGO_PUBLIC_SCHOOLS)


get_ipython().run_line_magic("sql", " select S.community_area_name, C.community_area_number, S.safety_score, C.per_capita_income \")
from CENSUS_DATA AS C , CHICAGO_PUBLIC_SCHOOLS AS S\
where C.community_area_number = S.community_area_number \
and S.safety_score = (select MIN(safety_score) from CHICAGO_PUBLIC_SCHOOLS)
