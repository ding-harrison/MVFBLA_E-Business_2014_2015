from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from accountstuff.models import UserInfo
from django.contrib.auth.models import User

def home(request):
	posInfos = UserInfo.objects.filter(user=request.user.username)
	context = {
		"user": request.user,
		"userinfo": posInfos[0] if posInfos else None
	}
	template = loader.get_template('homepage.html')
	return HttpResponse(template.render(RequestContext(request, context)))
def browseCategory(request):	 
	return render_to_response('browseCategory.html', context_instance=RequestContext(request))
def browseTag(request):	 
	return render_to_response('browseTag.html', context_instance=RequestContext(request))
def itemListing(request):	 
	return render_to_response('itemListing.html', context_instance=RequestContext(request))
def search(request):	 
	return render_to_response('search.html', context_instance=RequestContext(request))
def shoppingCart(request):	 
	return render_to_response('shoppingcart.html', context_instance=RequestContext(request))