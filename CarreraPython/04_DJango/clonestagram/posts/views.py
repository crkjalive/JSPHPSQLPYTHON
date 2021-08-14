"""Posts Views"""

"""Django"""
# ya no vamos a usar HttpResponse
# from django.http import HttpResponse

# ahora vamos a usar shortcuts render
from django.shortcuts import render 


"""Utilities"""
from datetime import datetime


"""json global de posts"""
posts = [
	{
		'title': 'Django Development',
		'user': {
			'name':'Wizard DJ',
			'picture': 'https://picsum.photos/50/50',
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M:%S hrs'),
		'photo':'https://picsum.photos/200/200',
	},
	{
		'title': 'Python Development',
		'user': {
			'name':'Jared',
			'picture': 'https://picsum.photos/50/50',
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M:%S hrs'),
		'photo':'https://picsum.photos/200/200',
	},
	{
		'title': 'Javascript Development',
		'user': {
			'name':'Mario Bross',
			'picture': 'https://picsum.photos/50/50',
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M:%S hrs'),
		'photo':'https://picsum.photos/200/200',
	}
]

# Create your views HTML here.
def list_posts(request):

	""" List existings posts """
	return render(request, 'feed.html', {'posts':posts})
