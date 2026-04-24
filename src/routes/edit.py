from flask import request
from tinydb import Query

def run(app, db):
    @app.route('/edit', methods=['PATCH'])
    def edit():
        body = request.get_json()
        id = body.get("id")
        title = body.get("title")
        description = body.get("description")
        
        if not id or not isinstance(id, int):
            return { "error": "You must pass a integer id" }, 400
            
        if title is None and description is None:
            return { "error": "You must pass title or description on body" }, 400
            
        if title and not isinstance(title, str):
            return { "error": "You must pass a string title in body" }, 400
            
        if description and not isinstance(description, str):
            return { "error": "You must pass a string description in body" }, 400
            
        Task = Query()
        task = db.search(Task.id == id)
        
        if not task:
            return { "error": "Task not found" }, 404
        
        newTitle = title if title else task[0].get("title")
        newDescription = description if description else task[0].get("description")
        
        db.update({
            "title": newTitle,
            "description": newDescription
        }, Task.id == id)
        
        return { "message": "Updated successfully" }, 200