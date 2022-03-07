import sqlite3

def sql_start():
    """Создаём Базу данных"""
    global base, cur
    base = sqlite3.connect('db.db')
    cur = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS subscriptions(name TEXT, znak TEXT)')
    base.commit()

async def sql_add_command(state):
    """Добавление данных в бд"""
    async with state.proxy() as data:
        cur.execute('INSERT INTO subscriptions VALUES (?,?)', tuple(data.values()))
        base.commit()



















