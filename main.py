print("Hello,World!")
print()

a = 1
b = 2
c = a + b
print(c)
print()

a = [1,2,3,4,5]
s = 0
for v in a:
    print(v)
print()
for v in a:
    s = s + v
print(s)
print()

persons = [
 {'name':'John','age':20},
 {'name':'Paul','age':19},
 {'name':'Karl','age':22},
 {'name':'Helen','age':21}
]
print("name\tage")
for person in persons:
    print('%s\t%d' % (person['name'],person['age']))
age = input("1-Enter an age to find: ")
print(age)
print()
age = input("2-Enter an age to find: ")
for person in persons:
    if person['age'] == int(age):
        print('%s\t%d' % (person['name'],person['age']))

