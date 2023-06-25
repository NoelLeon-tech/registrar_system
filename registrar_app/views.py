# Create your views here.
from django.shortcuts import render, redirect
from .models import Queue, Student
import random
from datetime import date, datetime
from django.db.models import Q
from django.http import Http404


def queue_list(request):
    queues = Queue.objects.filter(date_created=date.today()).filter(Q(status="Pending") | Q(status="Processing"))
    if queues:
        for i, queue in enumerate(queues):
            if i == 0:
                queue.status = "Processing"
                queue.save()
            elif queue.status == "Processed":
                queue.time_finished = datetime.now().time()
                queue.save()
        return render(request, 'registrar_app/queue_list.html', {'queues': queues})
                    
    else:
        queues = None
        return render(request, 'registrar_app/queue_list.html', {'queues': queues})
    
    
def new_queue(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        student_id = request.POST['student_id']
        student = None
        if not Student.objects.filter(student_id=student_id).exists():
            student = Student.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name, student_id=student_id)
        else:
            student = Student.objects.get(student_id=student_id)
        Queue.objects.create(
            student=student,
            time_created=datetime.now().time(),
            number=str(random.randint(1000, 9999))
        )
        return redirect('queue_list')
    else:
        return render(request, 'registrar_app/new_queue.html')
