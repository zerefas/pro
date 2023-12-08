from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from multiselectfield import MultiSelectField

# Create your models here.


class Movie(models.Model):

    Category=(

        ('action','ACTION'),
        ('drama', 'DRAMA'),
        ('comedy', 'COMEDY'),
        ('animated', 'ANIMATED'),

    )

    Language=(
        ('english','ENGLISH'),
        ('hindi', 'HINDI'),
    )

    Status =(
        ('recently','RECENTLY WATCH'),
        ('most','MOST WATCHED'),
        ('top','TOP RATED')
    )

    title = models.CharField(max_length=150,null=True)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(choices=Category ,max_length=10)
    language = models.CharField(max_length=10,choices=Language)
    status = models.CharField(max_length=10,choices=Status)
    cast = models.CharField(max_length=150 ,null=True,blank=True)
    year_of_production = models.DateField()
    view_count = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, null=True)
    movie_trailer = models.ImageField(upload_to='movies')
    created_date = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)




    def __str__(self):
        return self.title



Link_Choice =(

    ('D', 'Download_Link'),
    ('W', 'Watch_Link')

)


class Movielink(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    type= models.CharField(choices=Link_Choice, max_length=1)
    link = models.URLField()


    def __str__(self):
        return str(self.movie)