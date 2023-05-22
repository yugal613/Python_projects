import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="students_data"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table for students if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    grade VARCHAR(10)
)
"""
cursor.execute(create_table_query)
conn.commit()

# Insert a new student into the database
def insert_student(name, age, grade):
    insert_query = """
    INSERT INTO students (name, age, grade)
    VALUES (%s, %s, %s)
    """
    student_data = (name, age, grade)
    cursor.execute(insert_query, student_data)
    conn.commit()

# Retrieve all students from the database
def get_all_students():
    select_query = "SELECT * FROM students"
    cursor.execute(select_query)
    students = cursor.fetchall()
    return students

# Update a student's grade in the database
def update_student_grade(student_id, new_grade):
    update_query = "UPDATE students SET grade = %s WHERE id = %s"
    data = (new_grade, student_id)
    cursor.execute(update_query, data)
    conn.commit()

# Delete a student from the database
def delete_student(student_id):
    delete_query = "DELETE FROM students WHERE id = %s"
    data = (student_id,)
    cursor.execute(delete_query, data)
    conn.commit()

# Close the database connection
def close_connection():
    cursor.close()
    conn.close()

# Example usage
insert_student("yugal Mittal", 24, "A")
insert_student("suraj Dhenge", 22, "B")

students = get_all_students()
for student in students:
    print(student)

update_student_grade(1, "A+")
delete_student(2)

students = get_all_students()
for student in students:
    print(student)

close_connection()
