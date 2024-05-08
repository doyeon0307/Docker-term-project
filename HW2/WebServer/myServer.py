from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    student_id = request.form['student_id']
    student_info = get_student_info(student_id)
    return render_template('myServer.html', student=student_info)
  return render_template('myServer.html', student=None)

def get_student_info(student_id):
  con = mysql.connector.connect(
    host='database',
    user='user',
    password='password',
    database='myDatabase'
  )
  cur = con.cursor(dictionary=True)
  cur.execute("SELECT * FROM students WHERE sid = %s", (student_id,))
  rst = cur.fetchone()
  cur.close()
  con.close()
  return rst

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)