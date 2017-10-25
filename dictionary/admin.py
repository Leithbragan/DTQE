from django.contrib import admin
from dictionary.models import *

# Register your models here.


admin.site.register(Word)
admin.site.register(Translation)
admin.site.register(UserDictionary)
