# cli.py

import click
from flask.cli import with_appcontext
from .controllers.user import user_signup
from .database import db


@click.command('reset-db')
@with_appcontext
def reset_db_command():
    """Clear existing data and create new tables."""
    # run it with : FLASK_APP=. flask reset-db
    from .models.association import user_roles
    from .models.user import User
    from .models.role import Role
    from .models.token import Token
    db.drop_all()
    db.create_all()
    click.echo('The database has been reset.')

@click.command('create-admin')
@click.argument('username')
@click.argument('email')
@click.argument('password')
@with_appcontext
def create_admin_command(username, email, password):
    # run it with : FLASK_APP=. flask create-admin 'XXX' 'YYY' 'ZZZ'
    from .models.role import Role
    admin_role = Role.query.filter(Role.name == "admin").first()
    if admin_role is None:
        admin_role = Role()
        admin_role.name = "admin"
        admin_role.description = "the admin role duh."
        db.session.add(admin_role)
        db.session.commit()
    try:
        new_user = user_signup(username, email, password)
        new_user.roles.append(admin_role)
        db.session.add(new_user) # update the user roles
        db.session.commit()
        click.echo(username + " was created with admin role.")
    except Exception as err:
        return click.echo(str(err))

def cli_init_app(app):
    app.cli.add_command(reset_db_command)
    app.cli.add_command(create_admin_command)
