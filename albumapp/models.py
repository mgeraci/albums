from django.db import models


class Album(models.Model):
  artist = models.CharField(max_length=200)
  name = models.CharField(max_length=200)
  year = models.PositiveSmallIntegerField()
  cover = models.ImageField(upload_to='covers', blank=True, null=True)
  sample = models.FileField(upload_to='samples', blank=True, null=True)

  class Meta:
    ordering = ['year', 'artist']

  def __unicode__(self):
    return '{} - {} - {}'.format(self.artist, self.year, self.name)


class AlbumList(models.Model):
  name = models.CharField(max_length=200)
  slug = models.SlugField(max_length=200, unique=True)

  class Meta:
    ordering = ['name']

  def __unicode__(self):
    return self.name


class AlbumSelection(models.Model):
  album_list = models.ForeignKey(AlbumList)
  album = models.ForeignKey(Album)
  position = models.PositiveSmallIntegerField(blank=True, null=True)
  description = models.TextField(blank=True)

  class Meta:
    ordering = ['position']

  def __unicode__(self):
    return '{}: {} - {}'.format(self.album_list, self.position, self.album)


class AlbumLink(models.Model):
  name = models.CharField(max_length=100)
  href = models.CharField(max_length=300)
  album = models.ForeignKey(Album)

  class Meta:
    ordering = ['name']

  def __unicode__(self):
    return '{} - {}'.format(self.album, self.name)
