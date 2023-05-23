from django.db import models


class User(models.Model):
  name = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  company = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.name}"


class Lead(models.Model):
  lead_name = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  address = models.TextField(null=True)
  monthlySale = models.CharField(max_length=255)
  dailySale = models.CharField(max_length=255)
  yearlySale = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.lead_name}"


class Activity(models.Model):
  activity_name = models.CharField(max_length=255)
  description = models.TextField(null=True)
  owner = models.CharField(max_length=255)
  company = models.CharField(max_length=255)
  status = models.CharField(max_length=255)
  dateType = models.CharField(max_length=255)
  createdDate = models.DateField(null=True)

  def __str__(self):
    return f"{self.activity_name}"


class Contact(models.Model):
  contacted_name = models.CharField(max_length=255)
  description = models.TextField(null=True)
  note = models.TextField(null=True)
  type = models.CharField(max_length=255)
  date = models.DateField(null=True)

  def __str__(self):
    return f"{self.contacted_name}"
