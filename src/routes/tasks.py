from flask import request
from tinydb import Query

def run(app, db):
    @app.route('/tasks', methods=['GET', 'POST'])
    def tasks():
        if request.method == 'GET':
            return db.all(), 200
            
        body = request.get_json()
        id = body.get("id")
        title = body.get("title")
        completed = body.get("completed")
        
        if id is None and title is None and completed is None:
            return { "error": "You must pass id or title or completed on body" }, 400
        
        if id and not isinstance(id, int):
            return { "error": "You must pass integer id" }, 400
        
        if title and not isinstance(title, str):
            return { "error": "You must pass string title" }, 400
        
        if completed and not isinstance(completed, bool):
            return { "error": "You must pass boolean completed" }, 400

        Tasks = Query()
        
        tasks = db.search(
            (id and Tasks.id == id) or
            (title and Tasks.title.matches(f".*{title}.*", flags=2)) or
            Tasks.completed == completed
        )
        
        if (not tasks):
            return { "error": "Tasks not found" }, 404
            
        return tasks, 200