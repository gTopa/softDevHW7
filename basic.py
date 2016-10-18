import sqlite3

f = "discobandit.db"

db = sqlite3.connect(f)

#two cursors
c = db.cursor()
d = db.cursor()

def findAvg(id):
    q = "SELECT mark FROM courses WHERE courses.id = " + str(id) + ";"
    sum = 0.0
    ctr = 0
    for grade in d.execute(q):
        sum += grade[0]
        ctr += 1
    return sum / ctr

cmd = "SELECT name, id FROM students;"

for record in c.execute(cmd):
     print "Name: " + record[0] + ", ID: " + str(record[1])+", Average: " + str(findAvg(record[1]))

db.commit()
db.close()
