from django.db import models

class Colleges(models.Model):
    title = models.CharField(max_length=30)


class Majores(models.Model):
    title = models.CharField(max_length=30)


class Expertises(models.Model):
    title = models.CharField(max_length=30)


class Hindexs(models.Model):
    title = models.CharField(max_length=30)
