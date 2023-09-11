import os
import openai

from copy import deepcopy

from django.shortcuts import render
from openai_chatter.settings import API_KEY

TEXT_PURP = 'text-purple-600'

nav_dicts = [
  {'name': 'Home', 'color': TEXT_PURP, 'path': '/'},
  {'name': 'Documentation', 'color': TEXT_PURP, 'path': 'docs'},
  {'name': 'Links', 'color': TEXT_PURP, 'path': 'links'}
]

# Create your views here.
def index(request):
  if request.method == "POST":
    form = request.POST
    prompt = form['prompt']
    openai.api_key = API_KEY
    response = openai.ChatCompletion.create(
      model='gpt-3.5-turbo',
      messages=[
        {"role": "system", "content": "You are an expert on colors and color theory. You love art and nature. Send all responses with html markup so that the responses can be displayed as html elements. For all responses, use css stylings in your html tags to apply colors to accentuate your responses."},
        {"role": "user", "content": prompt}
      ],
      max_tokens=1024,
    )
    display=""
    response = response['choices'][0]['message']['content']
  else: 
    prompt = "Prompt will appear here . . . "
    response = "Your answer will appear here!"
    display = "display: hidden;"
  links = deepcopy(nav_dicts)
  links[0]['color'] = 'text-blue-600'
  return render(request, 'chatapp/index.html', {"prompt": prompt, "response": response, "display": display, "nav_links": links})

def docs(request):
  links = deepcopy(nav_dicts)
  links[1]['color'] = 'text-blue-600'
  return render(request, 'chatapp/docs.html', {"nav_links": links})

def linksview(request):
  links = deepcopy(nav_dicts)
  links[2]['color'] = 'text-blue-600'
  return render(request, 'chatapp/links.html', {"nav_links": links})