from django.contrib import admin
from .models import Review, Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    ordering = ('-created_at',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    ordering = ('-created_at',)