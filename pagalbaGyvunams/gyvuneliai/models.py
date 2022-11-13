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


GENDER = [
    ('Patinas', 'Patinas'),
    ('Patelė', 'Patelė'),
]


class Animal(models.Model):
    """
    Model for creating single animal in the DB
    """
    active = models.BooleanField(
        default=False,
        verbose_name=('Ar įrašas aktyvus? Taip/Ne'),
        help_text= ("Jeigu neuždėsi varnelės - įrašas nebus aktyvus, nebus matomas puslapyje"),
    )
    title = models.CharField(
        max_length=50,
        verbose_name=('Vardas'),
        help_text= ("Įrašyk gyvūnėlio vardą"),
    )
    breed = models.CharField(
        null=True,
        blank=True,
        max_length=200,
        verbose_name=('Veislė'),
        help_text= ("Įrašyk gyvūnėlio veislę"),
    )
    age = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=('Amžius'),
        help_text= ("Įrašyk gyvūnėlio amžių"),
    )
    weight = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=('Svoris'),
        help_text= ("Įrašyk gyvūnėlio svorį"),
    )
    sex = models.CharField(
        max_length=10,
        verbose_name=('Lytis'),
        choices = GENDER,
        default = 'Patinas',
    )
    description = models.CharField(
        max_length = 255,
        null=True,
        blank=True,
        help_text= ("Parašyk trumpą aprašymą apie gyvūnėlį"),
        verbose_name=('Apibūdink gyvūnėlio temperamentą'),
    )
    good_with_dogs = models.CharField(
        max_length = 100,
        verbose_name = ('Ar draugauja su šunimis?'),
        help_text= ("Trumpai"),
        null=True,
        blank=True,
    )
    good_with_cats = models.CharField(
        max_length = 100,
        verbose_name = ('Ar draugauja su katėmis?'),
        help_text= ("Trumpai"),
        null=True,
        blank=True,
    )
    adoption_donation = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=('Adoption mokestis(eur)'),
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
    story = RichTextField(
        null=True,
        blank=True,
        verbose_name=('Istorija'),
        help_text= ("Parašyk trumpą istoriją/aprašymą apie gyvūnėlį"),
    )

    # Tell how you want the info to be sorted and named in
    # django-admin panel. No need to re-migrate
    class Meta:
        ordering = ['-created']

    # Tell django how you want the title of the Blog_post item to be
    # represented in django-admin panel. No need to re-migrate
    def __str__(self):
        return self.title
