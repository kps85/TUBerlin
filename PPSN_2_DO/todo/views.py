import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic

from .models import Task

# Create your views here.

def index(request):
    task_count = Task.objects.count()
    list_count = request.GET.get('list_count', '5').split(" ")[0]
    search_query = request.GET.get('search', '').split(" ")
    
    if len(search_query) > 0 and search_query[0] != '':
        list_count = 0
        page_count = 1
        page = 1
        search_list_raw = []
        search_list = []
        for sq in search_query:
            search_list_raw.append(Task.objects.filter(task_desc__contains = sq).values('id').values())
        for slr in search_list_raw:
            search_list.append(slr.values('id'))
        return render(request, 'todo/index.html', {
            'task_list': Task.objects.filter(task_desc__in = ['10', '14']),
            'search_list': search_list,
            'list_count': 0, 'page_count': 1, 'pages': 1, 'page': 1,
        })
    else :
        if list_count == 'All':
            task_list = Task.objects.all().order_by('-task_deadline')
            return render(request, 'todo/index.html', {
                'task_list': task_list,
                'list_count': 0, 'page_count': 1, 'pages': 1, 'page': 1,
            })
        else:
            list_count = int(list_count)
            mod = task_count%list_count
            page_count = int(task_count/list_count)
            if mod > 0: page_count += 1
            page = request.GET.get('page', 0)
            offset = (int(page) - 1 ) * list_count
            if int(page) > 0:
                offset = (int(page) - 1 ) * list_count
                limit = int(page) * list_count
            else :
                offset = 0
                limit = list_count
            
            task_list = Task.objects.order_by('-task_deadline')[offset:limit]
            return render(request, 'todo/index.html', {
                'task_list': task_list,
                'list_count': list_count,
                'page_count': range(page_count),
                'pages': len(range(page_count)),
                'page': int(page)-1,
            })

def edit(request, task_id):
    t = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':        
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

def delete(request, task_id):
    t = Task.objects.get(pk=task_id)
    t.delete()
    return render(request, 'todo/index.html',{
        'info_message': 'Task deleted successfully.',
    })

def imprint(request):
    return render(request, 'todo/imprint.html',)
    
