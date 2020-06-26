from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import Pic


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def art_of_day(request):
    date = dt.date.today()
    return render(request, 'all-art/today-art.html', {"date": date,})


def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day


def art_today(request):
    date = dt.date.today()
    art = Pic.todays_art()
    return render(request, 'all-art/today-art.html', {"date": date,"art":art})

def search_results(request):

    if 'pic' in request.GET and request.GET["pic"]:
        search_term = request.GET.get("pic")
        searched_pics = Pic.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"pics": searched_pics})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

