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
        value.execute('SELECT * from department WHERE username =%s and password =%s',arg)
        return value.fetchone()
    except:
        return False

def addEvent(data):
    try:
        print(data)
        value.execute("INSERT INTO event ( 	dept_id,course_id,event_name,date,duration,venue_id ) VALUES (%s,%s,%s,%s,%s,%s)",data)
        info.commit()
        return True
    except:
        return False
    
def ViewEvent(data):
    try:
        print(data)
        # value.execute('select * from event where dept_id = %s',data)
        value.execute('SELECT event.ID, department.name,courses.Course_name, event.event_name, event.date, event.duration, venue.name , event.status, event.Reason from event left join department ON event.dept_id = department.id left join venue ON event.venue_id = venue.id left join courses on event.course_id = courses.id where event.dept_id =%s',(data,))
        return value.fetchall()
    except:
        return False

def deleteEvent(data):
    try:
        # print(data)
        value.execute("DELETE FROM event WHERE ID = %s and dept_id = %s",data)
        info.commit()
        return True
    except:
        return False

def editEvent(data):     
    try:
        print("i am eddit",data)
        value.execute(" SELECT event.event_name, event.date, event.duration,venue.id, venue.name from event left join venue ON event.venue_id = venue.id where event.id =%s and event.dept_id=%s",data)
        return value.fetchall()
    except:
        return False

def updateEvent_items(data):     
    try:
        print(data)
        value.execute(" UPDATE event SET event_name = %s,date = %s, duration = %s,venue_id = %s WHERE id = %s and dept_id =%s",data)
        info.commit()
        return True
    except:
        return False

def ViewVenue():
    try:
        value.execute('SELECT ID,name from venue')
        return value.fetchall()
    except:
        return False

def viewVenuedata():
    try:
        value.execute('SELECT * from venue')
        return value.fetchall()
    except:
        return False
