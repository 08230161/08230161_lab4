from django.db import models


class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    college = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

# 🌱 Your learning journey table
class LearningJourney(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title