from django.db import models

# Create your models here.
class CourseInquiry(models.Model):
    COURSE_CHOICES = [
        ('python_fs', 'Python Full Stack Development'),
        ('java_fs', 'Java Full Stack Development'),
        ('data_analytics', 'Data Analytics & Power BI'),
        ('ai_ml', 'AI & Machine Learning'),
        ('cloud_devops', 'Cloud & DevOps'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    selected_course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.selected_course}"