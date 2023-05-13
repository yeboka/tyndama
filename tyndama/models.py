from django.db import models


class Music(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    singer = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images_1')
    song = models.FileField(upload_to='images_1')

    def _str_(self):
        return self.name
