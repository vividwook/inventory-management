from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Device
import os

# Create Flask app
app = Flask(__name__)

#Enable CORS
CORS(app)

POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB", "inventory")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")

# Database Connection
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#Initialize SQLAlchemy
db.init_app(app)

# Define API routes
# GET
@app.route("/api/devices", methods=["GET"])
def get_devices():
    q = Device.query
    status = request.args.get("status")
    location = request.args.get("location")
    if status: q = q.filter_by(status=status)
    if location: q = q.filter_by(location=location)
    devices = q.limit(100).all()
    return jsonify([{
        "id": d.id, "asset_tag": d.asset_tag, "name": d.name,
        "location": d.location, "status": d.status
    } for d in devices])

# POST
@app.route("/api/devices", methods=["POST"])
def add_device():
    data = request.json
    device = Device(
        asset_tag=data["asset_tag"],
        name=data["name"],
        location=data["location"],
        status=data["status"],
    )
    db.session.add(device)
    db.session.commit()
    return jsonify({"message": "Device added"}), 201

# PUT
@app.route("/api/devices/<int:id>", methods=["PUT"])
def update_device(id):
    data = request.json
    d = Device.query.get_or_404(id)
    d.location = data.get("location", d.location)
    d.status = data.get("status", d.status)
    db.session.commit()
    return jsonify({"message": "Device updated"})

# Health Check
@app.route("/api/health")
def health(): return jsonify({"status": "ok"})

# App startup
if __name__ == "__main__":
    with app.app_context(): db.create_all()
    app.run(host="0.0.0.0", port=5000)
