from app.models import db

class Department(db.Model):
    __tablename__="departments"

    id=db.Column(
        db.Integer,
        primary_key=True
    )
    department_name = db.Column(
            db.String(50),
            nullable=False
        )
    
    location = db.Column(
            db.String(100),
            nullable=False
        )
    
    head_of_department = db.Column(
            db.String(50),
            nullable=False
        )