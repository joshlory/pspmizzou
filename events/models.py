from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from calendar import HTMLCalendar
from itertools import groupby
from datetime import date

from committees.models import Committee

class Event(models.Model):
    #id = db.Key()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    title = models.CharField(max_length=127)
    tagline = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User) #models.CharField(max_length=127)
    committee = models.CharField(max_length=127) #models.ForeignKey(Committee)
    guests = models.ManyToManyField(User, related_name="attending", null=True)
    
    def get_absolute_url(self):
        return reverse('view_event', args=[self.id])
    
    def __unicode__(self):
        return self.title
    

# @see: "Creating a Flexible Monthly Calendar in Django" 
# http://journal.uggedal.com/creating-a-flexible-monthly-calendar-in-django

class EventCalendar(HTMLCalendar):
    
    def __init__(self, events):
        super(EventCalendar, self).__init__()
        self.setfirstweekday(6)
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
                        reverse('view_event', args=[event.id]) + "'>" +
                        self.truncate(event.title, 14) + "</a></p>")
                return self.day_cell(cssclass, ''.join(body), day)
            return self.day_cell(cssclass, "&nbsp;", day)
        return self.day_cell('noday', None, None)
    
    def day_cell(self, cssclass, body, day):
        if not day is None:
            return '<td class="%s"><div class="cal_day">%s</div>%s</td>' % \
                (cssclass, day, body)
        return '<td class="%s">&nbsp;</td>' % (cssclass)
