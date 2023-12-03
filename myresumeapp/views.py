from django.shortcuts import render
# yourapp/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse

def index(request):
    return render(request, 'index.html')
def portfolio(request):
    return render(request, 'portfolio_details.html')

# views.py

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Replace this with your actual email address
        to_email = 'lutayisirealex256@gmail.com'

        # Construct the email message
        email_message = f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message}"

        try:
            # Send the email
            send_mail(
                'Resume App',
                email_message,
                email,
                [to_email],
                fail_silently=False,
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'error_message': str(e)})

    # If not a POST request, redirect to the home page or display an error
    return JsonResponse({'status': 'error', 'error_message': 'Invalid request method'})
