from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse
from meet.form import ContactForm


class HomeView(TemplateView):
    template_name = 'index.html'


class Documentations(TemplateView):
    template_name = 'docsument/document.html'


class Kontakt(TemplateView):
    template_name = 'contacts/index.html'


class Blog(TemplateView):
    template_name = 'blog/index.html'


class Zamena(TemplateView):
    template_name = 'zam/index.html'


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            theme = form.cleaned_data['theme']
            message = form.cleaned_data['message']

            subject = f"New message from {name}"
            message_body = f"Name: {name}\nEmail: {email}\n Theme:{theme}\n\nMessage:\n{message}"

            send_mail(subject, message_body, email, ['tuudelepp@shouu.cf'])
            return HttpResponseRedirect(reverse('success_page'))  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'contacts/index.html', {'form': form})