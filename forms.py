"""Forms for playlist app."""

from wtforms import SelectField, StringField
from wtforms.validators import Length
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField(validators=[Length(1, 50, "Name must be between 1 and 50 characters")])
    description = StringField()
    

class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField(validators=[Length(1, 50, "Title must be between 1 and 50 characters")])
    artist = StringField(validators=[Length(min=1, max=50, message="Name must be between 1 and 50 characters")])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
