import sqlite3
def reg_user(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(""" CREATE TABLE IF NOT EXISTS user_time (
        id BIGINT,
        status_pod,
        money
        ) """)
    db.commit()
    sql.execute(f"SELECT id FROM user_time WHERE id ={id}")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user_time VALUES (?,?,?)", (id,0,0))
        db.commit()


def channeg_status(id): #Изменения статуса пользователя
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE user_time SET status_pod = 1 WHERE id = {id}")
    db.commit()

def channeg_money(id,summ): #Изменения баланса
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    money = sql.execute(f"SELECT money FROM user_time WHERE id ={id}").fetchone()
    money = money[0]
    sql.execute(f"UPDATE user_time SET money = {summ+money} WHERE id = {id}")
    db.commit()

def cheak_status(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    a = sql.execute(f"SELECT status_pod FROM user_time WHERE id ={id}").fetchone()
    return a[0]

def cheak_money(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    a = sql.execute(f"SELECT money FROM user_time WHERE id ={id}").fetchone()
    return a[0]

def members_list():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    a = sql.execute(f'SELECT COUNT(*) FROM user_time').fetchone()[0]
    return a