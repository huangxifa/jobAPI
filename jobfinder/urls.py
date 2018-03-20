from django.urls import path
from jobfinder import views,rest_model

app_name = "jobfinder"
#
# router = routers.DefaultRouter()
# router.register(r'saleorder', rest_view.SaleOrderViewSet)

urlpatterns = [
    # default index
    # path('home', views.home, name="home"),
    # 执行爬虫的触发url
    path('excute',views.excute, name='index'),
    path("rest/joblist", rest_model.Jobdetail.as_view(), name="rest_job"),

]