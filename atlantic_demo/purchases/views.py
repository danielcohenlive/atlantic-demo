import csv

from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django.http import HttpResponse
from .forms import PurchaseFileForm


class UploadPurchaseView(View):
    def get(self, request):
        form = PurchaseFileForm()
        return render(request, 'upload_purchases.html', {'form': form})

    def post(self, request):
        form = PurchaseFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['csv_upload_file']
            csvReader = csv.reader(file, delimiter='\t')

            return HttpResponse(status=201)
        return HttpResponse(status=400)