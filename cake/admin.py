from django.contrib import admin
from django.urls import path
from .models import userModel , product , category , shape , flavor , cart , review , order , blog , inquiry 
from .reports import get_weekly_report , get_monthly_report
from django.shortcuts import render

class Adminproduct(admin.ModelAdmin):
    list_display = ['id','name','price','category','date']

class Admincustomer(admin.ModelAdmin):
    list_display = ['username','email','contact','password','date']

class Admincart(admin.ModelAdmin):
    list_display = ['id','username','product','image','price']

class Adminorder(admin.ModelAdmin):
    list_display = ['username','delivery_name','date','address']
    ordering = ('-date',)
    list_filter = ('date',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('weekly-report/', self.admin_site.admin_view(self.weekly_report_view), name='weekly_report'),
            path('monthly-report/', self.admin_site.admin_view(self.monthly_report_view), name='monthly_report'),
        ]
        return custom_urls + urls

    def weekly_report_view(self, request):
        report = get_weekly_report()
        return render(request, 'admin/report.html', {'report': report, 'title': 'Weekly Report'})

    def monthly_report_view(self, request):
        report = get_monthly_report()
        return render(request, 'admin/report.html', {'report': report, 'title': 'Monthly Report'})

class Adminreview(admin.ModelAdmin):
    list_display = ['username','feedback','date']

class Adminblog(admin.ModelAdmin):
    list_display = ['title','date']

class Admininquiry(admin.ModelAdmin):
    list_display = ['username','date']

# class Adminreport(admin.ModelAdmin):
#     list_display = ['weekly_order','weekly_income','monthly_order','monthly_income']
    

admin.site.register(userModel , Admincustomer)
admin.site.register(category)
admin.site.register(product , Adminproduct)
admin.site.register(shape)
admin.site.register(flavor)
admin.site.register(cart , Admincart)
admin.site.register(review , Adminreview)
admin.site.register(order , Adminorder)
admin.site.register(blog , Adminblog)
admin.site.register(inquiry , Admininquiry)
# admin.site.register(report , Adminreport)
# Register your models here.
