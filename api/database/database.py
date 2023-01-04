import mysql.connector as database
from flask import g,current_app
from flask.cli import with_appcontext
import click

from pprint import pprint


#generate connection to database.

def get_db():
    if 'db' not in g:
        g.db = database.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_NAME']
        )
        g.c = g.db.cursor(dictionary=True,buffered=True)
        
        return g.db,g.c


#close connection.

def close_db(e=None):
    db = g.pop('db',None)
    if db is not None:
        db.close()
    



#create all the tables for the first time.

def init_db():
    try:
        db,c = get_db()
        c.execute(
            """
            SHOW DATABASES;
            """
        )
        result = c.fetchall()
        click.echo("Database successfully working.")
        pprint(result)
    except Exception as e:
        click.echo("Database has failed during test.")
        click.echo(e)



#command.
@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    #click.echo("Database sucessfully initialize!")


#init all.
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)