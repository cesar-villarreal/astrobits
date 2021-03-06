from django.db import models

# Create your models here.

#class Julian(models.Model):
	#date_to_jd = models.DateTimeField()
	#jd_to_date = models.FloatField()

class Picture(models.Model):
	picture_url = models.CharField(max_length=150)
	picture_thumbnail = models.CharField(max_length=150)
	picture_description = models.CharField(max_length=200)


#class Circuits(models.Model):
    #circuitid = models.AutoField(db_column='circuitId', primary_key=True)  # Field name made lowercase.
    #circuitref = models.CharField(db_column='circuitRef', max_length=255)  # Field name made lowercase.
    #name = models.CharField(max_length=255)
    #location = models.CharField(max_length=255, blank=True, null=True)
    #country = models.CharField(max_length=255, blank=True, null=True)
    #lat = models.FloatField(blank=True, null=True)
    #lng = models.FloatField(blank=True, null=True)
    #alt = models.IntegerField(blank=True, null=True)
    #url = models.CharField(unique=True, max_length=255)

    #class Meta:
        #managed = True
        #db_table = 'circuits'


class Constructorresults(models.Model):
    constructorresultsid = models.AutoField(db_column='constructorResultsId', primary_key=True)  # Field name made lowercase.
    raceid = models.IntegerField(db_column='raceId')  # Field name made lowercase.
    constructorid = models.IntegerField(db_column='constructorId')  # Field name made lowercase.
    points = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'constructorResults'


#class Constructorstandings(models.Model):
    #constructorstandingsid = models.AutoField(db_column='constructorStandingsId', primary_key=True)  # Field name made lowercase.
    #raceid = models.IntegerField(db_column='raceId')  # Field name made lowercase.
    #constructorid = models.IntegerField(db_column='constructorId')  # Field name made lowercase.
    #points = models.FloatField()
    #position = models.IntegerField(blank=True, null=True)
    #positiontext = models.CharField(db_column='positionText', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #wins = models.IntegerField()

    #class Meta:
        #managed = True
        #db_table = 'constructorStandings'


class Constructors(models.Model):
    constructorid = models.AutoField(db_column='constructorId', primary_key=True)  # Field name made lowercase.
    constructorref = models.CharField(db_column='constructorRef', max_length=255)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=255)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'constructors'


class Driverstandings(models.Model):
    driverstandingsid = models.AutoField(db_column='driverStandingsId', primary_key=True)  # Field name made lowercase.
    raceid = models.IntegerField(db_column='raceId')  # Field name made lowercase.
    driverid = models.IntegerField(db_column='driverId')  # Field name made lowercase.
    points = models.FloatField()
    position = models.IntegerField(blank=True, null=True)
    positiontext = models.CharField(db_column='positionText', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wins = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'driverStandings'


class Drivers(models.Model):
    driverid = models.AutoField(db_column='driverId', primary_key=True)  # Field name made lowercase.
    driverref = models.CharField(db_column='driverRef', max_length=255)  # Field name made lowercase.
    number = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=3, blank=True, null=True)
    forename = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    dob = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'drivers'


#class Laptimes(models.Model):
    #raceid = models.IntegerField(db_column='raceId', primary_key=True)  # Field name made lowercase.
    #driverid = models.IntegerField(db_column='driverId')  # Field name made lowercase.
    #lap = models.IntegerField()
    #position = models.IntegerField(blank=True, null=True)
    #time = models.CharField(max_length=255, blank=True, null=True)
    #milliseconds = models.IntegerField(blank=True, null=True)

    #class Meta:
        #managed = True
        #db_table = 'lapTimes'
        #unique_together = (('raceid', 'driverid', 'lap'),)


#class Pitstops(models.Model):
    #raceid = models.IntegerField(db_column='raceId', primary_key=True)  # Field name made lowercase.
    #driverid = models.IntegerField(db_column='driverId')  # Field name made lowercase.
    #stop = models.IntegerField()
    #lap = models.IntegerField()
    #time = models.TimeField()
    #duration = models.CharField(max_length=255, blank=True, null=True)
    #milliseconds = models.IntegerField(blank=True, null=True)

    #class Meta:
        #managed = True
        #db_table = 'pitStops'
        #unique_together = (('raceid', 'driverid', 'stop'),)


#class Qualifying(models.Model):
    #qualifyid = models.AutoField(db_column='qualifyId', primary_key=True)  # Field name made lowercase.
    #raceid = models.IntegerField(db_column='raceId')  # Field name made lowercase.
    #driverid = models.IntegerField(db_column='driverId')  # Field name made lowercase.
    #constructorid = models.IntegerField(db_column='constructorId')  # Field name made lowercase.
    #number = models.IntegerField()
    #position = models.IntegerField(blank=True, null=True)
    #q1 = models.CharField(max_length=255, blank=True, null=True)
    #q2 = models.CharField(max_length=255, blank=True, null=True)
    #q3 = models.CharField(max_length=255, blank=True, null=True)

    #class Meta:
        #managed = True
        #db_table = 'qualifying'


class Races(models.Model):
    raceid = models.AutoField(db_column='raceId', primary_key=True)  # Field name made lowercase.
    year = models.IntegerField()
    round = models.IntegerField()
    circuitid = models.IntegerField(db_column='circuitId')  # Field name made lowercase.
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    url = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'races'


#class Results(models.Model):
    #resultid = models.AutoField(db_column='resultId', primary_key=True)  # Field name made lowercase.
    #raceid = models.IntegerField(db_column='raceId')  # Field name made lowercase.
    #driverid = models.IntegerField(db_column='driverId')  # Field name made lowercase.
    #constructorid = models.IntegerField(db_column='constructorId')  # Field name made lowercase.
    #number = models.IntegerField(blank=True, null=True)
    #grid = models.IntegerField()
    #position = models.IntegerField(blank=True, null=True)
    #positiontext = models.CharField(db_column='positionText', max_length=255)  # Field name made lowercase.
    #positionorder = models.IntegerField(db_column='positionOrder')  # Field name made lowercase.
    #points = models.FloatField()
    #laps = models.IntegerField()
    #time = models.CharField(max_length=255, blank=True, null=True)
    #milliseconds = models.IntegerField(blank=True, null=True)
    #fastestlap = models.IntegerField(db_column='fastestLap', blank=True, null=True)  # Field name made lowercase.
    #rank = models.IntegerField(blank=True, null=True)
    #fastestlaptime = models.CharField(db_column='fastestLapTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #fastestlapspeed = models.CharField(db_column='fastestLapSpeed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    #statusid = models.IntegerField(db_column='statusId')  # Field name made lowercase.

    #class Meta:
        #managed = True
        #db_table = 'results'


#class Seasons(models.Model):
    #year = models.IntegerField(primary_key=True)
    #url = models.CharField(unique=True, max_length=255)

    #class Meta:
        #managed = True
        #db_table = 'seasons'


#class Status(models.Model):
    #statusid = models.AutoField(db_column='statusId', primary_key=True)  # Field name made lowercase.
    #status = models.CharField(max_length=255)

    #class Meta:
        #managed = True
        #db_table = 'status'
