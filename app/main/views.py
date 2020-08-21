from flask import session,url_for,render_template
from . import main
from .. import db
from ..model import Course,Semester

def validate(courseid):
    if courseid[:2].isalpha() and courseid[2:].isnumeric() and len(courseid)==6:
        return True
    return False

@main.route('/<int:number>/<courseid>', methods = ['GET','POST'])
def visit_course(number,courseid):
    data = Course.query.filter_by(course_id = courseid).first()
    if data is not None and validate(courseid):
        return render_template('coursesite.html' , data = data , semester_no = number)
    else:
        return "<h1>Invalid Code!</h1>" # maybe error template

@main.route('/<int:number>')
def visit_semester(number):
    if int(number)< 9 and int(number) >0:
        data = Course.query.filter_by(semester_id = number).all()
        data_count = Course.query.count()
        n = int(data_count)
        rem = n - (n//3)
        return render_template('semester_page2.html',semester_no = number,data = data,n=n,rem = rem) #Actual site
    else:
        return "<h1>Invalid Code!</h1>"

@main.route('/')
def index():
    return render_template('home_temp.html')

@main.route('/check/<int:number>')
def trySem(number):
    out = ''
    data = Course.query.filter_by(semester_id = number).all()
    for item in data:
        out+= f'<h3>{item.course_id}</h3>'
    return out

@main.route('/allCourses')
def allCourses():
    semesters = Semester.query.all()
    return render_template('available_all.html',semesters = semesters)

@main.route('/debug1/<int:number>')
def trySem(number):
    out = ''
    data = Semester.query.all()
    for item in data:
        out+= f'<h3>{item.id}</h3>'
    return out
