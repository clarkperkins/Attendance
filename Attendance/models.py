from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Organization(models.Model):
    name = models.CharField("Name", max_length=100, unique=True)
    members = models.ManyToManyField(User)

    def __unicode__(self):
        numMembers = len(self.members.all())
        if numMembers is 1:
            return u"%s: 1 member" % self.name
        else:
            return u"%s: %s members" % (self.name, str(numMembers))


class Meeting(models.Model):
    organization = models.ForeignKey(Organization)
    name = models.CharField("Name", max_length=100)
    date = models.DateField("Date")

    def __unicode__(self):
        return u"%s on %s" % (self.name, self.date)

ATTENDANCE_TYPES = (
    ('P', 'Present'),
    ('U', 'Unexcused'),
    ('E', 'Excused'),
    ('L', 'Late'),
)

ATTENDANCE_VERBS = {
    'Present':'at',
    'Unexcused':'from',
    'Excused':'from',
    'Late':'to',
    '':'',
}

class AttendanceRecord(models.Model):
    meeting = models.ForeignKey(Meeting)
    user = models.ForeignKey(User)
    status = models.CharField("", max_length=10, choices=ATTENDANCE_TYPES)

    def __unicode__(self):
        return "%s was %s %s %s" % (self.user, self.status, ATTENDANCE_VERBS[self.status], self.meeting)
