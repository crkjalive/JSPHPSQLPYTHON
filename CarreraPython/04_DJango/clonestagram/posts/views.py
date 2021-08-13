"""Posts Views"""

"""Django"""
from django.http import HttpResponse

"""Utilities"""
from datetime import datetime


"""json global de posts"""
posts = [
	{
		'name':'Django Development',
		'user': 'Wizard DJ',
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M:%S hrs'),
		'picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8zxI-vXc42JHCBi9Ny4XK0mDxAp8bNGG2aLdrZqK-fxqaH-UkxRaxpamKFwEbSqIxnko&usqp=CAU'

	},
	{
		'name':'Python Development',
		'user': 'Jared',
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M:%S hrs'),
		'picture': 'https://pm1.narvii.com/6040/e77a03c4629a9b4ae5daf07c76b2529906db5814_hq.jpg'

	},
	{
		'name':'Mario Bross',
		'user': 'Linda',
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M:%S hrs'),
		'picture': 'https://pm1.narvii.com/6040/2144164f518c6dda99b856fc8b65acc6ba4161f0_hq.jpg'

	},
]

# Create your views HTML here.
def list_posts(request):

	""" List existings posts """
	
	content = []
	
	for post in posts:
		content.append("""
			<h1>Hola care monda</h1>
			<h3><strong>{name}</strong></h3>
			<p><small>{user} - <i>{timestamp}</i></small></p>
			<figure><img src="{picture}"/></figure>
			""".format(**post))

	return HttpResponse("<br>".join(content))