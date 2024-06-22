from django.db import models
from django.conf import settings  # Import settings to get the custom user model
# import uuid
from django.utils import timezone
import os
from django.conf import settings


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


def problem_markdown_upload_to(instance, filename):
    extension = filename.split(".")[-1]
    k = str(instance.id).split("_")[-1]
    new_filename = f"{k}.{extension}"
    return os.path.join(
        settings.BASE_DIR, "problems", str(instance.contest.id), new_filename
    )


class Contest(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    registrations = models.IntegerField(default=0)
    start_time = models.DateTimeField()
    length = models.DurationField()

    def int(self):
        return self.id

    @property
    def is_past_contest(self):
        return self.start_time + self.length < timezone.now()


class Problem(models.Model):
    id = models.CharField(max_length=50, unique=True, primary_key=True)
    contest = models.ForeignKey(
        Contest, related_name="problems", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    markdown_file = models.FileField(upload_to=problem_markdown_upload_to)
    difficulty = models.IntegerField()  # Define difficulty levels
    tags = models.ManyToManyField("Tag", blank=True)
    solved_by = models.IntegerField(default=0)

    def __str__(self):
        return self.id

    def get_markdown_content(self):
        with open(self.markdown_file.path, "r") as file:
            return file.read()


class Submission(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    submission_time = models.DateTimeField(auto_now_add=True)
    submitted_value = models.FloatField()
    is_correct = models.BooleanField(default=False)

    def int(self):
        return self.id
