from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from skills.models import SkillNode


def index(request):
	skills = SkillNode.objects.all()
	context = {
		'skills':skills[0]	
	}
	return render(request, 'skills/index.html', context)


def details(request, pk):
	pass

def add(request, pk):
	skills = get_object_or_404(SkillNode, pk=pk)
	skills.knowledge_count +=1
	skills.save()
	return HttpResponseRedirect(reverse('skills:index'))


def reduce(request, pk):
	negative_knowledge_count_message = ""
	skills = get_object_or_404(SkillNode, pk=pk)
	if skills.knowledge_count > 0:
		skills.knowledge_count -=1
		skills.save()
	return HttpResponseRedirect(reverse('skills:index'))