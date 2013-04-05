from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User

def mainpage(request):
  return render_to_response('mainpage.html',
    {
      'titlehead': 'Receptes de laguela',
      'pagetitle': 'Welcome to the Receptes  app',
      'contentbody': 'Managing non legal funding since 2013'
      #'user': request.user
    })
  #output = template.render(variables)
  #return HttpResponse(output)

def userpage(request, username):
  try:
    user = User.objects.get(username=username)
  except:
    raise Http404('User not found.')

  ingredients = user.recepta_set.all()
  template = get_template('userpage.html')
  variables = Context({
    'username': username,
    'ingredients': ingredients
    })
  output = template.render(variables)
  return HttpResponse(output)
