from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.TextField()
    author = models.ManyToManyField('Author', blank = True)
    publisher = models.ForeignKey('Publisher', on_delete = models.PROTECT, blank = True, null = True)
    publish_date = models.DateField(blank = True, null = True)
    ISBN = models.CharField(max_length = 13)
    page = models.IntegerField(blank = True, null = True)
    genre = models.ManyToManyField('GenreSub', blank = True)
    series = models.ManyToManyField('Series', blank = True)

    class Meta:
        verbose_name = '책'
        verbose_name_plural = '책'

    def __str__(self):
        return self.title

class Pricetag(models.Model):
    book = models.ForeignKey('Book', on_delete= models.CASCADE)
    price = models.IntegerField(blank = True, null = True)
    discountedPrice = models.IntegerField(blank = True, null = True) 
    company = models.ForeignKey('Company', on_delete = models.PROTECT)
    isDigital = models.BooleanField()
    isRental = models.BooleanField(default = False)

class Company(models.Model):
    name = models.TextField()


class Author(models.Model):
    name = models.TextField()
    originalName = models.TextField(blank = True)
    nationality = models.ForeignKey('Country', on_delete = models.PROTECT, blank = True, null = True)
    birth = models.DateTimeField(blank = True, null = True)

    class Meta:
        verbose_name = '작가'
        verbose_name_plural = '작가'

    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name = '시리즈'
        verbose_name_plural = '시리즈'

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name = '출판사'
        verbose_name_plural = '출판사'

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name = '장르'
        verbose_name_plural = '장르'

    def __str__(self):
        return self.name

class GenreSub(models.Model):
    name = models.TextField()
    parentGenre = models.ForeignKey('Genre', on_delete = models.PROTECT)

    class Meta:
        verbose_name = '하위장르'
        verbose_name_plural = '하위장르'

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name = '국적'
        verbose_name_plural = '국적'

    def __str__(self):
        return self.name

class Theme(models.Model):
    name = models.TextField()
    book = models.ManyToManyField('Book', blank = True)

    class Meta:
        verbose_name = '테마'
        verbose_name_plural = '테마'