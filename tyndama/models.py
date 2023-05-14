from django.db import models

from .helper import  get_time




class Music(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    singer = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images_1')
    song = models.FileField(upload_to='images_1')
    album = models.CharField(max_length=255, default="-")
    time = models.CharField(max_length=50)

    def _str_(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.time:
            sec = get_time(self.song)
            audio_length = int(sec / 60)
            mode = int(sec - (audio_length * 60))
            print(mode)
            time = f"{audio_length}:{mode}"


            self.time = time

        return super().save(*args, **kwargs)



