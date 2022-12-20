import psycopg2
# Connect to your postgres DB 连接postgres
conn = psycopg2.connect("dbname=postgres user=postgres password=1")

# Open a cursor to perform database operations 打开游标执行数据库操作
cur = conn.cursor()

# Execute a query 执行查询
cur.execute("SELECT * FROM person")

# Retrieve query results 检索查询结果
records = cur.fetchall()
print(records)
print()

print('ID\tNAME\tAGE')
for record in records:
    print('%d\t%s\t%d' % record)
print()

age = input("Enter an age: ")
cur.execute("SELECT * FROM person WHERE age = %s" % age)
records = cur.fetchall()
print('ID\tNAME\tAGE')
for record in records:
    print('%d\t%s\t%d' % record)
print()

# insert data
person_id = input("Enter an id to insert: ")
person_age = input("Enter an age to insert: ")
person_name = input("Enter a name to insert: ")
cur.execute("insert into person (id, age, name) values (%s, %s, '%s')" % (person_id,person_age,person_name))
conn.commit()
cur.execute("SELECT * FROM person")
records = cur.fetchall()
print('ID\tNAME\tAGE')
for record in records:
    print('%d\t%s\t%d' % record)