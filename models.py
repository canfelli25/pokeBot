from app import db

class User(db.Model):
    __tablename__= 'user'
    telegram_user_id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    def insert(**kwargs):
        self.name = kwargs['name']
        self.telegram_user_id = kwargs['user_id']

        user = self.query.get(self.telegram_user_id)

        if user is None:
            db.session.add(self)
            db.session.commit()
            user = self
        
        return user