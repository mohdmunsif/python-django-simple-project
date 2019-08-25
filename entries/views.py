from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

from .models import Entries
from .forms import EntriesForm


@login_required
def index(request):
    return HttpResponse("FINAL PROJECT TOYS")


@login_required
def browse(request):
    if request.method == 'GET':
        try:
            entries = Entries.objects.all()
            paginator = Paginator(entries, 5)
            page = request.GET.get('page')
            entries = paginator.get_page(page)

        except Entries.DoesNotExist:
            raise Http404("Entries does not exist")
        context = {
            "entries": entries
        }

        return render(request, "entries/index.html", context)
    else:  # POST
        raise Http404("Error encountered")


@login_required
def search(request):
    if request.method == 'POST':
        try:
            searchval = request.POST['searchstr']
            # entries = Entries.objects.filter(toyname__icontains=searchval)
            entries = Entries.objects.filter(
                Q(toyname__icontains=searchval) | Q(descr__icontains=searchval))
            paginator = Paginator(entries, 5)
            page = request.GET.get('page')
            entries = paginator.get_page(page)

        except Entries.DoesNotExist:
            raise Http404("Entries does not exist")
        context = {
            "entries": entries
        }

        return render(request, "entries/index.html", context)
    else:  # POST
        raise Http404("Error encountered")


@login_required
def searchage(request):
    if request.method == 'POST':
        try:
            searchval = request.POST['age_filter']
            entries = Entries.objects.filter(
                age_lower__lte=searchval)
            paginator = Paginator(entries, 5)
            page = request.GET.get('page')
            entries = paginator.get_page(page)

        except Entries.DoesNotExist:
            raise Http404("Entries does not exist")
        context = {
            "entries": entries
        }

        return render(request, "entries/index.html", context)
    else:  # POST
        raise Http404("Error encountered")


@login_required
def submit(request):
    if request.method == 'GET':  # display form
        context = {
            "entries": Entries.objects.all(),
            "form": EntriesForm()
        }
        return render(request, "entries/submit.html", context)
    else:
        if request.method == 'POST':
            form = EntriesForm(request.POST, request.FILES)
            if form.is_valid():
                entry = form.save(commit=False)
                entry.username = request.user
                entry.datetime = timezone.now()
                entry.save()
                return redirect('entries:oneentry', entry_id=entry.pk)
            else:
                # return HttpResponse("FORM ERROR?")
                return render(request,  "entries/submit.html", {"form": form})
        else:
            return HttpResponse("WHAT METHOD DID YOU USE?")


@login_required
def welcome(request):
    return HttpResponse("FINAL PROJECT TOYS - welcome URL")


@login_required
def oneentry(request, entry_id):
    if request.method == 'GET':
        try:
            entry = Entries.objects.get(pk=entry_id)
        except Flight.DoesNotExist:
            raise Http404("No such toy")

        context = {
            "entry_id": entry_id,
            "entry": entry
        }
        return render(request, "entries/oneentry.html", context)
    else:  # post
        return HttpResponse("FINAL PROJECT TOYS - browse URL")

    # return HttpResponse("FINAL PROJECT TOYS - browse URL")
