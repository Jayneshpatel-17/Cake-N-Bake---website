from django.utils import timezone
from django.db.models import Sum, Count
from datetime import timedelta
from .models import order

def get_weekly_report():
    today = timezone.now().date()
    start_of_week = today - timedelta(days=today.weekday())  # Start of the week (Monday)
    end_of_week = start_of_week + timedelta(days=6)  # End of the week (Sunday)

    weekly_orders = order.objects.filter(date__date__range=[start_of_week, end_of_week])
    total_sales = weekly_orders.aggregate(total=Sum('total'))['total'] or 0
    total_orders = weekly_orders.count()

    return {
        "start_of_week": start_of_week,
        "end_of_week": end_of_week,
        "total_orders": total_orders,
        "total_sales": total_sales,
    }

def get_monthly_report():
    today = timezone.now().date()
    start_of_month = today.replace(day=1)  # Start of the month
    end_of_month = (start_of_month + timedelta(days=31)).replace(day=1) - timedelta(days=1)  # End of the month

    monthly_orders = order.objects.filter(date__date__range=[start_of_month, end_of_month])
    total_sales = monthly_orders.aggregate(total=Sum('total'))['total'] or 0
    total_orders = monthly_orders.count()

    return {
        "start_of_month": start_of_month,
        "end_of_month": end_of_month,
        "total_orders": total_orders,
        "total_sales": total_sales,
    }