from django.urls import path 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

import workoutapp.views as workout_views

app_name = "workoutapp"
urlpatterns = [
        path('', workout_views.HomeView.as_view(), name="home"),
        path('login', LoginView.as_view(), name="login"),
        path('logout', LogoutView.as_view(), name="logout"),
        path('signup', UserSignupView.as_view(), name="signup"),
        path(
          'create',
          login_required(workout_views.ExerciseCreateView.as_view()),
          name="exercise_create"),
        )
]