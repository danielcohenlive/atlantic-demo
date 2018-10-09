from django.conf.urls import url

from purchases.views import UploadPurchaseView

urlpatterns = [
    url(r'', UploadPurchaseView.as_view()),
]