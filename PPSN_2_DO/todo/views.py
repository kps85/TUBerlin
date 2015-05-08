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
    list_count = request.GET.get('list_count', '5').strip().split(" ")[0]
    search_query_raw = request.GET.get('search', '').strip().split(" ")
    search_query = []
    del_query = request.GET.get('delete', '')
    page_count, pages, page = 1, 1, 1
    offset, search_count = 0, 0
    limit, info_message, warn_message, search_message = None, None, None, None
    
    if len(del_query) > 0 and del_query[0]!= '':
        try:
            t = Task.objects.get(pk=del_query)
        except ObjectDoesNotExist:
            warn_message = 'Tried to delete task with id = ' + del_query + '. Task does not exist.'
        else:
            t.delete()
            info_message = 'Task (id = ' + del_query + ') successfully deleted.'
            
    if len(search_query_raw) > 0 and search_query_raw[0] != '':
        for s in search_query_raw:
            tasks = Task.objects.filter(task_desc__icontains=s).values('id')
            if tasks:
                for task in tasks:
                    search_query.append(task.get('id'))
        task_list = Task.objects.filter(id__in = search_query)
        search_count = task_list.count()
        search_message = str(search_count) + ' result(s) for "' + ' '.join(search_query_raw) + '"'
        
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
            page_count, pages, page = range(page_count), len(range(page_count)), int(page)-1
            
    return render(request, 'todo/index.html', {
        'task_list': task_list[offset:limit],
        'list_count': list_count,
        'page_count': page_count,
        'pages': pages,
        'page': page,
        'info_message': info_message,
        'warn_message': warn_message,
        'search_message': search_message,
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
                s = request.POST['status']
                p = int(request.POST.get('progress', 0))
                if ( s == 'cancelled' ) : s = 'C'
                elif ( s == 'done' ) : s = 'D'
                elif ( s == 'important' ) : s = 'I'
                else : s = 'R'            

                if ( str(p) == '' ) : p = 0
                elif ( p == 100 and s != 'D' ) :
                    s = 'D'
                elif ( p != 100 and s == 'D' ) :
                    p = 100
                
                t.task_deadline = datetime.datetime.strptime(request.POST['deadline'], "%Y-%m-%d")
            except (KeyError):
                return render(request, 'todo/editEntry.html', {
                    'task': t,
                    'info_message': "Doesn't work.",
                })
            except (ValueError):
                return render(request, 'todo/editEntry.html', {
                    'task': t,
                    'warn_message': "Sorry, missing or wrong value (date or progress). Try again!",
                })
            else:
                t.task_desc, t.task_progress, t.task_status = request.POST['description'], p, s
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
