from django.shortcuts import render

work_list = []

def index(request):
    work = request.GET.get('work')
    if work:
        work_list.append(work)
    context = {
        'work': work_list
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def detail(request, work):
    return render(request, 'todos/detail.html', {'work': work})