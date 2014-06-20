from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def landing_page(request):
    # args.update(csrf(request))
    # return render_to_response('catalog/landing_page.html', args,context_instance=RequestContext(request))
    # return HttpResponse('Landing page for maker news india')
    return render(request, 'newsletter/landing_page.html', {
        })