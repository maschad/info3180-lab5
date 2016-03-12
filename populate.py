from app import db
from app.models import Myprofile


def add():
    newprofile = Myprofile(first_name='john',
                           last_name='brown',
                           username='jonny105',
                           password='admin',
                           )
    db.session.add(newprofile)
    db.session.commit()


if __name__ == "__main__":
    add()
