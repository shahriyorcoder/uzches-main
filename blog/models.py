from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# News
class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news/')
    description = models.TextField()
    content = RichTextField()
    views = models.IntegerField(default=0)
    twitter_link = models.URLField()
    facebook_link = models.URLField()
    telegram_link = models.URLField()

    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(News, self).save(*args, **kwargs)


# Course
class Category(models.Model):
    title = models.CharField(max_length=250)
    course_count = models.IntegerField(default=0)

LANG = ( 
    ("Uz", "Uzbek"), 
    ("Ru", "Russian"), 
    ("En", "English"), 

) 
LEVEL = ( 
    ("Low", "Low"), 
    ("Middle", "Middle"), 
    ("High", "High"), 

) 
class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_saved = models.ForeignKey(User, on_delete=models.CASCADE,related_name='course_is_saved')
    is_purchased = models.ForeignKey(User, on_delete=models.CASCADE,related_name='course_is_purchased')
    is_completed = models.ForeignKey(User, on_delete=models.CASCADE,related_name='course_is_completed')
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    preview = models.ImageField(upload_to='preview/')
    is_free = models.BooleanField()
    has_discount = models.BooleanField()
    original_price = models.IntegerField(default=0)
    discount_price = models.IntegerField(default=0)
    language = models.CharField(choices=LANG,max_length=200)
    level = models.CharField(choices=LEVEL,max_length=200)
    average_rating = models.IntegerField(default=0)
    module_count = models.IntegerField(default=0)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.TextField()

class Module(models.Model):

    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    lesson_count = models.IntegerField(default=0)
    order = models.IntegerField(default=0)

class Lesson(models.Model):
    module = models.ForeignKey(Module,on_delete=models.CASCADE)
    is_watched = models.ForeignKey(User,on_delete=models.CASCADE)
    bookmark = models.ForeignKey(User,on_delete=models.CASCADE, related_name='bookmark')
    title = models.CharField(max_length=250)
    video_url = models.URLField()
    preview = models.ImageField(upload_to='lesson_preview/')
    description = RichTextField()
    order = models.IntegerField(default=0)
