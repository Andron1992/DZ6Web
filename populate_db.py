from faker import Faker
import psycopg2
import random
from datetime import datetime

# Параметри підключення до бази даних
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="2112",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
fake = Faker()

# Заповнення таблиці груп
group_names = ['Group A', 'Group B', 'Group C']
for group_name in group_names:
    cursor.execute("INSERT INTO groups (group_name) VALUES (%s)", (group_name,))

# Заповнення таблиці викладачів
for _ in range(5):
    cursor.execute("INSERT INTO teachers (first_name, last_name) VALUES (%s, %s)",
                   (fake.first_name(), fake.last_name()))

# Заповнення таблиці предметів
subject_names = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'Literature', 'Art']
for subject_name in subject_names:
    cursor.execute("INSERT INTO subjects (subject_name, teacher_id) VALUES (%s, %s)",
                   (subject_name, random.randint(1, 5)))

# Заповнення таблиці студентів
for _ in range(50):
    cursor.execute("INSERT INTO students (first_name, last_name, group_id) VALUES (%s, %s, %s)",
                   (fake.first_name(), fake.last_name(), random.randint(1, 3)))

# Заповнення таблиці оцінок
for _ in range(1000):
    cursor.execute("INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (%s, %s, %s, %s)",
                   (random.randint(1, 50), random.randint(1, 8), random.randint(1, 100), fake.date_between(start_date='-1y', end_date='today')))

# Підтвердження змін та закриття з'єднання
conn.commit()
cursor.close()
conn.close()
