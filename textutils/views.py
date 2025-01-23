# i have created this file - Nikhil
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # return HttpResponse('Home Page')
    info = {'name':'Nikhil','place':'India'}
    return render(request,'index.html',info)

def analyze(request):
    #this line help me to get the data what i have written in the text area
    #getting the text
    textareaInput=request.POST.get('text','default')
    #checking checkbox
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')

    analyzed = textareaInput

    if removepunc == 'on':
        punctuation = '''.,;:!?'"-–—()[]{}\/|~`@#$%^&*_+=<>…'''
        analyzed = ''.join(char for char in analyzed if char not in punctuation)

    if uppercase == 'on':
        analyzed = analyzed.upper()

    if charactercounter == 'on':
        analyzed = str(len(analyzed))
#This condition invoke for more than one analysis prompt call
    if (removepunc == 'on' and charactercounter == 'on'):
        punctuation = '''.,;:!?'"-–—()[]{}\/|~`@#$%^&*_+=<>…'''
        analyzed = ''.join(char for char in analyzed if char not in punctuation)
        analyzedcout = str(len(analyzed))

    if (uppercase != 'on' and charactercounter != 'on'):
        analyzed = analyzed.upper()
        analyzedcout = str(len(analyzed))
     
    if (removepunc != 'on' and uppercase != 'on'):
         punctuation = '''.,;:!?'"-–—()[]{}\/|~`@#$%^&*_+=<>…'''
         analyzed = ''.join(char for char in analyzed if char not in punctuation)
         analyzed = analyzed.upper()
        #By-Swarnav Das

    if (removepunc != 'on' and uppercase != 'on' and charactercounter != 'on'):
        back = '''<a href="/"><button style="width: 100px; height: 50px; background-color:#ff0000; color: white; border: none; border-radius: 4px; cursor: pointer;">Back</button></a>'''
        return HttpResponse('Please select any operation and try again \n' + back)
    
    params = {'purpose': 'Analyzed Text', 'analyzed_text': analyzed , 'analyzed_count': analyzedcout}

    return render(request, 'analyze.html', params)  
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
