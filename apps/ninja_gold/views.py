from django.shortcuts import render, redirect

# Create your views here.
import random

def index(request):
    if 'gold' not in request.session or not request.session['gold']:
        # session['gold'] = int((random.random() * (100 - 0 + 1)))
        request.session['gold'] = 0
        request.session['activity'] = ""

    context = {
        'gold': request.session['gold'],
        'activity': request.session['activity']
    }

    return render(request, "ninja_gold/index.html", context)
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route


def process_money(request):
    # get the source
    if request.method == 'POST':
        source = request.POST['location']

        if source == 'farm':
            foundGold = int((random.random() * 10) + 10)
            request.session['gold'] += foundGold
            request.session['activity'] += "Earned " + str(foundGold) + " golds from the farm!\n"
        elif source == 'cave':
            foundGold = int((random.random() * 5) + 5)
            request.session['gold'] += foundGold
            request.session['activity'] += "Earned " + str(foundGold) + " golds from the cave!\n"
        elif source == 'house':
            foundGold = int((random.random() * 2) + 2)
            request.session['gold'] += foundGold
            request.session['activity'] += "Earned " + str(foundGold) + " golds from the house!\n "
        elif source == 'casino':
            toss = random.random()
            if toss >= 0.5:
                winner = True
            else:
                winner = False

            amountWon = int((random.random() * 50))
            if winner:
                request.session['gold'] += amountWon
                request.session['activity'] += "Won " + str(amountWon) + " golds at the casino!\n"
            else:
                request.session['gold'] -= amountWon
                request.session['activity'] += "Lost " + str(amountWon) + " golds at the casino! Ouch!\n"

        return redirect("/ninja_gold")

