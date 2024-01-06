import os
from app.main import create_app, db
from app import blueprint

environment = os.environ.get('ENV', 'development')
app = create_app(environment)
app.register_blueprint(blueprint)
app.app_context().push()

if __name__ == '__main__':
    app.run()
