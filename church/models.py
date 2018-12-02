from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Grouped(models.Model):
    group = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.group


class Member(models.Model):
    group = models.ForeignKey(Grouped, on_delete=models.CASCADE)
    member = models.CharField(max_length=30, blank=True)


class Pledge(models.Model):
    group = models.ForeignKey(Grouped, on_delete=models.CASCADE)
    person = models.CharField(max_length=30, unique=False, blank=True)
    pledge = models.TextField(blank=True)


class Tool(models.Model):
    group = models.ForeignKey(Grouped, on_delete=models.CASCADE)
    tool = models.FileField(upload_to='groups', blank=True)
    link = models.URLField(blank=True)
    description = models.CharField(max_length=200, blank=True)


class Staff(models.Model):
    full_name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    message = models.TextField()
    image = models.ImageField(upload_to='profile_pics')
    tel = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.full_name


class Service(models.Model):
    service = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.service


class signUp(models.Model):
    SEX_CHOICES = (('M', 'Male'), ('F', 'Female'))
    RSHIP_CHOICES = (
        ('single', 'Single'),
        ('In a Relationship', (
            ('dating', 'Dating'),
            ('engaged', 'Engaged'),
            ('married', 'Married')
        )
         )
    )
    NATIONALITY_CHOICES = (
        ('Ugandan', 'Ugandan'),
        ('Kenyan', 'Kenyan'),
        ('Tanzanian', 'Tanzanian'),
        ('Rwandese', 'Rwandese'),
        ('Sudanese', 'Sudanese'),
        ('Indian', 'Indian'),
        ('Somalese', 'Somalese'),
        ('American', 'American'),
        ('British', 'British'),
        ('French', 'French'),
        ('Russian', 'Russian'),
        ('Congolese', 'Congolese'),
        ('Nigerian', 'Nigerian'),
        ('German', 'German'),
        ('South African', 'South African')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30, primary_key=True)
    gender = models.CharField(max_length=1, choices=SEX_CHOICES, default=' ')
    nationality = models.CharField(max_length=20, choices=NATIONALITY_CHOICES, default='uganda')
    address = models.TextField(default=' ')
    relationship_status = models.CharField(max_length=10, choices=RSHIP_CHOICES, default='single')
    profile = models.TextField(default='Tell us about yourself')
    tel_number = models.IntegerField(default=256)
    occupation = models.CharField(max_length=20, default=' ')
    profile_picture = models.ImageField(upload_to='profile_pics')
    terms_and_conditions = models.TextField(default='1.We are a strictly anglican church group')
    agree_with_terms_and_conditions = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('church:profile', kwargs={'username': self.user.username})

    def __str__(self):
        return self.full_name


class chosenGroup(models.Model):
    user = models.ForeignKey(signUp, on_delete=models.CASCADE)
    group = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('church:detailgroup', kwargs={'group': self.group})


class serviceTool(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, unique=False)
    title = models.CharField(max_length=200, blank=True)
    item = models.URLField()

    def __str__(self):
        return self.item


class Event(models.Model):
    person_in_charge = models.CharField(max_length=30)
    event = models.CharField(max_length=255, primary_key=True)
    poster = models.ImageField(upload_to='posters', blank=True)
    date = models.DateTimeField(unique=False)
    description = models.TextField()
    venue = models.CharField(max_length=100)
    google_maps = models.ImageField(upload_to='maps')

    def get_absolute_url(self):
        return reverse('church:eventstaff')

    def __str__(self):
        return self.event


class attendanceList(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    person = models.CharField(max_length=30)


class eventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to='pics', blank=True)
    description = models.CharField(max_length=300, blank=True)


class Image(models.Model):
    group = models.ForeignKey(Grouped, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics', blank=True)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.description


class Video(models.Model):
    video = models.FileField(upload_to='vids')
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.description


class Audio(models.Model):
    audio = models.FileField(upload_to='audios')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class Document(models.Model):
    doc = models.FileField(upload_to='docs')
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class Comment(models.Model):
    topic = models.ForeignKey(Event, unique=False, on_delete=models.CASCADE)
    person = models.CharField(max_length=30)
    query = models.TextField(primary_key=True, max_length=255, unique=False)

    def __str__(self):
        return self.query


class Responses(models.Model):
    query = models.ForeignKey(Comment, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30, default=' ', blank=True)
    answer = models.TextField(blank=True)

    def __str__(self):
        return self.answer


class Message(models.Model):
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.message


class New(models.Model):
    title = models.CharField(max_length=500,primary_key=True)
    details = models.TextField()

    def __str__(self):
        return self.title

class newsImages(models.Model):
    title = models.ForeignKey(New,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics')
