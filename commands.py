from main import db
from flask import Blueprint
from main import bcrypt
from models.pet import Pet
from models.user import User
from models.rental import Rental



db_commands = Blueprint("db", __name__)


@db_commands .cli.command("create")
def create_tables():
    db.create_all()
    print("All tables and relations have been successfully created")
    

@db_commands .cli.command("drop")
def drop_tables():
    db.drop_all()
    print("All tables in db have now been dropped")


@db_commands .cli.command("seed")
def seed_tables():
    
    user1 = User(
        user_name = "Mike", 
        user_password = bcrypt.generate_password_hash("mikee").decode('utf-8'),
        user_verified = True
    )
    
    user2 = User(
        user_name = "Katie", 
        user_password = bcrypt.generate_password_hash("katieW").decode('utf-8'),
        user_verified = True    
    )    

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    
    pet1 = Pet(
        pet_name = "Tiggy", 
        pet_type = "dog",
        user_id = 1
    )

    pet2 = Pet(
        pet_name = "Poncho", 
        pet_type = "cat",
        user_id = 2
    )    

    
    db.session.add(pet1)
    db.session.add(pet2)
    db.session.commit()
    
    
    # patient1 = Patient(
    #     per_id = 2,
    #     pat_age = 15,
    #     pat_sex = "F",
    #     pat_weight = 45.3,
    #     pat_height = 147
    # )
    
    # patient2 = Patient(
    #     per_id = 1,
    #     pat_age = 43,
    #     pat_sex = "M",
    #     pat_weight = 75.2,
    #     pat_height = 181
    # )
    
    # db.session.add(patient1)
    # db.session.add(patient2)
    # db.session.commit()
    
    # spec1 = Specialty(
    #     spec_type = "General Practice"
    # )
    
    # spec2 = Specialty(
    #     spec_type = "Haematology"
    # )
    
    # db.session.add(spec1)
    # db.session.add(spec2)
    # db.session.commit()
    
    # prac1 = Practitioner(
    #     per_id = 3,
    #     spec_id = 2
    # )
    
    # prac2 = Practitioner(
    #     per_id = 4,
    #     spec_id = 1
    # )
    
    # db.session.add(prac1)
    # db.session.add(prac2)
    # db.session.commit()
    
    # ex1 = Years(
    #     spec_id = 2,
    #     prac_id = 1
    # )
    
    # ex2 = Years(
    #     spec_id = 1,
    #     prac_id = 2
    # )

    # db.session.add(ex1)
    # db.session.add(ex2)
    # db.session.commit()
    
    print("Tables seeded!")