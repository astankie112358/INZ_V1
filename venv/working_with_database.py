import mysql.connector
from pandas import DataFrame
def connecttodatabase():
    conn=None
    conn=mysql.connector.connect(host='127.0.0.1',
                                     database='nba_inz_schema',
                                     user='root',
                                     password='nuka2008',
                                     auth_plugin='mysql_native_password'
                                     )
    return conn

def insertplayer(id:int, surname:str, name: str):
    conn=connecttodatabase()
    inscursor=conn.cursor()
    sql=("Insert into zawodnicy values (%s, %s, %s)")
    values=(id,surname,name)
    try:
        inscursor.execute(sql,values)
        conn.commit()
    except:
        print("Podałeś złe dane dla zawodnika")
    conn.close()
def deleteplayer(id:int):
    conn=connecttodatabase()
    delcursor=conn.cursor()
    sql=("Delete from zawodnicy where id_zawodnik=%s")
    values=(id,)
    try:
        delcursor.execute(sql,values)
        conn.commit()
    except:
        print("Podałeś złego zawodnika")
    conn.close()

def insertteam(id: int, teamname: str, cityname: str):
    conn=connecttodatabase()
    inscursor=conn.cursor()
    sql=("Insert into druzyny values (%s, %s, %s)")
    values=(id, teamname, cityname)
    try:
        inscursor.execute(sql,values)
        conn.commit()
    except:
        print("Podałeś złe dane dla druzyny")
    conn.close()

