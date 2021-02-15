from django.contrib import admin
from .models import Class, Subject, TypeOfSchool, LessonInterval, Lesson, Room, \
	SetLesson
# Register your models here.
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(TypeOfSchool)
admin.site.register(LessonInterval)
admin.site.register(Lesson)
admin.site.register(Room)
admin.site.register(SetLesson)