from django.db import models
class WebsiteCommon(models.Model):
    brand = models.CharField(max_length=255)
    copyright_text = models.CharField(max_length=255)
    subscribe_text = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.brand)

class HeaderSection(models.Model):
    background_image = models.ImageField(upload_to="header/")
    main_title = models.CharField(max_length=255)
    sub_title = models.TextField()
    button_text = models.CharField(max_length=255, null=True, blank=True)
    button_link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.main_title)

class Menu(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    def __str__(self):
        return"{}".format(self.name)

    class Meta:
        ordering = ("order",)


class Projects(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    picture = models.ImageField(upload_to="projects/")

    def __str__(self):
        return"{}".format(self.title)


class AboutSection(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    picture = models.ImageField(upload_to="about/")

    def __str__(self):
        return "{}".format(self.title)

class Contact(models.Model):
    icon = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return "{}".format(self.title)

class FooterIcon(models.Model):
    link = models.CharField(max_length=255)
    name = models.CharField("icon",max_length=255)

    def __str__(self):
        return "{}".format(self.name)

class Subscription(models.Model):
    email = models.EmailField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    # background_image = models.ImageField(upload_to="Subscription/")

    def __str__(self):
        return "{}".format(self.email)

# Create your models here.
