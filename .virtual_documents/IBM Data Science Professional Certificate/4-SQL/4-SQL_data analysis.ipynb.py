# get_ipython().getoutput("pip install ipython-sql ")


get_ipython().run_line_magic("load_ext", " sql")


# Remember the connection string is of the format:
# get_ipython().run_line_magic("sql", " ibm_db_sa://my-username:my-password@my-hostname:my-port/my-db-name")
# Enter the connection string for your Db2 on Cloud database instance below
# i.e. copy after db2:// from the URI string in Service Credentials of your Db2 instance. Remove the double quotes at the end.
get_ipython().run_line_magic("sql", " ibm_db_sa://")


get_ipython().run_cell_magic("sql", "", """-- DROP TABLE mine;
CREATE TABLE mine (
	country VARCHAR(50),
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	test_score INT
);
DROP TABLE mine;""")


import pandas
chicago_socioeconomic_data = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')


# get_ipython().run_line_magic("sql", " PERSIST chicago_socioeconomic_data")
get_ipython().run_line_magic("sql", " DROP TABLE chicago_socioeconomic_data")
get_ipython().run_line_magic("sql", " --persist chicago_socioeconomic_data")


get_ipython().run_line_magic("sql", " SELECT * FROM chicago_socioeconomic_data limit 5;")


get_ipython().run_line_magic("sql", " select COUNT(*) from chicago_socioeconomic_data;")


get_ipython().run_line_magic("sql", " select COUNT(community_area_name) from chicago_socioeconomic_data where hardship_index > 50 ")


get_ipython().run_line_magic("sql", " select MAX(hardship_index) from chicago_socioeconomic_data;")


get_ipython().run_line_magic("sql", " select community_area_name from chicago_socioeconomic_data where hardship_index = (select MAX(hardship_index) from chicago_socioeconomic_data);")


get_ipython().run_line_magic("sql", " select community_area_name, per_capita_income_  from chicago_socioeconomic_data where per_capita_income_ > 60000;")


import matplotlib.pyplot as plt
get_ipython().run_line_magic("matplotlib", " inline")
import seaborn as sns

query = get_ipython().run_line_magic("sql", " select per_capita_income_, hardship_index from chicago_socioeconomic_data;")
df = query.DataFrame()

# df.plot(kind= 'scatter',x='per_capita_income_',y='hardship_index')
plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=df)

