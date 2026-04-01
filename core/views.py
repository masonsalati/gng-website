from django.shortcuts import render, redirect
from django.conf import settings

from .models import Review, Booking
from .forms import ReviewForm, BookingForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "booking.html", {"success": True, "form": BookingForm()})
    else:
        form = BookingForm()

    return render(request, "booking.html", {"form": form})


def review(request):
    reviews = Review.objects.all().order_by('-created_at')

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review')
    else:
        form = ReviewForm()

    return render(request, "review.html", {
        'form': form,
        'reviews': reviews,
    })