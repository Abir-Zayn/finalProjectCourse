from django.contrib import admin
from .models import *

admin.site.register(books)
admin.site.register(loan)
admin.site.register(returnbook)
admin.site.register(Profile)
admin.site.register(wishlist)