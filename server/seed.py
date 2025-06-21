#!/usr/bin/env python3

from server.app import create_app
from server.models import db, User, Guest, Episode, Appearance
from werkzeug.security import generate_password_hash
from datetime import date

app = create_app()

with app.app_context():
    print("🌱 Seeding database...")

    # Clear existing data
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    User.query.delete()

    # Create users
    user1 = User(username="admin", password_hash=generate_password_hash("adminpass"))
    user2 = User(username="host", password_hash=generate_password_hash("hostpass"))

    db.session.add_all([user1, user2])
    db.session.commit()

    # Create guests
    guest1 = Guest(name="Zendaya", occupation="Actor")
    guest2 = Guest(name="Elon Musk", occupation="Entrepreneur")
    guest3 = Guest(name="Billie Eilish", occupation="Musician")

    db.session.add_all([guest1, guest2, guest3])
    db.session.commit()

    # Create episodes
    ep1 = Episode(date=date(2023, 11, 10), number=101)
    ep2 = Episode(date=date(2023, 11, 11), number=102)

    db.session.add_all([ep1, ep2])
    db.session.commit()

    # Create appearances
    a1 = Appearance(rating=5, guest_id=guest1.id, episode_id=ep1.id)
    a2 = Appearance(rating=4, guest_id=guest2.id, episode_id=ep1.id)
    a3 = Appearance(rating=5, guest_id=guest3.id, episode_id=ep2.id)

    db.session.add_all([a1, a2, a3])
    db.session.commit()

    print("✅ Done seeding!")
