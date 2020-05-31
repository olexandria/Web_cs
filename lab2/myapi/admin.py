from django.contrib import admin

from .models import Library
from .models import Book
from .models import Course
from .models import Post, Like
# Register your models here.


admin.site.register(Library)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Book)
admin.site.register(Course)

