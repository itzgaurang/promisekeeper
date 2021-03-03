from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator
from .models import Contact, Promise, Party, Politician
from django.contrib import messages


# Create your views here.

#Homepage
def home(request):
    allPromise = Promise.objects.all()
    paginator = Paginator(allPromise, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    cpromise = allPromise.filter(status='C')
    ncpromise = allPromise.filter(status='NC')
    ppromise = allPromise.filter(status='P')
    apromise = allPromise.filter(status='A')

    promise_count = allPromise.count()
    cpromise_count = cpromise.count()
    ncpromise_count = ncpromise.count()
    ppromise_count = ppromise.count()
    apromise_count = apromise.count()

    context = {'page_obj':page_obj, 'promise_count':promise_count, 'cpromise_count':cpromise_count, 'ncpromise_count':ncpromise_count, 'ppromise_count':ppromise_count, 'apromise_count':apromise_count}
    return render(request, 'promise_keeper/home.html', context)

#Contact Page
def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']

        if len(name)<2 or len(email)<3 or len(desc)<5:
            messages.error(request, "Please Fill Form Correctly")
        else:
            messages.success(request, "Message Sent")
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()
    return render(request, 'promise_keeper/contact.html')

#About Page
def about(request):
    # return HttpResponse('This is about')
    return render(request, 'promise_keeper/about.html')

#Promise Template
def promises(request, slug):
    promise = Promise.objects.filter(slug=slug).first()
    context = {'promise':promise}
    return render(request, 'promise_keeper/promises.html', context)

#Party Template
def party(request, slug):
    search = Party.objects.filter(slug=slug).first()
    promises = Promise.objects.filter(party=search)
    party = Party.objects.filter(slug=slug).first()
    promise_count = promises.count()

    cpromise = promises.filter(status='C')
    ncpromise = promises.filter(status='NC')
    ppromise = promises.filter(status='P')
    apromise = promises.filter(status='A')
    
    cpromise_count = cpromise.count()
    ncpromise_count = ncpromise.count()
    ppromise_count = ppromise.count()
    apromise_count = apromise.count()

    paginator = Paginator(promises, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if promise_count > 0:
        score = (1*apromise_count + 2*ncpromise_count + 3*ppromise_count + 4*cpromise_count)/(4*promise_count)
        party.score = round(score * 10, 2)

    context = {'page_obj':page_obj, 'party': party, 'promise_count':promise_count, 'cpromise_count':cpromise_count, 'ncpromise_count':ncpromise_count, 'ppromise_count':ppromise_count, 'apromise_count':apromise_count}
    return render(request, 'promise_keeper/party.html', context)

#Politician Template
def politician(request, slug):
    search = Politician.objects.filter(slug=slug).first()
    promises = Promise.objects.filter(by=search)
    politician = Politician.objects.filter(slug=slug).first()
    promise_count = promises.count()
    
    cpromise = promises.filter(status='C')
    ncpromise = promises.filter(status='NC')
    ppromise = promises.filter(status='P')
    apromise = promises.filter(status='A')
    
    cpromise_count = cpromise.count()
    ncpromise_count = ncpromise.count()
    ppromise_count = ppromise.count()
    apromise_count = apromise.count()

    paginator = Paginator(promises, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    if promise_count > 0:
        score = (1*apromise_count + 2*ncpromise_count + 3*ppromise_count + 4*cpromise_count)/(4*promise_count)
        politician.score = round(score * 10, 2)

    context = {'page_obj':page_obj, 'politician': politician, 'promise_count':promise_count, 'cpromise_count':cpromise_count, 'ncpromise_count':ncpromise_count, 'ppromise_count':ppromise_count, 'apromise_count':apromise_count}
    return render(request, 'promise_keeper/politician.html', context)

#Search Page
def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPromise = Promise.objects.none()
        politicians = Politician.objects.none()
        parties = Party.objects.none()
    elif len(query)<1:
        allPromise = Promise.objects.none()
        politicians = Politician.objects.none()
        parties = Party.objects.none()
    else:
        allPromise = Promise.objects.filter(name__icontains=query)
        politicians = Politician.objects.filter(name__icontains=query)
        parties = Party.objects.filter(name__icontains=query)
    if allPromise.count() == 0 and politicians.count() == 0 and parties.count() == 0:
        messages.warning(request, "No Search Result Found. Please Refine Your Query")
    paginator = Paginator(allPromise, 30)
    paginator2 = Paginator(politicians, 15)
    paginator3 = Paginator(parties, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    politician0 = request.GET.get('page')
    politician1 = paginator2.get_page(politician0)

    parties0 = request.GET.get('page')
    parties1 = paginator3.get_page(parties0)
    context = {'page_obj':page_obj, 'query':query, 'politician1':politician1, 'parties1':parties1, 'query':query}
    return render(request, 'promise_keeper/search.html', context)
    # return HttpResponse('This is search')

#Politician List Page
def politician_list(request):
    allPolitician = Politician.objects.all()
    paginator = Paginator(allPolitician, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request, 'promise_keeper/politician_list.html', context)

#Parties Page
def parties_list(request):
    allParties = Party.objects.all()
    paginator = Paginator(allParties, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request, 'promise_keeper/parties_list.html', context)