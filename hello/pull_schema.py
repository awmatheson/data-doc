## for the script
import psycopg

conn = psycopg2.connect(dbname="test", user="postgres", password="secret")

cur.execute('''select
  schemaname as "Schema",
  relname as "Table",
  description as "Description"
from
  pg_catalog.pg_statio_all_tables as st
left outer join
  pg_catalog.pg_description pgd on (pgd.objoid=st.relid)
WHERE 
  schemaname IN ('aggregates','heroku')
AND  
  (objsubid = 0 OR objsubid IS NULL)
order by
  1,2 asc''')


cur.execute('''select 
  table_schema as "Schema",
  table_name as "Table",
  column_name as "Column",
  data_type as "Data Type",
  coalesce(pgd.description,'') as "Description"
from
  pg_catalog.pg_statio_all_tables st
inner join
  information_schema."columns" sc on st.relname = sc.table_name
left outer join
  pg_catalog.pg_description pgd on (pgd.objoid=st.relid and pgd.objsubid=sc.ordinal_position) 
  and table_schema in ('heroku', 'aggregates')
order by
  1,
  2,
  3,
  ordinal_position''')

from django.db import models


## for the webapp part
# postgres://sfzixwtugxwrun:e4d04dee9409ebb4c662a3d95e2629d5e39b1a450b70e048f57d6256824ac90b@ec2-23-21-246-11.compute-1.amazonaws.com:5432/d55vbrhped6ur6

class User..
.
.
.
.
database = 

class Database(models.Model):
  user = models.ManyToManyField(User)
  db_alias = models.CharField(max_length=255)
  db_type = models.CharField(max_length=120)
  db_connection_url  = models.TextField()
  schemas = models.TextField() # These should be separated by a comma in the user input field

class Schema(models.Model):
	database = models.ForeignKey(Database, on_delete=models.CASCADE)
  schema_name = models.CharField(max_length=255)

class Table(models.Model):
	schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
  table_name = models.CharField(max_length=255)
  description = models.TextField()

class Column(models.Model):
	table = models.ForeignKey(Table, on_delete=models.CASCADE)
  column_name = models.CharField(max_length=255)
  data_type = models.CharField(max_length=80)
  description = models.TextField()

class DatabaseForm(ModelForm):
  class Meta:
    model = Database
    fields = ['db_alias','db_type','db_connection_url']

    #when user saves, in view run script to pull schema and tables and columns associated with database

