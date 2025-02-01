from django.shortcuts import render, redirect
import requests

def home(request):
    return render(request, 'home.html')

def insight(request):
    return render(request, 'insight.html')

def generate_ad(request):
    image_url = None
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '')
        api_url = f"https://image.pollinations.ai/prompt/{prompt}"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            image_url = api_url 
        else:
            image_url = None
    
    return render(request, 'generate_ad.html', {'image_url': image_url})