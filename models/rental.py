from main import db


class Rental(db.Model):
    __tablename__ = "rentals"
    
    rent_id = db.Column(db.Integer, primary_key=True, nullable=False)
    rent_date = db.Column(db.Date, nullable=False)
    
    user_id =  db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    pet_id =  db.Column(db.Integer, db.ForeignKey("pets.pet_id"), nullable=False)
