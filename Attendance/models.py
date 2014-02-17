from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Organization(models.Model):
    name = models.CharField("Name", max_length=100, unique=True)
    members = models.ManyToManyField(User)
    admin = models.ForeignKey(User, related_name="admin_of_set")

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
    ('present', 'Present'),
    ('unexcused', 'Unexcused'),
    ('excused', 'Excused'),
    ('late', 'Late'),
)

ATTENDANCE_PRONOUNS = {
    'present': 'at',
    'unexcused': 'from',
    'excused': 'from',
    'late': 'to',
    '': '',
}

class AttendanceRecord(models.Model):
    meeting = models.ForeignKey(Meeting)
    user = models.ForeignKey(User)
    status = models.CharField("", max_length=10, choices=ATTENDANCE_TYPES)

    def __unicode__(self):
        return "%s %s was %s %s %s" % (self.user.first_name, self.user.last_name, self.status, ATTENDANCE_PRONOUNS[self.status], self.meeting)
