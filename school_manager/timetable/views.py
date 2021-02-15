from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from school.models import SetLesson


def home(request):
    context = {
        'lessons':
            SetLesson.objects.all()

    }
    return render(request, 'timetable/timetable.html', context)


class LessonListView(LoginRequiredMixin, ListView):
    model = SetLesson
    template_name = 'timetable/timetable.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'lessons'
    ordering = ['day']

