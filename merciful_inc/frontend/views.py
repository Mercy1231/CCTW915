from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'frontend/index.html', {})

def about(request):
	return render(request, 'frontend/about.html', {})

def services(request):
	return render(request, 'frontend/services.html', {})

def staff(request):
	return render(request, 'frontend/staff.html', {})

def testimonials(request):
	return render(request, 'frontend/about.html', {})