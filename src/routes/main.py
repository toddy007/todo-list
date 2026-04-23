def run(app):
    @app.route('/')
    def home():
        return { "msg": "hello world" }, 200