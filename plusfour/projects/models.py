from django.db import models


class Owner(models.Model):
    first = models.TextField()
    last = models.TextField()
    details = models.TextField()
    public_source_repository = models.URLField()


class Project(models.Model):
    name = models.TextField()
    icon_path = models.TextField()
    description = models.TextField()
    ranking = models.IntegerField()

    def __unicode__(self):
        return self.name


class Technology(models.Model):
    project = models.ManyToManyField(Project)
    framework = models.TextField()
    language = models.TextField()

    def __unicode__(self):
        return '{} {}'.format(self.framework, self.language)