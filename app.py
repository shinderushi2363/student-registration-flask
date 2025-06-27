from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

# 🔌 Connect to RDS MySQL
def get_connection():
    return pymysql.connect(
        host="studentdb.cebqy8iach2s.us-east-1.rds.amazonaws.com",
        user="admin",
        password="Account2363#",  # 🔐 Use secure method in real apps
        database="studentdb"
    )

# 🏠 Home Route - Registration Form
@app.route('/')
def home():
    return render_template('register.html')

# 📨 Form Submission Route
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    course = request.form['course']
    address = request.form['address']

    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO students (name, email, phone, course, address) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (name, email, phone, course, address))
        conn.commit()
        cursor.close()
        conn.close()
        return render_template('success.html', name=name)
    except Exception as e:
        return f"❌ Error: {e}"

# ▶️ Corrected Run Config for EC2
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
