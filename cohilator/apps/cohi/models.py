from enum import Enum

from django.db.models import Model, CharField, ForeignKey, PROTECT, PositiveIntegerField, DateField, TextField, \
    DateTimeField, NullBooleanField, DurationField, IntegerField


class BrewType(Model):
    name = CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Continent(Enum):
    AFRICA = 1
    ASIA_TEMPERATE = 2
    ASIA_TROPICAL = 3
    AUSTRALASIA = 4
    EUROPE = 5
    PACIFIC = 6
    NORTH_AMERICA = 7
    CENTRAL_AMERICA = 8
    SOUTH_AMERICA = 9

    @staticmethod
    def choices():
        return ((v.value, v.name) for v in list(Continent))


class Country(Model):
    name = CharField(max_length=500, unique=True)
    continent = PositiveIntegerField(choices=Continent.choices())

    def __str__(self):
        return self.name


class Producer(Model):
    name = CharField(max_length=500, unique=True)
    country = ForeignKey(Country, on_delete=PROTECT)

    def __str__(self):
        return self.name


class Roaster(Model):
    name = CharField(max_length=500, unique=True)
    country = ForeignKey(Country, on_delete=PROTECT)

    def __str__(self):
        return self.name


class Package(Model):
    name = CharField(max_length=500)
    producer = ForeignKey(Producer, on_delete=PROTECT, null=True)
    roaster = ForeignKey(Roaster, on_delete=PROTECT, null=True)
    volume = PositiveIntegerField(default=250, help_text='in gram')
    roasted_on = DateField(null=True, blank=True)
    opened_on = DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return '{} ({})'.format(self.name, self.roasted_on)


class Grinder(Model):
    name = CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name


class Technique(Model):
    name = CharField(max_length=500)

    def __str__(self):
        return self.name


class Brew(Model):
    type = ForeignKey(BrewType, on_delete=PROTECT)
    package = ForeignKey(Package, on_delete=PROTECT)
    grinder = ForeignKey(Grinder, on_delete=PROTECT)
    grinder_setting = CharField(max_length=200)
    volume_beans = PositiveIntegerField(help_text='in gram')
    volume_water = PositiveIntegerField(help_text='in gram')
    temperature = PositiveIntegerField(help_text='in Celsius')
    extraction_time = DurationField(default='00:MM:ss', help_text='as HH:MM:ss')
    technique = ForeignKey(Technique, on_delete=PROTECT)
    description = TextField()
    remark = TextField()
    rating = IntegerField(default=0, help_text='use negative values for bad, positive for good results')

    brewed_on = DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} ({})'.format(self.package.name, self.type.name)
