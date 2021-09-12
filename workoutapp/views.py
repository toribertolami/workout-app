from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from workoutapp.modles import Exercise

# Create your views here.
class HomeView(TemplateView):
    template_name = 'workoutapp/home.html'

class UserSignupView(FormView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('workoutapp:home')
    template_name='registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class ExerciseCreateView(CreateView):
    model = Exercise
    fields = ["name", "sets", "reps", "weight"]
    success_url = reverse_lazy("workoutapp:home")

    def form_valid(self,form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)