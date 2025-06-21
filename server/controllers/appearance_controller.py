from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models import db
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode

appearance_bp = Blueprint("appearances", __name__)

@appearance_bp.route("/appearances", methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.get_json()

    try:
        rating = int(data.get("rating"))
        if not (1 <= rating <= 5):
            return jsonify({"error": "Rating must be between 1 and 5"}), 400

        guest = Guest.query.get(data.get("guest_id"))
        episode = Episode.query.get(data.get("episode_id"))

        if not guest or not episode:
            return jsonify({"error": "Guest or episode not found"}), 404

        new_appearance = Appearance(
            rating=rating,
            guest_id=guest.id,
            episode_id=episode.id
        )

        db.session.add(new_appearance)
        db.session.commit()

        return jsonify(new_appearance.to_dict()), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400
