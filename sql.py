import sqlite3

#connect to sqlite
connection=sqlite3.connect("student.db")

#create a cursor object  to insert record,create table,retrieve
cursor=connection.cursor()
#create a table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

#insert some more records


cursor.execute('''insert into STUDENT Values ('Shahid', 'Data Science', 'A', 90),
    ('Ayesha', 'Data Science', 'B', 85),
    ('John', 'Machine Learning', 'A', 78),
    ('Sara', 'Data Science', 'C', 88),
    ('Michael', 'AI', 'B', 92),
    ('Alice', 'AI', 'A', 95),
    ('Bob', 'Data Science', 'B', 80),
    ('Charlie', 'Machine Learning', 'A', 76),
    ('David', 'Data Science', 'C', 82),
    ('Eva', 'AI', 'B', 89),
    ('Frank', 'Data Science', 'A', 84),
    ('Grace', 'AI', 'C', 91),
    ('Henry', 'Machine Learning', 'B', 87),
    ('Ivy', 'Data Science', 'A', 77),
    ('Jack', 'AI', 'C', 93),
    ('Kim', 'Machine Learning', 'A', 81),
    ('Liam', 'Data Science', 'B', 79),
    ('Mia', 'AI', 'C', 86),
    ('Noah', 'Machine Learning', 'A', 88),
    ('Olivia', 'Data Science', 'B', 83);''')


#Display all the recors



print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')



for row in data:
    print(row)
    
    
    
    # close the  connection
    
connection.commit()
connection.close()

    