import os
import openai

from django.shortcuts import render
from openai_chatter.settings import API_KEY

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
  else: 
    prompt = ""
    response = ""
    display = "display: hidden;"
  return render(request, 'chatapp/index.html', {"prompt": prompt, "response": response['choices'][0]['message']['content'], "display": display})