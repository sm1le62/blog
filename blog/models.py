from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(default="Описание")
    keywords = models.CharField(max_length=120, default="Ключевые слова")
    image = models.FileField(null=True, blank=True)
    content = models.TextField()
    visible = models.BooleanField(default=1)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/" %(self.id)

    class Meta:
        ordering = ["-id", "-timestamp"]
