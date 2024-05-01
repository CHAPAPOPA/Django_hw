from django.shortcuts import render

import csv


def home_page(request):
    return render(request, 'home_page.html')


def contact_information(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')

        with open('contact_info.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, message])

    return render(request, 'contact_information.html')
