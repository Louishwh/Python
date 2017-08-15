from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic,Entry
from .forms import TopicForm,EntryForm


def  index(request):
	return render(request,'learning_logs/index.html')

def topics(request):
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics':topics}
	return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
	topic = get_object_or_404(Topic,id=topic_id)
	if topic.owner != request.user:
		raise Http404

	entries = topic.entry_set.order_by('-date_added')
	topics = Topic.object.order_by('date_added')
	content = {'topic',topic,'entries',entries}
	return render(request,'learning_logs/topics.html',content)

@login_required
def new_topic(request):
	if request.method != 'POST':
		# 未提交数据，创建一个新表单
		form = TopicForm()
	else:
		# 处理POST的数据
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))

	content = {'form':form}
	return render(request,'learning_logs/new_topic.html',content)

@login_required
def new_entry(request,topic_id):
	if request.method != 'POST':
		form = EntryForm()
	else:
		form = EntryForm(request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))

	content = {'topic':topic,'form':form}
	return render(request,'learning_log/new_entry.html',content)

@login_required
def edit_entry(request,entry_id):
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if topic.owner != request.user:
		raise  Http404

	if request.method != 'POST':
		form = EntryForm(instance=entry)
	else:
		form = EntryForm(instance=entry,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))

	content = {'entry':entry,'topic':topic,'form':form}
	return render(request,'learning_logs/edit_entry.html',content)