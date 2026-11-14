from django.contrib import admin
from .models import ChaiVarietie, ChaiReview, Store, ChaiCertificate, Order, OrderItem


# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 1  # Number of extra forms to display

class ChaiCertificateInline(admin.StackedInline):
    model = ChaiCertificate
    extra = 1  # Number of extra forms to display

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Number of extra forms to display

class ChaiVarietieAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'date_added')
    search_fields = ('name', 'description')
    list_filter = ('type',)
    inlines = [ChaiReviewInline, ChaiCertificateInline]  # Add the inline for reviews and certificates


class storeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')
    filter_horizontal = ('chai_varieties',)  # Use a horizontal filter for the many-to-many field

class chaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issue_date', 'expiry_date')
    search_fields = ('chai__name', 'certificate_number')  # Search by chai name and certificate number
    list_filter = ('issue_date', 'expiry_date')  # Filter by issue and expiry dates


class OrderAdmin(admin.ModelAdmin):
    search_fields = ('order_id', 'user__username') 
    list_display = ('order_id', 'user', 'created_at', 'total_amount')
    inlines = [OrderItemInline]  # Add the inline for order items
    readonly_fields = ('total_amount',)
 
    
    
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'chai', 'quantity')
    search_fields = ('order__order_id', 'chai__name')  # Search by order ID and chai name
    list_filter = ('order', 'chai','order__user__username')  # Filter by order and chai
    


admin.site.register(ChaiVarietie, ChaiVarietieAdmin)
admin.site.register(Store, storeAdmin)
admin.site.register(ChaiCertificate, chaiCertificateAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)