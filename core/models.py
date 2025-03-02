from django.db import models


class Feedback(models.Model):
    name_surname = models.CharField(max_length=255)
    text = models.TextField()
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)

    def __str__(self):
        return f"{self.name_surname} - {self.subject}"


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    text = models.TextField()


class MainService(models.Model):
    service_name = models.CharField(max_length=255)
    service_text = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)

    def __str__(self):
        return self.service_name


class Statistics(models.Model):
    experience_years = models.PositiveIntegerField()
    technician_number = models.PositiveIntegerField()
    satisfied_clients = models.PositiveIntegerField()
    complete_projects = models.PositiveIntegerField()

    def __str__(self):
        return f"Stats: {self.experience_years} years," \
               f" {self.technician_number} techs," \
               f" {self.satisfied_clients} clients," \
               f" {self.complete_projects} projects"


class ContactInformation(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.address} | {self.email} | {self.phone}"
