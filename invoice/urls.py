from django.urls import path

from invoice import views


urlpatterns = [
    # 一覧画面
    path('',  views.InvoiceFilterView.as_view(template_name = "invoice/invoice_filter.html"), name='index'),
    # 詳細画面
    path('detail/<int:pk>/', views.InvoiceDetailView.as_view(template_name = "invoice/invoice_detail.html"), name='detail'),
    # 登録画面
    path('create/', views.InvoiceCreateView.as_view(template_name = "invoice/invoice_form.html"), name='create'),
    # 更新画面
    path('update/<int:pk>/', views.InvoiceCreateView.as_view(template_name = "invoice/invoice_form.html"), name='update'),
    # 削除画面
    path('delete/<int:pk>/', views.InvoiceDeleteView.as_view(template_name = "invoice/invoice_confirm_delete.html"), name='delete'),
    
    path("index/",views.HomeTemplateView.as_view(template_name = "invoice/index.html"), name="blogs"),

]