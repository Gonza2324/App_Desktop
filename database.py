"cSpell:disable"
import mysql.connector

midb = mysql.connector.connect(
    host = "localhost",
    user = "Gonzalo",
    password = "KORNkorn2402",
    database = "derivadas"
)

cursor = midb.cursor()

def conectar_basededatos():
    return midb

#TODO:cambiar el nombre de la tabla
def Insert(entry1, entry2, entry3):
    cursor.execute("""
        INSERT INTO usuarios (nick, email, password)
        VALUES (%s, %s, %s)
    """, (entry1, entry2, entry3))
    midb.commit()