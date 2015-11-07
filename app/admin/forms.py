from werkzeug.security import check_password_hash
from wtforms import form, StringField, validators, PasswordField
from wtforms.validators import DataRequired
from app.models import User


class LoginForm(form.Form):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

    def get_user(self):
        user = User.objects(name=self.name.data).first()
        return user

    def validate_name(self, field):
        user = self.get_user()
        if user:
            if not check_password_hash(user.password, self.password.data):
                raise validators.ValidationError('password error')

        else:
            raise validators.ValidationError('user error')
