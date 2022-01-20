from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html' )
    # return HttpResponse ("<h1><center>Hello Guys<center><h1>")
    
def homenew(request):
    return render(request,'index1.html')

def analyz(request):
    gttext = request.POST.get('text','default')
    # print(gttext)
    removepun = request.POST.get('remove_punctuation','off')
    upper = request.POST.get('uppercase','off')
    # print(gttext)
    punctuation = '''!~`@#$%^&*()_{}[]'":;<>.,?/\|'''
    if removepun == 'on' and upper == 'on':
        analyzed = ""
        for i in gttext:
            if i not in punctuation:
                analyzed = analyzed + i.upper()
        dic = {'purpose':'Remove punctuation and Upper case', 'analyzed_text':analyzed}
        return render(request, 'analyz.html',dic)
    elif removepun == 'on':
        analyzed = ""
        for i in gttext:
            if i not in punctuation:
                analyzed = analyzed + i
        dic = {'purpose':'remove punctuations', 'analyzed_text':analyzed}
        return render(request, 'analyz.html',dic)
    elif upper == 'on':
        analyzed = ""
        for i in gttext:
                analyzed = analyzed + i.upper()
        dic = {'purpose':'Upper Case', 'analyzed_text':analyzed}
        return render(request, 'analyz.html',dic)

    else:
        analyzed = ''
        for i in gttext:
            analyzed = analyzed + i
        dic = {'purpose':'Remove punctuation and Upper case', 'analyzed_text':analyzed}
        return render(request, 'analyz.html',dic)
        
# def video(request):
#     v = "<video controls><source src = 'F:\Mobio\Python\Django\textutils\movie.mp4 type = 'video/mp4'><video>"
#     # b = "<a href = '/'>back</a>"
#     return HttpResponse(v)

# def image(request):
#     x = "<img src = 'wp2670838-full-hd-wallpaper-downlord.jpg' alt = 'snake'><br><a href = '/'>back</a>"
#     return HttpResponse(x)

# def essay(request):
#     with open("F:\Mobio\Python\File IO\Fruits.txt") as f:
#         return HttpResponse(f.read())
    
# def rmvslash(request):
#     slash = request.GET.get('address')
#     p = ","
#     add = ''
#     for i in slash:
#         if i not in p:
#             add = add + i
            
#     properadd = {'properadd':add}
    
#     return render(request, 'result.html',properadd)

# def navigator(request):
#     s = '''<div>Your best site for streaming songs: <b>Gaana</b></div><a href='https://gaana.com/'>Ganna</a><br>
#         <div>Best site for downloading movies: <b>Mkvcinemas</b></div>
#         <a href = 'https://www.mkvcinemas.si/'>mkvcinemas</a><br>
#         <div>Best site to read newspaper: <b>Times of india</b></div>
#         <a href = 'https://timesofindia.indiatimes.com/'>Time Of India</a> 
#         <div>Shop Online the Latest Fashion in apparels brands in India: <b>Ajio</b></div>
#         <a href = 'https://www.ajio.com/'>Ajio</a>'''
    
#     return HttpResponse(s)
