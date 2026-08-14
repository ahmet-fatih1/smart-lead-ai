from flask import Flask, jsonify
from flask_cors import CORS

from config import Config
from app.routes import pages_bp, api_bp
from app.database import init_db

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    CORS(app)

    init_db(app)

    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp)

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({
            "durum": "aktif"
        })
    return app