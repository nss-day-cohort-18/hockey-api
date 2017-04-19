from django.db import models

# Create your models here.



class HockeyTeam(models.Model):
    teamname = models.CharField(max_length=44)
    logo = models.FilePathField(path="/static/logos")
    city = models.CharField(max_length=255)
    coach = models.CharField(max_length=55)
    mascot = models.CharField(max_length=55)

    def __str__(self):
        return self.teamname


class HockeyPlayer(models.Model):
    playername = models.CharField(max_length=55)
    position = models.CharField(max_length=20)
    team = models.ForeignKey(HockeyTeam, related_name='players')



class Cohort(models.Model):
    designator = models.CharField(max_length=4)
    start_date = models.DateField()
    graduation_date = models.DateField()
    website = models.CharField(max_length=255)





