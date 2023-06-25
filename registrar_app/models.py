from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=10, null=True, blank=True)


    def __str__(self):
        return f"Student ID: {self.student_id} {self.first_name} {self.middle_name} {self.last_name}"

class Queue(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    time_created = models.TimeField()
    time_finished = models.TimeField(null=True, blank=True)
    number = models.CharField(max_length=4)
    STATUS_CHOICES = [
        ("Processing", "Processing"),
        ("Processed", "Processed"),
        ("Canceled", "Canceled"),
        ("Skipped", "Skipped"),
        ("Pending", "Pending")
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Pending")

    def __str__(self):
        return f"Queue - Student: {self.student.first_name, self.student.middle_name, self.student.last_name} (ID: {self.student.student_id}), Status: {self.status}, Number: {self.number}"
