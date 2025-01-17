from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.db.models import F
from .models import Product, Purchase

# Create your views here.
def index(request):
    products = Product.objects.exclude(quantity = 0)
    context = {'products': products}
    return render(request, 'shop/index.html', context)

class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'person', 'address']

    def form_valid(self, form):
        self.object = form.save()
        products = Product.objects.filter(name=self.object.product.name).update(quantity=F('quantity') - 1)
        return HttpResponse(f'Спасибо за покупку, {self.object.person}!')
