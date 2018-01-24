from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse

from .models import Rental
from .forms import RentalCreateForm


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'rentals/index.html'
    context_object_name = 'new_rentals_list'

    def get_queryset(self):

        return Rental.objects.order_by('-created_date')[:10]


class DetailView(generic.DetailView):
    model = Rental
    template_name = 'rentals/detail.html'


class RentalCreateView(generic.CreateView):
    form_class = RentalCreateForm
    template_name = 'rentals/rental_form.html'
    success_url = '/rentals/'

class RentalUpdateView(generic.UpdateView):
    form_class = RentalCreateForm
    template_name = 'rentals/rental_form.html'
    success_url = '/rentals/'


    def get_queryset(self):
        return Rental.objects.filter(pk = self.kwargs.get('pk', None))
