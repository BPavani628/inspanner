from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InquiryForm

def home(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! Our career counselor will contact you shortly.")
            return redirect('home')
        else:
            messages.error(request, "Please check the form for errors and submit again.")
    else:
        form = InquiryForm()

    courses = [
        {
            'title': 'Python Full Stack Development',
            'tag': 'Trending',
            'desc': 'Master Python, Django, REST APIs, HTML/CSS/JS, React, and database design with real-world deployments.',
            'duration': '4 Months',
            'mode': 'Classroom & Online',
            'icon': 'bi-code-slash'
        },
        {
            'title': 'Data Analytics & Power BI',
            'tag': 'High Demand',
            'desc': 'Advanced Excel, SQL, Python for Data Science, Power BI, and Tableau dashboard storytelling.',
            'duration': '3 Months',
            'mode': 'Classroom & Online',
            'icon': 'bi-graph-up-arrow'
        },
        {
            'title': 'AI & Machine Learning Bootcamp',
            'tag': 'Advanced',
            'desc': 'Deep Learning, NLP, Prompt Engineering, Computer Vision, and Generative AI framework implementations.',
            'duration': '4 Months',
            'mode': 'Classroom & Online',
            'icon': 'bi-cpu'
        },
        {
            'title': 'Java Full Stack Development',
            'tag': 'Enterprise',
            'desc': 'Core & Advanced Java, Spring Boot, Microservices, Hibernate, and Angular/React frontends.',
            'duration': '4 Months',
            'mode': 'Classroom & Online',
            'icon': 'bi-laptop'
        }
    ]

    return render(request, 'inspannerlanding.html', {'form': form, 'courses': courses}) 
