from django.urls import path
from .views import HomeView, Documentations, Kontakt, Blog, Zamena

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('doc/', Documentations.as_view(), name='doc'),
    path('blog/', Blog.as_view(), name='blog'),
    path('contacts/', Kontakt.as_view(), name='contact'),
    path('blog/zamena-tindera/', Zamena.as_view(), name='zamena'),
    # Add more URL patterns as needed
]