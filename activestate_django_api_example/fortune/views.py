from django.shortcuts import render
from django.http import JsonResponse
import random


def fortune(request):
    fortunes = [
        'A feather in the hand is better than a bird in the air. ',
        'A golden egg of opportunity falls into your lap this month.',
        'Bide your time, for success is near.',
        'Curiosity kills boredom. Nothing can kill curiosity.',
        'Disbelief destroys the magic.',
        'Dont just spend time. Invest it.',
        'Every wise man started out by asking many questions.',
        'Fortune Not Found: Abort, Retry, Ignore?',
        'Good to begin well, better to end well.',
        'How many of you believe in psycho-kinesis? Raise my hand.',
        'Imagination rules the world.',
        'Keep your face to the sunshine and you will never see shadows.',
        'Listen to everyone. Ideas come from everywhere.',
        'Man is born to live and not prepared to live.',
        'No one can walk backwards into the future.',
        'One of the first things you should look for in a problem is its positive side.',
        'Pick battles big enough to matter, small enough to win.',
        'Remember the birthday but never the age.',
        'Success is failure turned inside out.',
        'The harder you work, the luckier you get.',
        'Use your eloquence where it will do the most good.',
        'Whats hidden in an empty box?',
        'Your reputation is your wealth.',
    ]

    return JsonResponse({
        'data': random.choice(fortunes),
        'status': 'awesome'
    })
