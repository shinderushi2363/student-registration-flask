# 🧱 Full Stack Deployment: Flask App on EC2 with AWS RDS (MySQL)

## 🎯 Objective
Deploy a Python Flask-based student registration web application on an Amazon EC2 instance, connect it to a MySQL database hosted on Amazon RDS, and make it accessible over the internet.

---

## 📦 Project Stack

| Layer     | Technology              |
|-----------|--------------------------|
| Frontend  | HTML (Flask Templates)   |
| Backend   | Python (Flask)           |
| Database  | Amazon RDS (MySQL)       |
| Hosting   | Amazon EC2               |
| Git Repo  | GitHub                   |

---

## ✅ Step-by-Step Deployment Guide

### ✅ STEP 1: Login into EC2
```bash
ssh -i my-key.pem ec2-user@<your-ec2-public-ip>
✅ STEP 2: Update & Install Packages
For Amazon Linux:
bash
Copy
Edit
sudo yum update -y
sudo yum install python3 git -y
For Ubuntu:
bash
Copy
Edit
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
✅ STEP 3: Clone Flask Project from GitHub
bash
Copy
Edit
git clone https://github.com/shinderushi2363/student-registration-flask.git
cd student-registration-flask
✅ STEP 4: Set Up Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
✅ STEP 5: Install Flask and PyMySQL
bash
Copy
Edit
pip install flask pymysql
☁️ Amazon RDS (MySQL) Setup
🔹 STEP 6.1: Create RDS Instance
Go to AWS RDS Console > Create Database

Choose: Standard Create

Engine: MySQL

DB Identifier: studentdb

Master Username: admin

Master Password: yoursecurepass123

Public Access: Yes

VPC Security Group: Create new (e.g., rds-access-group)

Initial DB Name: studentdb

Port: 3306

🔹 STEP 6.2: Allow Inbound MySQL Connections
Go to EC2 > Security Groups > rds-access-group > Inbound Rules

Add Rule:

Type: MySQL/Aurora

Port: 3306

Source: 0.0.0.0/0 (⚠️ For dev only. Use EC2 IP for production.)

🔹 STEP 6.3: Get RDS Endpoint
Example:

Copy
Edit
studentdb.abc123xyz.rds.amazonaws.com
✅ STEP 6.4: Modify app.py for RDS Connection
python
Copy
Edit
import pymysql

conn = pymysql.connect(
    host="your-rds-endpoint.rds.amazonaws.com",
    user="admin",
    password="yoursecurepass123",
    database="studentdb"
)
✅ STEP 7: Create MySQL Table in RDS
Create file:

bash
Copy
Edit
nano create_table.py
Paste:

python
Copy
Edit
import pymysql

conn = pymysql.connect(
    host="your-rds-endpoint.rds.amazonaws.com",
    user="admin",
    password="yoursecurepass123",
    database="studentdb"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    course VARCHAR(50),
    address TEXT
)
""")

conn.commit()
cursor.close()
conn.close()
Run it:

bash
Copy
Edit
python3 create_table.py
✅ STEP 8: Allow Flask Access from All IPs
At the end of app.py:

python
Copy
Edit
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
✅ STEP 9: Open Port 5000 in EC2 Security Group
Go to:

EC2 > Instances > Your Instance > Security Group > Edit Inbound Rules

Add Rule:

Type: Custom TCP

Port: 5000

Source: 0.0.0.0/0

✅ STEP 10: Run the Flask App
bash
Copy
Edit
python3 app.py
✅ STEP 11: Access Application in Browser
cpp
Copy
Edit
http://<your-ec2-public-ip>:5000
🔍 Test Full Flow
Fill and submit the student registration form.

Confirm the success message.

Verify data in RDS via SQL client or query:

sql
Copy
Edit
SELECT * FROM students;
📋 Project Summary
Component	Description
EC2	Hosted Flask App
GitHub	Cloned project source code
Python venv	Created virtual environment
pip	Installed Flask & PyMySQL
RDS	MySQL Database backend
Flask	Connected to RDS & exposed via browser

🔗 Project Links
🗃️ GitHub Repo: Student Registration App

👨‍💼 LinkedIn: Rushikesh Shinde

📌 Author
Rushikesh Shinde
Cloud & DevOps Enthusiast | AWS Learner
📫 Let's connect on LinkedIn