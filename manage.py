from flask.ext.script import Manager, Server
from werkzeug.security import generate_password_hash
from app import create_app
from app.models import User, Post

app = create_app()
manager = Manager(app)

manager.add_command("runserver", Server(host='0.0.0.0', port=5000, use_debugger=True))

@manager.command
def add_user():
    admin = User(name='admin', password=generate_password_hash('123456'))
    admin.save()

@manager.command
def add_post():
    user = User.objects(name="admin").first()
    post = Post(title="Hello",
                content="Hello World",
                author=user,
                status=1,
                tags=['python', 'flask'])
    post.save()

if __name__ == '__main__':
    manager.run()