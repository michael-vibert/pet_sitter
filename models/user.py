from main import db 


class User(db.Model):
    __tablename__ = "users"
    # table rows
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)
    user_password = db.Column(db.String, nullable=False)
    user_verified = db.Column(db.Boolean, nullable=False)
    
    pets = db.relationship("Pet", backref="owner", cascade="all, delete")
    rentals = db.relationship("Rental", backref="renter", cascade="all, delete")