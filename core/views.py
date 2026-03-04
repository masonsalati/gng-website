from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')

def review(request):
    return render(request, 'review.html')


from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect

def booking(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        send_mail(
            subject="New Booking Request",
            message=f"""
Name: {name}
Email: {email}
Phone: {phone}
Message: {message}
""",
            from_email=None,  # IMPORTANT: uses DEFAULT_FROM_EMAIL from settings.py
            recipient_list=["glassngutter@gmail.com"],
            fail_silently=False,
        )

        return render(request, "booking.html", {"success": True})

    return render(request, "booking.html")

from .models import Review
from .forms import ReviewForm

def review(request):
    reviews = Review.objects.all().order_by('-created_at')

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()

            # Send thank-you email
            send_mail(
                "Thank You for Your Review!",
                "Hi {},\n\nThank you for your review of GnG! We appreciate your support.".format(review.name),
                settings.EMAIL_HOST_USER,
                [review.email],
                fail_silently=False,
            )

            return redirect('review')
    else:
        form = ReviewForm()

    return render(request, "review.html", {
        'form': form,
        'reviews': reviews
    })