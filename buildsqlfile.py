import sqlite3
conn = sqlite3.connect('mydatabase_ls_On_Fire.sqlite3')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS Certificate (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT ,
                UIDStudent TEXT ,
                GENDER TEXT , 
                WordUse TEXT)""")

def insert_imformation(Name,UIDStudent,Gender,WordUse):
    with conn: 
        command = 'INSERT INTO Certificate VALUES (?,?,?,?,?)'
        c.execute(command, (None, Name, UIDStudent, Gender, WordUse))
    conn.commit()
    print('Saved')

#insert_job('sirawichaya' , '0659420414' , 'software en')

def view_imformation():
    with conn:
        command = 'SELECT * FROM Certificate'
        c.execute(command)
    return c.fetchall()
