from django.contrib import admin
from .models import quote

# Register your models here.
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phone', 'message')

admin.site.register(quote, QuoteAdmin)
