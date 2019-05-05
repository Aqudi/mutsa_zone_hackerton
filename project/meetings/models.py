from django.db import models

# Create your models here.
class Meeting(models.Model):
    objects = models.Manager()

    category = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    min_number = models.IntegerField()
    max_number = models.IntegerField()
    current_number = models.IntegerField(default=0)
    meeting_time = models.CharField(max_length=200)
    meeting_place = models.CharField(max_length=200)
    description = models.TextField()
    writer_email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    view_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_add=True)


class Participant(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    motive = models.TextField()

    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_add=True)