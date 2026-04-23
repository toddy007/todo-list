from pathlib import Path
import importlib

def load_routes(app, db):
    for file in Path("src/routes").glob("*.py"):
        if file.name == "__init__.py":
            continue
    
        module = importlib.import_module(f"routes.{file.stem}")
        module.run(app, db)