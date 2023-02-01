# importing all the required modules
from django.shortcuts import render, redirect
from pytube import *
from .forms import DirectoryForm
from django.contrib import messages
from django.http import JsonResponse
from asyncio import sleep
from django.http import HttpResponse
from django import forms
from .forms import userForm, DirectoryForm

responseText = {"Download":"Video is downloading!",
            "completed":"Download successfully!",
            "errorUrl":"Please check and insert url correctly!"}

def statusTexts(request, statusText):
    return HttpResponse(responseText[statusText])

# defining function
def index(request):
    # checking whether request.method is post or not
    if request.method == 'POST': 
         
        form = userForm(request.POST)

        if form.is_valid():
            url = form.cleaned_data['url']
            print("Here my url: "+url)

            try:
                selected_resolution = form.cleaned_data['resolution']
                video = YouTube(url)
                vid_id = video.video_id
                print(vid_id)
                
                check_availibilty = video.check_availability()
                print(check_availibilty)

                # setting video resolution
                if selected_resolution == "lowRes":
                    stream = video.streams.get_lowest_resolution()
                else:
                    stream = video.streams.get_highest_resolution()
                
                stream.download()
                response_message = 'Download successfully!'

            except Exception:
                url=""
                response_message = 'Please check and insert url correctly!'
                pass
    else:
        form = userForm()
        url =""
        response_message = 'Please insert url'

    return render(request, 'ytdownloadapp/index.html', {
            "userForm" : form,
            "response_message": response_message,
            "url" : url})
