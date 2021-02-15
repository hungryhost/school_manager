from django.db import models
from django.conf import settings

# Create your models here.


class Class(models.Model):
	name = models.CharField(max_length=20, primary_key=True)
	created_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)

	def __str__(self):
		return str(self.name)


class Subject(models.Model):
	name = models.CharField(max_length=500, null=False, blank=False)
	description = models.TextField(max_length=500, null=False, blank=True)
	target_class = models.IntegerField(null=False, blank=False)
	created_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)

	def __str__(self):
		return str(self.name) + " " + str(self.target_class) + " класс"


class TypeOfSchool(models.Model):
	type = models.CharField(max_length=100, primary_key=True)
	created_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)

	def __str__(self):
		return str(self.type)


class Room(models.Model):
	room = models.CharField(max_length=100, primary_key=True)
	created_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)

	def __str__(self):
		return str(self.room)


class LessonInterval(models.Model):
	school_type = models.ForeignKey(TypeOfSchool, related_name='intervals',
		on_delete=models.CASCADE, null=False, blank=False)
	start = models.TimeField()
	end = models.TimeField()
	created_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)

	def __str__(self):
		return str(self.start) + " - " + str(self.end)


class Lesson(models.Model):
	subject = models.ForeignKey(Subject, related_name='lessons',
		on_delete=models.CASCADE, null=False, blank=False)
	teacher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='teaching',
		on_delete=models.CASCADE, null=False, blank=False)
	lesson_interval = models.ForeignKey(LessonInterval, related_name='listed_lessons',
		on_delete=models.CASCADE, null=True, blank=True)
	room = models.ForeignKey(Room, related_name='held_lessons',
		on_delete=models.CASCADE, null=True, blank=True)
	description = models.TextField(max_length=500, null=False, blank=True)
	note = models.TextField(max_length=500, null=False, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)

	def __str__(self):
		return str(self.subject) + " " + str(self.teacher)


class SetLesson(models.Model):
	WEEKDAYS = [
		(1, 'Понедельник'),
		(2, 'Вторник'),
		(3, 'Среда'),
		(4, 'Четверг'),
		(5, 'Пятница'),
		(6, 'Суббота'),
	]
	lesson = models.ForeignKey(Lesson, related_name='set_lessons',
		on_delete=models.CASCADE, null=False, blank=False)
	day = models.IntegerField(
		choices=WEEKDAYS,
		null=False,
		blank=False
	)
