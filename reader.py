import MySQLdb
import serial
import time
import webbrowser
import MySQLdb
obj=serial.Serial('COM3',9600)
time.sleep(1)
q='http://localhost/index.html'
webbrowser.open(q)
conn=MySQLdb.connect('localhost','root','','users')
cursor=conn.cursor()
cursor.execute("select * from check1")
tog=cursor.fetchone()
cursor.close()
conn.close()
for i in tog:
    tog1=i
while True:
    if tog1==1:
        x=obj.readline()
        conn=MySQLdb.connect('localhost','root','','users')
        cursor=conn.cursor()
        cursor.execute("select * from entries where id ='%s'"%(x[:12]))
        res=cursor.fetchone()
        if res is None:
            q='http://localhost/register.php?id='+x
            webbrowser.open(q) 
        else:
            q='http://localhost/nextpage.php?id='+x
            webbrowser.open(q)
        for i in tog:
            tog1=i
    cursor.close()
    #conn.close()
    conn=MySQLdb.connect('localhost','root','','users')
    cursor=conn.cursor()
    cursor.execute('select toggle from check1')
    tog=cursor.fetchone()
    for i in tog:
        tog1=i

        
   
        
