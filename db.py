import MySQLdb as mdb

def query():
  conn = mdb.connect(host=<host>, user=<user>, passwd=<password>, db=<db_name>)
  cur = con.cursor()
  cur.execute("SELECT column1,column2 FROM table WHERE column3=value") ####to do
  r = cursor.fetchall()
  return r


'''mysql_note.md
# WHERE
```
SELECT column_name FROM sheet_name WHERE column operator value
```
operator: =; <>;	>;	<; >=; <=; BETWEEN; LIKE
'''
