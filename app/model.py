from . import db

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key = True)
    course_id = db.Column(db.String , index = True,unique = True)
    course_title = db.Column(db.String(64))
    description = db.Column(db.String(64))
    vid_title1 = db.Column(db.String(64))
    vid_desc1 = db.Column(db.String(64))
    vid_title2 = db.Column(db.String(64))
    vid_desc2 = db.Column(db.String(64))
    resc_title1 = db.Column(db.String(64))
    resc_desc1 = db.Column(db.String(64))
    resc_title2 = db.Column(db.String(64))
    resc_desc2 = db.Column(db.String(64))
    resc_title3 = db.Column(db.String(64))
    resc_desc3 = db.Column(db.String(64))
    vid_link1 = db.Column(db.String(64))
    vid_link2 = db.Column(db.String(64))
    resc_link1 = db.Column(db.String(64))
    resc_link2 = db.Column(db.String(64))
    resc_link3 = db.Column(db.String(64))
    mit_link = db.Column(db.String(64))
    semester_id = db.Column(db.Integer, db.ForeignKey('semesters.id'))

    def __repr__(self):
        return '<Course %r> ' % self.course_id

class Semester(db.Model):
    __tablename__ = 'semesters'
    id = db.Column(db.Integer, primary_key = True)
    courses = db.relationship('Course',backref = 'semester')

    def __repr__(self):
        return '<Semester %r> ' % self.id
