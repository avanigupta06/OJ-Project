from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Problem(models.Model):
    DIFFICULTY_LEVELS = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_LEVELS)
    input_testcase = models.TextField()
    output_testcase = models.TextField()

    def __str__(self):
        return f"{self.title}"

class HiddenTestCase(models.Model):
    problem = models.ForeignKey("home.Problem", on_delete=models.CASCADE, related_name="hidden_testcases")
    input_data = models.TextField()
    expected_output = models.TextField()

    def __str__(self):
        return f"Hidden TestCase for Problem {self.problem.title}"