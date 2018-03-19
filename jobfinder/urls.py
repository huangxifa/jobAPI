from django.urls import path
from jobfinder import views

app_name = "jobfinder"
#
# router = routers.DefaultRouter()
# router.register(r'saleorder', rest_view.SaleOrderViewSet)

urlpatterns = [
    # default index
    # path('home', views.home, name="home"),
    # 销售订单管理
    path('excute',views.excute, name='index')
    ]