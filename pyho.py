import MySQLdb
con = MySQLdb.connect("localhost","root","","database1") 
cur=con.cursor()
cur.execute("insert into details values('jus','30')") 
con.commit()
cur.close()
con.close()