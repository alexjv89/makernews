from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from models import Newsletter
# Create your views here.
def landing_page(request):
	# args.update(csrf(request))
	# return render_to_response('catalog/landing_page.html', args,context_instance=RequestContext(request))
	# return HttpResponse('Landing page for maker news india')
	print "\n\n\n on the landing page"
	return render(request, 'newsletter/landing_page2.html', {
		})

def calendar_page(request):
	print "\n\n\n came here"
	# return HttpResponse('Landing page for maker news india')
	return render(request, 'newsletter/calendar_page.html', {
		})

def test_page(request):
	print "\n\n\n came here"
	# return HttpResponse('Landing page for maker news india')
	return render(request, 'newsletter/test_page.html', {
		})

def embed_email_signup(request):
	# print "\n\n\n came here"
	# return HttpResponse('Landing page for maker news india')
	return render(request, 'newsletter/embed_email_signup.html', {
		})

def archive_page(request):
	print "\n\n\n came here"
	all_nl=Newsletter.objects.all().order_by('-number')
	# return HttpResponse('Landing page for maker news india')
	return render(request, 'newsletter/archive_page.html', {
		'all_nl':all_nl,
		})

def newsletter_page(request,newsletter_no):
	# print "\n\n\n came here"
	# return HttpResponse('Landing page for maker news india')
	nl=Newsletter.objects.get(number=newsletter_no)
	prev=int(newsletter_no)-1
	if prev>0:
		nl.previous='/newsletter/'+ str(prev)
	next=int(newsletter_no)+1
	# print "\n"*3
	# print next
	if Newsletter.objects.filter(number=str(next)):
		nl.next='/newsletter/'+str(next)
		# print "next set to " + str(next)
	# else:
		# print "no next newsletter"
	return render(request, 'newsletter/newsletter_page.html', {
		'newsletter_no':newsletter_no,
		'nl':nl,
		})

def team_page(request):
	print "\n\n\n came here"
	# return HttpResponse('Landing page for maker news india')
	return render(request, 'newsletter/team_page.html', {

		})
