from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from .models import Review
from .forms import ReviewForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def booking(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        try:
            send_mail(
                subject="New Booking Request",
                message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}",
                from_email=None,  # uses DEFAULT_FROM_EMAIL from settings.py
                recipient_list=["glassngutter@gmail.com"],
                fail_silently=False,
            )
            return render(request, "booking.html", {"success": True})
        except Exception as e:
            return render(request, "booking.html", {"error": "Failed to send email. Please try again later."})

    return render(request, "booking.html")


def review(request):
    reviews = Review.objects.all().order_by('-created_at')

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()

            try:
                send_mail(
                    subject="Thank You for Your Review!",
                    message=f"Hi {review.name},\n\nThank you for your review of GnG! We appreciate your support.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[review.email],
                    fail_silently=False,
                )
            except Exception:
                pass  # Don't block the redirect if the thank-you email fails

            return redirect('review')
    else:
        form = ReviewForm()

    return render(request, "review.html", {
        'form': form,
        'reviews': reviews,
    })