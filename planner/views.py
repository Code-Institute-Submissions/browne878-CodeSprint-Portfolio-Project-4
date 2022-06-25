from django.shortcuts import render, redirect
from .models import Company, Project, Sprint, Case, User_Profile
from django.contrib.auth.models import User


# Pages
def projects(request):
    projects = Project.objects.filter(
        company=User_Profile.objects.get(user_id=request.user).company_id)
    context = {
        'projects': {}
    }
    for project in projects:
        try:
            context['projects'][project.name] = Sprint.objects.filter(
                project=project)
        except Sprint.DoesNotExist:
            context['projects'][project.name] = 'No Sprints Found'
    return render(request, 'planner/projects.html', context)


def new_project(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user = User.objects.get(username=request.user)
        company = Company.objects.get(owner=user)
        Project.objects.create(name=name, company=company)
        user_profile = User_Profile.objects.get(user_id=user)
        user_profile.role = User_Profile.Role.ADMIN
        user_profile.save()
    return redirect('projects')


def sprints(request, project):
    company = User_Profile.objects.get(user_id=request.user).company_id
    project = Project.objects.get(
        company=company)
    sprints = Sprint.objects.filter(project=project)
    context = {
        'sprints': {}
    }
    for sprint in sprints:
        try:
            context['sprints'][sprint.name] = Case.objects.filter(
                sprint=sprint
            )
        except Case.DoesNotExist:
            context['sprints'][sprint.name] = 'No Cases Found'
    return render(request, 'planner/sprints.html', context)


def new_sprint(request, project):
    if request.method == 'POST':
        Sprint.objects.create(
            name=request.POST.get('name'),
            starts_at=request.POST.get('date-starts'),
            ends_at=request.POST.get('date-ends'),
            project=Project.objects.get(
                company=User_Profile.objects.get(
                    user_id=request.user
                    ).company_id,
                name=project
            )
        )
    return redirect('sprints', project)


def cases(request, sprint):
    current_sprint = Sprint.objects.get(name=sprint)
    cases = Case.objects.filter(sprint=current_sprint)
    context = {
        'cases': cases
    }
    return render(request, 'planner/cases.html', context)


def new_case(request, sprint):
    if request.method == 'POST':
        Case.objects.create(
            category=request.POST.get('category'),
            title=request.POST.get('title'),
            status=request.POST.get('status'),
            due_date=request.POST.get('date-due'),
            task_size=request.POST.get('size'),
            sprint=Sprint.objects.get(name=sprint)
        )
    return redirect('cases', sprint)


def edit_case(request, sprint, case):
    print(request.method)
    if request.method == 'POST':
        found_case = Case.objects.get(case_id=case)
        found_case.title = request.POST.get('title')
        found_case.category = request.POST.get('category')
        found_case.status = request.POST.get('status')
        found_case.due_date = request.POST.get('date-due')
        found_case.task_size = request.POST.get('size')
        found_case.save()
    return redirect('cases', sprint)


def delete_case(request, sprint, case):
    print(request.method)
    if request.method == 'POST':
        Case.objects.filter(case_id=case).delete()
    return redirect('cases', sprint)


def create_profile(request):
    return render(request, 'planner/create_profile.html')


def new_profile(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('user')
        user = User.objects.get(username=username)
        try:
            User_Profile.objects.get(user_id=user)
        except User_Profile.DoesNotExist:
            User_Profile.objects.create(first_name=first_name,
                                        last_name=last_name,
                                        role=User_Profile.Role.CLIENT,
                                        user_id=user)
            return redirect('create-company')

    return render(request, 'planner/create_profile.html')


def create_company(request):
    return render(request, 'planner/create_company.html')


def new_company(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('user')
        user = User.objects.get(username=username)
        user_profile = User_Profile.objects.get(user_id=user)
        Company.objects.create(name=name, owner=user)
        user_profile.company_id = Company.objects.get(name=name)
        user_profile.save()
        return redirect('projects')
