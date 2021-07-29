from django.shortcuts import render
import datetime
# Create your views here.


def index(request):
    day_now = datetime.datetime.today().strftime("%d/%m/%Y")
    return render(request, "new_year/index.html", {
        "date": day_now
    })
