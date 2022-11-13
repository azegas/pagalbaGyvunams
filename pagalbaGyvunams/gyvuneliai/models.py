from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Tag(models.Model):
    """
    Model for Cat/dog tag, later used in Animal model
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    
class Animal(models.Model):
    """
    Model for creating single animal in the DB
    """
    title = models.CharField(
        max_length=200,
        verbose_name=('vardas'),
        help_text= ("Įrašyk gyvūnėlio vardą"),
    )
    description = RichTextField(
        null=True,
        blank=True,
        help_text= ("Parašyk trumpą aprašymą apie gyvūnėlį"),
        verbose_name=('Apie gyvunėlį'),
    )
    active = models.BooleanField(
        default=False,
        verbose_name=('Ar įrašas aktyvus? Taip/Ne'),
        help_text= ("Jeigu neuždėsi varnelės - įrašas nebus aktyvus, nebus matomas puslapyje"),
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    tags = models.ForeignKey(
        Tag,
        default=1,
        on_delete=models.SET_DEFAULT, # if deleting a tag, all posts
                                      # with that tag WONT be deleted,
                                      # only a default tag will be
                                      # applied
        verbose_name=('Šuo/Katė'),
    )
    photo = models.ImageField(
        upload_to="photo/%Y/%m%d",
        blank=True,
        verbose_name=('Nuotrauka'),
        help_text= ("Išrink ir įkelk gražiausią mažuliuko nuotrauką"),
    )

    # Tell how you want the info to be sorted and named in
    # django-admin panel. No need to re-migrate
    class Meta:
        ordering = ['-created']

    # Tell django how you want the title of the Blog_post item to be
    # represented in django-admin panel. No need to re-migrate
    def __str__(self):
        return self.title
