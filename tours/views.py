import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tour, Booking
from django.contrib import messages

def tour_list(request):
    tours = Tour.objects.all()
    # Convert tours to JSON for use in JS
    tours_json = json.dumps(list(tours.values('id', 'name', 'description', 'price', 'days')), default=str)
    
    return render(request, 'tour_list.html', {
        'tours': tours,
        'tours_json': tours_json
    })

def book_now(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)

    if request.method == 'POST':
        # Get form data from POST
        customer_name = request.POST.get('customer_name')
        email = request.POST.get('email')
        people = request.POST.get('people')
        payment_method = request.POST.get('payment_method')

        # Save booking to database
        Booking.objects.create(
            tour=tour,
            customer_name=customer_name,
            email=email,
            people=people,
            payment_method=payment_method
        )

        # Show success message
        messages.success(request, f"{tour.name} booked successfully!")
        return redirect('booking_history')

    # Optional: render separate booking form if needed
    return render(request, 'booking_form.html', {'tour': tour})

def booking_history(request):
    # Get all bookings ordered by newest first
    bookings = Booking.objects.all().order_by('-id')
    return render(request, 'booking_history.html', {'bookings': bookings})
