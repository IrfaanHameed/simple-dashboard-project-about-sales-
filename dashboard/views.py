# dashboard/views.py

from django.shortcuts import render
from .models import Sale
import json
import datetime

def dashboard(request):
    # Query to get sales data for the last 30 days
    last_30_days_sales = Sale.objects.filter(
        date__gte=datetime.date.today() - datetime.timedelta(days=30)
    ).order_by('date')

    # Prepare data for charts
    dates = [sale.date.strftime('%Y-%m-%d') for sale in last_30_days_sales]
    amounts = [float(sale.amount) for sale in last_30_days_sales]

    # Calculate counts for pie chart
    completed_sales_count = Sale.objects.filter(status='done').count()
    pending_sales_count = Sale.objects.filter(status='pending').count()

    # Calculate total sales for bar chart
    total_sales = Sale.objects.count()
    completed_sales = Sale.objects.filter(status='done').count()
    pending_sales = Sale.objects.filter(status='pending').count()

    context = {
        'dates': json.dumps(dates),
        'amounts': json.dumps(amounts),
        'completed_sales_count': completed_sales_count,
        'pending_sales_count': pending_sales_count,
        'total_sales': total_sales,
        'completed_sales': completed_sales,
        'pending_sales': pending_sales,
    }
    return render(request, 'dashboard.html', context)





