from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import random
# home -----------------------------------------------------------------------------------------------------
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    if  request.session['gold'] < 0:
        request.session['gold'] = 0
    return render(request,'index.html')

# selection -------------------------------------------------------------------------------------------------
def farm(request):
    coins = random.randint(10,20)
    request.session['gold'] += coins
    request.session['activity'].append(f'Congrats here is {coins}Gs!')
    return redirect('/')

# selection -------------------------------------------------------------------------------------------------
def cave(request):
    coins = random.randint(5,15)
    request.session['gold'] += coins
    request.session['activity'].append(f'Congrats here is {coins}Gs!')
    return redirect('/')

# selection -------------------------------------------------------------------------------------------------
def home(request):
    coins = random.randint(1,5)
    request.session['gold'] += coins
    request.session['activity'].append(f'Congrats here is {coins}Gs!')
    return redirect('/')

# selection -------------------------------------------------------------------------------------------------
def casino(request):
    coins = random.randint(-100,100)
    request.session['gold'] += coins
    if  request.session['gold'] < 0:
        request.session['activity'].append('You Lose. Gold Reset to zero!')
    elif coins > 0 :
         request.session['activity'].append(f'Congrats You win {coins}Gs!')
    else:
        coins = abs(coins)
        request.session['activity'].append(f'Sorry you lose {coins}Gs...FOCUS!')
    return redirect('/')

# reset -----------------------------------------------------------------------------------------------------
def reset(request):
    del request.session['gold']
    del request.session['activity']
    return redirect('/')