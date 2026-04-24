from tinydb import Query

def run(app, db):
    @app.route('/delete/<int:id>', methods=['DELETE'])
    def delete(id):
        Task = Query()
        task = db.search(Task.id == id)
        
        if not task:
            return { "error": "Task not found" }, 404

        db.remove(Task.id == id)
        
        return { "message": "Task deleted successfully" }, 200