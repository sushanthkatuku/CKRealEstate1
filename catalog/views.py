from .models import Property, Neighborhood, PropertyType
from django.shortcuts import render

def index(request):
    """View function for the home page of the site."""
    num_properties = Property.objects.all().count()

    # Count the number of available property listings
    num_available_properties = Property.objects.filter(property_status='available').count()

    # Get the current featured property
    featured_property = Property.objects.filter(property_is_featured=True).first()

    context = {
        'num_properties': num_properties,
        'num_available_properties': num_available_properties,
        'featured_property': featured_property,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)



def home(request):
    return render(request, 'home.html')

def listings(request):
    properties = Property.objects.all()
    return render(request, 'listings.html', {'listings': properties})

from .models import OwnerProfile

def owner_profile(request):
    owner_id = request.session.get('owner_id')

    # Fetch the owner profile using filter
    if owner_id:
        owner = OwnerProfile.objects.filter(id=owner_id).first()  # Get the owner by ID
    else:
        owner = OwnerProfile.objects.first()  # Fetch the first owner if no ID in session
        if owner:
            request.session['owner_id'] = owner.id  # Store the owner's ID in the session

    return render(request, 'owner_profile.html', {'owner': owner})


def contact_property(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    message_sent = False

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Compose the email
        subject = f"Property Inquiry: {property_obj.name}"
        body = (
            f"Name: {name}\n"
            f"Email: {email}\n\n"
            f"Message:\n{message}"
        )

        # Send the email to the property's contact email
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,  # Your email from settings.py
            [property_obj.contact_email],
        )
        message_sent = True

    return render(request, 'contact_property.html', {
        'property': property_obj,
        'message_sent': message_sent
    })

