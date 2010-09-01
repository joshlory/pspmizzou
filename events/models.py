from appengine_django.models import BaseModel
from django.core.urlresolvers import reverse

from google.appengine.ext import db
from calendar import HTMLCalendar
from itertools import groupby
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
    
    def __init__(self, events):
        super(EventCalendar, self).__init__()
        self.events = self.by_day(events)
    
    def by_day(self, events):
        field = lambda event: event.start_datetime.day
        return dict(
            [(day, list(items)) for day, items in groupby(events, field)]
        )
        
    def truncate(self, str, num_letters):
        if len(str) <= num_letters:
            return str
        return str[0:num_letters] + "&hellip;"
    
    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(EventCalendar, self).formatmonth(year, month)
    
    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'
            if day in self.events:
                body = []
                for event in self.events[day]:
                    body.append("<p><a href='" + 
                        reverse('view_event', args=[event.key()]) + "'>" +
                        self.truncate(event.title, 14) + "</a></p>")
                return self.day_cell(cssclass, ''.join(body), day)
            return self.day_cell(cssclass, "&nbsp;", day)
        return self.day_cell('noday', None, None)
    
    def day_cell(self, cssclass, body, day):
        if not day is None:
            return '<td class="%s"><div class="cal_day">%s</div>%s</td>' % \
                (cssclass, day, body)
        return '<td class="%s">&nbsp;</td>' % (cssclass)
