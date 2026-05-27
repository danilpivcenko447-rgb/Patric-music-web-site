from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.artist} - {self.title}"

class Track(models.Model):
    title = models.CharField(max_length=200)
    audio = models.FileField(upload_to='tracks/')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')

    def __str__(self):
        return self.title


class UserLibrary(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'track']

