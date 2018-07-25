from app import app
from app.models import Acl
from flask_script import Manager

manager = Manager(app)

@manager.command
def save():
    acl = Acl(srcip="10.32.32.32", dstip="100.100.100.100", dstport="80", device="firewall", reason="zabbix", staff="wjl")
    acl.save()

if __name__ == '__main__':
    manager.run()


