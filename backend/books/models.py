from django.db import models

# Create your models here.
class Book(models.Model):
    book_number = models.AutoField(primary_key = True)
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

class Author(models.Model):
    author_number = models.AutoField(primary_key = True)
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
    series_number = models.AutoField(primary_key = True)
    name = models.TextField()

    class Meta:
        verbose_name = '시리즈'
        verbose_name_plural = '시리즈'

    def __str__(self):
        return self.name

class Publisher(models.Model):
    publisher_number = models.AutoField(primary_key = True)
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

# 이후에 책의 시리즈를 정리하는 Series 모델 만들기