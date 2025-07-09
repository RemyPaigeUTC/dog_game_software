import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post

# When the flask shell command runs, it will invoke this function and register the items returned by it in the shell session
# After you add the shell context processor function you can work with database entities without having to import them
@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}