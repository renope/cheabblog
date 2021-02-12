from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=150, null=True, blank=True)
    facebook_url = models.CharField(max_length=150, null=True, blank=True)
    twitter_url = models.CharField(max_length=150, null=True, blank=True)
    instagram_url = models.CharField(max_length=150, null=True, blank=True)
    pinterest_url = models.CharField(max_length=150, null=True, blank=True)
    

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=150)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=150)
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.Datefield(auto_now=True)
    category = models.CharField(max_length=150, default='coding')
    snippet = models.CharField(max_length=150)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    # create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    # update_at = models.DateTimeField(_("Update at"), auto_now=True)
    # publish_time = models.DateTimeField(_("Publish at"), db_index=True)
