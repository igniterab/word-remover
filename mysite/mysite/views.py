#file being created by me
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    '''sending variable , info in templates by passing as a third arguments'''
    info = {"Name":"Ashish Bhardwaj","Designation":"student"}
    #hamesha templates aise hi bnayi jaati h
    return render(request,"index.html",info)


def data_submitted(request):
    #this function is used to get the data enterd by user
    text_entered = request.POST.get('text','default')
    word = request.POST.get('word','default')
    #yaha post liya h kyoki data bhout zyaada bada ho skta h
    #POST simple words mai clean URL deta h
    
    #to check the value of checkbox
    check_box = request.POST.get('check_box','off') #default value off li h
    word_list = text_entered.split()
    if check_box == 'on':
        abc = (' '.join([i for i in word_list if i not in word]))
        punct = {"purpose":"Remove punctuations","analyzed_text":abc,"data":text_entered,"word":word}
        return render(request,"data_submitted.html",punct)
    else:
        return HttpResponse("<h1>Please check that checkbox and try again :)</h1>")