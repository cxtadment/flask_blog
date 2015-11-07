from flask.ext.admin import Admin
from app.admin.views import MyIndexView, UserView, PostView
from app.models import User, Post


def create_admin(app=None):
    admin = Admin(app, name="CleanBlogAdmin", index_view=MyIndexView(), base_template='admin/my_master.html')
    admin.add_view(UserView(User))
    admin.add_view(PostView(Post))