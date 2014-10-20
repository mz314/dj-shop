from django.shortcuts import render


def gateway(request):
    return render(request,'payments/invoice/invoice.html')