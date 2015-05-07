import datetime

from django.core.urlresolvers import reverse
from django.db.models.base import ObjectDoesNotExist 
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic

from .models import Task

# Create your views here.

def index(request):
    task_count = Task.objects.count()
    task_list = Task.objects.order_by('-task_deadline')
    list_count = request.GET.get('list_count', '5').split(" ")[0]
    search_query = request.GET.get('search', '')
    del_query = request.GET.get('delete', '')
    offset = 0
    limit = None
    page_count = 1
    pages = 1
    page = 1
    info_message = None
    warn_message = None
    
    if len(del_query) > 0 and del_query[0]!= '':
        try:
            t = Task.objects.get(pk=del_query)
        except ObjectDoesNotExist:
            warn_message = 'Tried to delete task with id = ' + del_query + '. Task does not exist.'
        else:
            t.delete()
            info_message = 'Task (id = ' + del_query + ') successfully deleted.'
            
    if len(search_query) > 0 and search_query[0] != '':
        task_list = Task.objects.filter(task_desc__contains = search_query)
        
    else :
        if list_count == 'All':
            list_count = 0
        else:
            list_count = int(list_count)
            mod = task_count%list_count
            page_count = int(task_count/list_count)
            if mod > 0: page_count += 1
            page = request.GET.get('page', 1)
            offset = (int(page) - 1 ) * list_count
            if int(page) > 0:
                offset = (int(page) - 1 ) * list_count
                limit = int(page) * list_count
            else :
                limit = list_count

            page_count = range(page_count)
            pages = len(page_count)
            page = int(page)-1
            
    return render(request, 'todo/index.html', {
        'task_list': task_list[offset:limit],
        'list_count': list_count,
        'page_count': page_count,
        'pages': pages,
        'page': page,
        'info_message': info_message,
        'warn_message': warn_message,
    })

def edit(request, task_id):
    t = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        if ( request.POST['description'] == '' ) :
            return render(request, 'todo/editEntry.html', {
                'task': t,
                'warn_message': 'Sorry, missing description. Try again!',
            })
        else :
            try:    
                if ( request.POST['status'] == 'cancelled' ) : s = 'C'
                elif ( request.POST['status'] == 'done' ) : s = 'D'
                elif ( request.POST['status'] == 'important' ) : s = 'I'
                else : s = 'R'            

                if ( request.POST['progress'] == '' ) : p = 0
                elif ( request.POST['progress'] == 100 and s != 'D' ) :
                    s = 'D'
                    p = request.POST['progress']
                elif ( request.POST['progress'] != 100 and s == 'D' ) :
                    s = 'R'
                    p = 100
                else : p = request.POST['progress']
                
                t.task_deadline = datetime.datetime.strptime(request.POST['deadline'], "%Y-%m-%d")
            except (KeyError):
                return render(request, 'todo/editEntry.html', {
                    'task': t,
                    'info_message': "Doesn't work.",
                })
            except (ValueError):
                return render(request, 'todo/editEntry.html', {
                    'task': t,
                    'warn_message': "Sorry, missing or wrong date. Try again!",
                })
            else:
                t.task_desc = request.POST['description']
                t.task_progress = p
                t.task_status = s
                t.save()
                return render(request, 'todo/editEntry.html', {
                    'task': t,
                    'info_message': "Task updated successfully.",
                })
    else:
        return render(request, 'todo/editEntry.html', { 'task': t, })

def create(request):
    if request.method == 'POST':
        if ( request.POST['description'] == '' ) :
            return render(request, 'todo/createEntry.html', {
                'task_deadline': request.POST['deadline'],
                'task_desc': request.POST['description'],
                'task_progress': request.POST['progress'],
                'task_status': request.POST['status'],
                'warn_message': "Sorry, missing description. Try again.",
            })
        else :
            try:
                if ( request.POST['status'] == 'cancelled' ) : s = 'C'
                elif ( request.POST['status'] == 'done' ) : s = 'D'
                elif ( request.POST['status'] == 'important' ) : s = 'I'
                else : s = 'R'

                if ( request.POST['progress'] == '' ) : p = 0
                elif ( request.POST['progress'] == '100' and s != 'D' ) :
                    s = 'D'
                    p = request.POST['progress']
                elif ( request.POST['progress'] != '100' and s == 'D' ) : p = 100
                else : p = request.POST['progress']
                
                t = Task(
                    task_deadline = datetime.datetime.strptime(request.POST['deadline'], "%Y-%m-%d"),
                    task_desc = request.POST['description'],
                    task_progress = p,
                    task_status = s,
                )
            except (KeyError):
                return render(request, 'todo/createEntry.html', {
                    'warn_message': "Doesn't work.",
                })
            except (ValueError):
                return render(request, 'todo/createEntry.html', {
                    'task_deadline': request.POST['deadline'],
                    'task_desc': request.POST['description'],
                    'task_progress': request.POST['progress'],
                    'task_status': request.POST['status'],
                    'warn_message': "Sorry, missing date. Try again.",
                })
            else:
                t.save()
                return render(request, 'todo/createEntry.html', {
                    'info_message': "Task created successfully.",
                })
    else:
        return render(request, 'todo/createEntry.html',)

def imprint(request):
    return render(request, 'todo/imprint.html',)
