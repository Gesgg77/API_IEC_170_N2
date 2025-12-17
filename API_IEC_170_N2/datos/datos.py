import sqlite3

def conectar():
    return sqlite3.connect('api_iec_170.db')

def insertar_objeto(user):
    con = conectar()
    cur = con.cursor()
    cur.execute(
        'INSERT INTO users VALUES (NULL,?,?,?,?,?)',
        (user.name, user.username, user.email, user.phone, user.website)
    )
    con.commit()
    con.close()

def obtener_user_name(nombre):
    con = conectar()
    cur = con.cursor()
    cur.execute('SELECT * FROM users WHERE name=?', (nombre,))
    r = cur.fetchone()
    con.close()
    return r
