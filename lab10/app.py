from flask import Flask, render_template
import psycopg2
app = Flask(__name__)

#создать схему запроса
#создать таблицу

#подключение к постгресс БД
con = psycopg2.connect('host=pg.spb-kit.online port=s4321 user=student password=stud_pass dbname = g11_Turova')

#маршрут 
@app.route('/list')
def my_list():
    cur = con.cursor()
    #получаем список всех заметок
    cur.execute("SELECT ID, txt, ts FROM lab10.notes;")
    #fatchall - возвращает все строки с сервера
    res = cur.fetchall()
    #Обязательно нужно закрывать
    cur.close()
    return render_template('list.html', list = res)

