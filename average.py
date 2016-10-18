import sqlite3   #enable control of an sqlite database

f="discobandit.db"
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

q = "SELECT students.name, students.id, courses.mark from students, courses where students.id=courses.id"
c.execute(q)
info = c.fetchall()

avg = 0
pos = 0
ctr = 0

while pos < len(info):
    idNum = info[pos][1] #id of student
    if pos == 0:
        tmp_id = info[0][1] #first value
    if idNum == tmp_id: #if same student
        ctr += 1
        avg += info[pos][2]
        pos +=1
    else:
        print info[pos-1][0], info[pos-1][1], avg*1.0/ctr
        tmp_id = idNum #set id = next student
        avg = 0 #reset
        ctr = 0
print info[pos-1][0], info[pos-1][1], avg*1.0/ctr      
    
#==========================================================
db.commit() #save changes
db.close()  #close database
