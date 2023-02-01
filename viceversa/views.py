from django.shortcuts import render
import re


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET["usertext"]
    reversed_text = user_text[::-1]
    len_text = len(re.findall(r"[а-яА-Яa-zA-Z]{2,}",user_text))
    return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text, 'lentext':len_text})
