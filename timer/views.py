from django.shortcuts import render
from .models import PomodoroSession 
def index(request):
    if request.method == "POST":
        task_name = request.POST.get('task_name')
        duration = request.POST.get('duration')
        PomodoroSession.objects.create(
            task_name = task_name,
            duration = duration
        )
    return render(request, 'timer/index.html')

def history(request):
    sessions = PomodoroSession.objects.all().order_by('completed_at')
    return render(request, 'timer/history.html', {'sessions': sessions})