from tinydb import Query

def run(app, db):
    @app.route('/complete/<int:id>')
    def complete(id):
        Task = Query()
        task = db.search(Task.id == id)
        
        if not task:
            return { "error": "Task not found" }, 404

        if task[0].get("completed"):
            return { "error": "Task already completed" }, 400
            
        db.update({ "completed": True }, Task.id == id)
        
        return { "message": "Task completed successfully" }, 200