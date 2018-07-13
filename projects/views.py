from django.shortcuts import render, get_object_or_404
from urllib.parse import quote_plus
from .models import Project, ProjectCategory, PageProjectsDescription

def projects(request):
	categories = ProjectCategory.objects.filter(is_active=True)

	title_description_model = PageProjectsDescription.objects.filter(is_active=True)[0]
	print(title_description_model)
	title = title_description_model.title
	short_description = title_description_model.short_description
	description = title_description_model.description
	
	projects = Project.objects.filter(is_active=True)
	# category_title = ProjectCategory.
	# category_description
	# print(projects)
	# if project.category.name == 'Проекти':
	# 	category_title = 
	# 	category_description
	context = {
			'categories': categories,
			'title': title,
			'short_description':short_description,
			'description': description,
			'projects': projects,
		}

	return render(request, 'projects/projects.html', context)

def project_detail(request, id=None):
	categories = ProjectCategory.objects.filter(is_active=True)
	project = get_object_or_404(Project, id=id)
	share_string = quote_plus("Проект ") + quote_plus(project.name)
	if project.short_description:
		share_string = quote_plus("Проект ") + quote_plus(project.name) + quote_plus(" ") + quote_plus(project.short_description)
	context = {
			'categories': categories,
			'project': project,
			'share_string': share_string,
		}

	return render(request, 'projects/project_detail.html', context)


def projects_in_category(request, id=None):
	categories = ProjectCategory.objects.filter(is_active=True)
	category = get_object_or_404(ProjectCategory, id=id)
	projects_in_category = Project.objects.filter(is_active=True, category_id = id)
	context = {
			'categories': categories,
			'category':category,
			'projects_in_category': projects_in_category,
		}

	return render(request, 'projects/projects_in_category.html', context)