from appengine_django.models import BaseModel
from google.appengine.ext import db

# @see GAE "Modeling Entity Relationships" 
# http://code.google.com/appengine/articles/modeling.html

# Create your models here.
class Event(BaseModel):
    id = db.Key()
    start_datetime = db.DateTimeProperty()
    end_datetime = db.DateTimeProperty()
    title = db.StringProperty()
    tagline = db.StringProperty()
    description = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    owner = db.StringProperty() #ReferenceProperty()
    committee = db.StringProperty() #ReferenceProperty()
    guests = db.StringProperty()
    
    def __unicode__(self):
        return self.title
        
    