import os
from flask import Flask
from flask_cors import CORS
from importlib import import_module
from pathlib import Path

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Dynamically import and register route blueprints
    routes_path = Path(__file__).parent / "routes"
    for py in routes_path.glob("*.py"):
        if py.name.startswith("_"):
            continue
        mod = import_module(f"app.routes.{py.stem}")
        if hasattr(mod, "bp"):
            app.register_blueprint(mod.bp)
    return app
