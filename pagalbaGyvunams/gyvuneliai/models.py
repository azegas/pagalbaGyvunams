from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    
class Animal(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(null=True, blank=True)
    # content = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=False)
    photo = models.ImageField(upload_to="photo/%Y/%m%d", blank=True)

    # Tell how you want the info to be sorted and named in
    # django-admin panel. No need to re-migrate
    class Meta:
        ordering = ['-created']

    # Tell django how you want the title of the Blog_post item to be
    # represented in django-admin panel. No need to re-migrate
    def __str__(self):
        return self.title
