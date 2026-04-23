import time
from flask import request

def run(app, db):
    @app.route('/create', methods=['POST'])
    def create():
        body = request.get_json()
        title = body.get("title")
        description = body.get("description")
        
        if (not title) or (not isinstance(title, str)):
            return { "error": "You must pass a string title in body" }, 400
            
        if (not description) or (not isinstance(description, str)):
            return { "error": "You must pass a string description in body" }, 400
            
        allTasks = db.all()
        lastTask = allTasks[-1] if allTasks else {}
        newId = lastTask.get("id") + 1 if lastTask.get("id") else 1
        
        nowTimestamp = time.time()
        
        db.insert({
            "id": newId,
            "title": title,
            "description": description,
            "completed": False,
            "createdAt": int(nowTimestamp)
        })
        
        return { "message": "Created successfully" }, 201