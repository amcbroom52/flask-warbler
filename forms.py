from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, HiddenField
from wtforms.validators import InputRequired, Email, Length, URL, Optional


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[InputRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField(
        'Username',
        validators=[InputRequired(), Length(max=30)],
    )

    email = StringField(
        'E-mail',
        validators=[InputRequired(), Email(), Length(max=50)],
    )

    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=6, max=50)],
    )

    image_url = StringField(
        '(Optional) Image URL',
        validators=[Optional(), URL(), Length(max=255)]
    )


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField(
        'Username',
        validators=[InputRequired(), Length(max=30)],
    )

    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=6, max=50)],
    )

class UpdateUserForm(UserAddForm):
    """Edit user form."""

    header_image_url = StringField(
        "Header Image",
        validators=[Optional(), URL(), Length(max=255)]
    )

    bio = TextAreaField(
        "Bio",
        validators=[Optional()]
    )

    location = StringField(
        "Location",
        validators=[Optional(), Length(max=30)]
    )

class LikeButtonForm(FlaskForm):
    """Like button form."""

    current_url = HiddenField(
        validators=[InputRequired(), URL()]
    )



class CsrfProtectForm(FlaskForm):
    """CSRF protect form."""
