import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="admin", host="localhost")
cursor = conn.cursor()

# создаем таблицу <name>
# cursor.execute("CREATE TABLE stasuptrader_db (id SERIAL PRIMARY KEY, name VARCHAR(50))")
# поддверждаем транзакцию
conn.commit()
# print("Таблица успешно создана")
cursor.close()
conn.close()