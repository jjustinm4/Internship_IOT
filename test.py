import MySQLdb
x='11004E93AD61'
conn=MySQLdb.connect('localhost','root','','users')
cursor=conn.cursor()
cursor.execute("select * from check1")
tog=cursor.fetchone()
cursor.close()
for i in tog:
    tog1=i
while True:    
    print(tog1)
    conn=MySQLdb.connect('localhost','root','','users')
    cursor=conn.cursor()
    cursor.execute("select * from entries where id ='%s'"%(x))
    res=cursor.fetchone()
    print (res)
    cursor.close()
    cursor=conn.cursor()
    cursor.execute('select toggle from check1')
    tog=cursor.fetchone()
    for i in tog:
        tog1=i
