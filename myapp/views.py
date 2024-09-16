from django.shortcuts import redirect
from django.utils.translation import activate
from django.utils.translation import get_language_from_request
from django.urls import reverse
from django.shortcuts import render, redirect
# from django.utils.translation import LANGUAGE_SESSION_KEY




# Create your views here.
def home(request):
    return render(request, 'index.html')



def switch_language(request, lang_code):
    # Validate the language code to ensure it's a supported language
    if lang_code in ['en', 'hi', 'es', 'fr', 'de']:  # List all your supported languages
        activate(lang_code)
       # request.session[LANGUAGE_SESSION_KEY] = lang_code

    # Get the URL of the page the user was on before switching the language
    # You might want to use `request.META.get('HTTP_REFERER')` to get the referring URL
    # or redirect to a specific URL if needed.
    next_url = request.META.get('HTTP_REFERER', '/')

    # Redirect back to the referring page or the home page
    return redirect(next_url)