from main import db 


class Pet(db.Model):
    __tablename__ = "pets"
    # table rows
    pet_id = db.Column(db.Integer, primary_key=True)
    pet_name = db.Column(db.String, nullable=False)
    pet_type = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)