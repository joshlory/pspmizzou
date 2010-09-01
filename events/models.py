from appengine_django.models import BaseModel
from google.appengine.ext import db
from calendar import HTMLCalendar
from datetime import date

# @see: GAE "Modeling Entity Relationships" 
# http://code.google.com/appengine/articles/modeling.html

class Event(BaseModel):
    id = db.Key()
    start_datetime = db.DateTimeProperty()
    end_datetime = db.DateTimeProperty()
    title = db.StringProperty()
    tagline = db.StringProperty()
    location = db.StringProperty()
    description = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    owner = db.StringProperty() #ReferenceProperty()
    committee = db.StringProperty() #ReferenceProperty()
    guests = db.StringProperty()
    
    def __unicode__(self):
        return self.title
    

# @see: "Creating a Flexible Monthly Calendar in Django" 
# http://journal.uggedal.com/creating-a-flexible-monthly-calendar-in-django

class EventCalendar(HTMLCalendar):
    
    def __init__(self): #, events):
        super(EventCalendar, self).__init__()
    
    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            #if date.today() == date(self.year, self.month, day):
            #    cssclass += ' today'
            return self.day_cell(cssclass, "&nbsp;", day)
        return self.day_cell('noday', None, None)
    
    def day_cell(self, cssclass, body, day):
        if not day is None:
            return '<td class="%s"><div class="cal_day">%s</div>%s</td>' % (cssclass, day, body)
        return '<td class="%s">&nbsp;</td>' % (cssclass)
