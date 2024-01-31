from . import db 
from flask_login import UserMixin
from sqlalchemy.orm import synonym

class User(db.Model, UserMixin):
    userId = db.Column(db.String(15), primary_key=True)
    password = db.Column(db.String(100), nullable=False)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    userType = db.Column(db.String(20), nullable=False)
    posts = db.relationship('Post')
    # ballots = db.relationship('Ballot', backref='user', lazy=True)

    def get_id(self):
        return str(self.userId)

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studentId = db.Column(db.String(15), db.ForeignKey('user.userId'), nullable=False, unique=True)
    name = db.Column(db.String(200), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    voteCount = None
    votePercentage = None
    # ballot_id = db.Column(db.Integer, db.ForeignKey('ballot.id'), nullable=False)
    student = db.relationship('User', backref='candidate', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.String(15), db.ForeignKey('user.userId'), nullable=False)
    userName = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text)
    image = db.Column(db.String(200))

class Vote(db.Model):
    voter = db.Column(db.String(15), db.ForeignKey('user.userId'), primary_key=True, nullable=False)
    president = db.Column(db.String(15))
    executive_vp = db.Column(db.String(15))
    executive_board_sec = db.Column(db.String(15))
    vp_finance = db.Column(db.String(15))
    vp_academic_affairs = db.Column(db.String(15))
    vp_internal_affairs = db.Column(db.String(15))
    vp_external_affairs = db.Column(db.String(15))
    vp_public_relations = db.Column(db.String(15))
    vp_research_dev = db.Column(db.String(15))
    first_yr_rep = db.Column(db.String(15))
    second_yr_rep = db.Column(db.String(15))
    third_yr_rep = db.Column(db.String(15))
    fourth_yr_rep = db.Column(db.String(15))

class BallotStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isOpen = db.Column(db.Boolean, nullable=False)
    # ballots = db.relationship('Ballot', back_populates='ballot_status', lazy=True)

# class Ballot(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.String(15), db.ForeignKey('user.userId'), nullable=False)
#     ballot_status_id = db.Column(db.Integer, db.ForeignKey('ballot_status.id'), nullable=False)
#     ballot_name = db.Column(db.String(100), nullable=False)
#     candidates = db.relationship('Candidate', backref='ballots', lazy=True)
#     ballot_status = db.relationship('BallotStatus', back_populates='ballots')


