from django.contrib import admin
from .models import *

admin.site.register(News)
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Lesson)
admin.site.register(Module)
admin.site.register(Comment)