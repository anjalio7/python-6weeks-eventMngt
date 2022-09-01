import mysql.connector
info=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    db="event_management"
)

value=info.cursor()

def login(arg):
    try:
        value.execute('SELECT * from login WHERE Username=%s and Password=%s',arg)
        return value.fetchall()
    except:
        return False

def addCourses(data):
    try:
        print(data)
        value.execute("INSERT INTO courses (Course_name,Course_code) VALUES (%s,%s)",data)
        info.commit()
        return True
    except:
        return False

def ViewCourses():
    try:
        value.execute('SELECT * from courses')
        return value.fetchall()
    except:
        return False

def ViewCoursesname():
    try:
        value.execute('SELECT ID,Course_name from courses')
        return value.fetchall()
    except:
        return False

def deleteCourses(data):
    try:
        # print(data)
        value.execute("DELETE FROM courses WHERE ID = %s",data)
        info.commit()
        return True
    except:
        return False

def editCourses(data):     
    try:
        print(data)
        value.execute(" SELECT * FROM courses WHERE id = %s",data)
        return value.fetchall()
    except:
        return False

def updateCourses_items(data):     
    try:
        print(data)
        value.execute(" UPDATE courses SET Course_name = %s,Course_code = %s WHERE id = %s",data)
        info.commit()
        return True
    except:
        return False

def addDepartment(data):
    try:
        print(data)
        value.execute("INSERT INTO department (course_id, name, username, password) VALUES (%s,%s,%s,%s)",data)
        info.commit()
        return True
    except:
        return False

def ViewDepartment():
    try:
        value.execute('SELECT department.id,courses.id,courses.course_name,department.name,department.username,department.password from department left join courses on department.course_id = courses.id')
        return value.fetchall()
    except:
        return False

def editDepartment(data):     
    try:
        print(data)
        value.execute(" SELECT department.id,courses.id,courses.course_name,department.name,department.username,department.password from department left join courses on department.id = %s",data)
        return value.fetchall()
    except:
        return False

def updateDepartment_items(data):     
    try:
        print(data)
        value.execute(" UPDATE department SET course_id = %s,name = %s,username = %s,password = %s WHERE id = %s",data)
        info.commit()
        return True
    except:
        return False

def addVenue(data):
    try:
        print(data)
        value.execute("INSERT INTO venue (name,location,capacity) VALUES (%s,%s,%s)",data)
        info.commit()
        return True
    except:
        return False

def ViewVenue():
    try:
        value.execute('SELECT * from venue')
        return value.fetchall()
    except:
        return False

def deleteVenue(data):
    try:
        # print(data)
        value.execute("DELETE FROM venue WHERE ID = %s",data)
        info.commit()
        return True
    except:
        return False


def editVenue(data):     
    try:
        print(data)
        value.execute(" SELECT * FROM venue WHERE id = %s",data)
        return value.fetchall()
    except:
        return False

def updateVenue_items(data):     
    try:
        print(data)
        value.execute(" UPDATE venue SET name = %s,location = %s,capacity = %s WHERE id = %s",data)
        info.commit()
        return True
    except:
        return False

def ViewEvent():
    try:
        value.execute('SELECT event.ID, department.name,courses.Course_name, event.event_name, event.date, event.duration, venue.name , event.status from event left join department ON event.dept_id = department.id left join venue ON event.venue_id = venue.id left join courses on event.course_id = courses.id')
        return value.fetchall()
    except:
        return False

def RejectEvent(data):
    try:
        print("dajkajn",data)
        value.execute(" UPDATE event set status = 'Reject' WHERE id = %s",data)
        info.commit()
        return True
    except:
        return False

def view_today(data):
    try:
        value.execute(" SELECT event.ID, department.name,courses.Course_name, event.event_name, event.date, event.duration, venue.name , event.status from event left join department ON event.dept_id = department.id left join venue ON event.venue_id = venue.id left join courses on event.course_id = courses.id WHERE date =%s",data)
        return value.fetchall()
    except:
        return False

def AcceptEvent(data):
    try:
        print(data)
        value.execute(" UPDATE event set status = 'Accept' WHERE id = %s",data)
        info.commit()
        return True
    except:
        return False

def addReason(data):
    try:
        print(data)
        value.execute(" UPDATE event set reason = %s WHERE id = %s",data)
        info.commit()
        return True
    except:
        return False