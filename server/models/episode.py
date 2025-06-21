from server.models import db

class Episode(db.Model):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    appearances = db.relationship("Appearance", back_populates="episode", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date.isoformat(),
            "number": self.number
        }

    def to_dict_with_appearances(self):
        return {
            'id': self.id,
            'date': self.date,
            'number': self.number,
            'appearances': [
                {
                    'id': a.id,
                    'rating': a.rating,
                    'guest': {
                        'id': a.guest.id,
                        'name': a.guest.name,
                        'occupation': a.guest.occupation
                    }
                }
                for a in self.appearances
            ]
        }
    
    def __repr__(self):
        return f"<Episode id={self.id} date={self.date} number={self.number}>"
