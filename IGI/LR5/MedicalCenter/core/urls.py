from django.urls import path
from .views import (
    HomeView,
    ServiceListView,
    DoctorDetailView,
    AboutView,
    DoctorListView,
    NewsListView,
    NewsDetailView,
    GlossaryListView,
    ContactsView,
    PrivacyPolicyView,
    VacancyListView,
    ListView,
    Review,
    ReviewCreateView,
    PromoCodeListView,
    TemplateView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('services/', ServiceListView.as_view(), name='services'),
    path('doctors/', DoctorListView.as_view(), name='doctors'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('about/', AboutView.as_view(), name='about'), 
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('glossary/', GlossaryListView.as_view(), name='glossary'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('privacy/', TemplateView.as_view(template_name='core/privacy_policy.html'), name='privacy-policy'),
    path('vacancies/', VacancyListView.as_view(), name='vacancies'),
    path('reviews/', ListView.as_view(model=Review, template_name='core/reviews.html'), name='reviews'),
    path('add-review/', ReviewCreateView.as_view(), name='add-review'),
    path('promocodes/', PromoCodeListView.as_view(), name='promocodes'),
]