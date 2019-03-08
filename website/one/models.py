from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Upload(models.Model):
    title = models.CharField(max_length = 30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UploadFragment(models.Model):
    file = models.FileField()
    upload = models.ForeignKey(Upload, related_name="files", on_delete=models.CASCADE)
