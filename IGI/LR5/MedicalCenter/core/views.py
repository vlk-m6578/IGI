from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import News, GlossaryTerm, Employee, Vacancy, Review, PromoCode, Doctor, Service
from .forms import ReviewForm
from django.urls import reverse_lazy
from .filters import ServiceFilter
from django.utils import timezone

class HomeView(ListView):
    template_name = 'core/home.html'
    context_object_name = 'latest_news'
    
    def get_queryset(self):
        return News.objects.order_by('-publish_date')[:3]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['glossary_terms'] = GlossaryTerm.objects.all()[:5]
        return context
    
class ServiceListView(ListView):
    model = Service
    paginate_by = 10
    filterset_class = ServiceFilter
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ServiceFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'

class DoctorListView(ListView):
    model = Doctor
    template_name = 'core/doctors.html'
    context_object_name = 'doctors'
    paginate_by = 10

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'core/doctor_detail.html'
    context_object_name = 'doctor'

class NewsListView(ListView):
    model = News
    template_name = 'core/news_list.html'
    context_object_name = 'news_list'
    ordering = ['-publish_date']
    paginate_by = 6

class NewsDetailView(DetailView):
    model = News
    template_name = 'core/news_detail.html'
    context_object_name = 'news'

class GlossaryListView(ListView):
    model = GlossaryTerm
    template_name = 'core/glossary.html'

class ContactsView(ListView):
    model = Employee
    template_name = 'core/contacts.html'

class PrivacyPolicyView(TemplateView):
    template_name = 'core/privacy_policy.html'

class VacancyListView(ListView):
    model = Vacancy
    template_name = 'core/vacancies.html'

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'core/add_review.html'
    success_url = reverse_lazy('reviews')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PromoCodeListView(ListView):
    model = PromoCode
    template_name = 'core/promocodes.html'
    context_object_name = 'promocodes'

    def get_queryset(self):
        return PromoCode.objects.filter(valid_until__gte=timezone.now())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['archive'] = PromoCode.objects.filter(valid_until__lt=timezone.now())
        return context