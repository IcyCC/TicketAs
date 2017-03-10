# -*- coding:utf-8 -*-  
from flask.ext.migrate import Migrate,MigrateCommand
from flask.ext.script import Manager,Shell

from server.app import *

app = create_app('run')
manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
    return dict(app = app,db = db)

manager.add_command("shell",Shell(make_context=make_shell_context,use_ipython=False))
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()