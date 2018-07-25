from app import db
import datetime
from flask_mongoengine.wtf import model_form

class Acl(db.Document):
    srcip = db.StringField(required=True, max_length=20)
    dstip = db.StringField(required=True, max_length=20)
    dstport = db.StringField(required = True, max_length = 20)
    device = db.StringField(required = True, max_length = 20)
    reason = db.StringField(required = True, max_length = 20)
    staff = db.StringField(required = True, max_length=20)
    time = db.DateTimeField(default=datetime.datetime.now())



AclForm = model_form(Acl)

