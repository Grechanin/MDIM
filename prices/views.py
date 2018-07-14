from django.http import JsonResponse
from django.views.generic import FormView
from django.shortcuts import render, get_object_or_404
from .forms import OrderForm
from .models import Prices, PriceCategory, ProiceCategoryDescription, OrderModel

def prices(request):
	prices = Prices.objects.filter(is_active=True)[0]

	title = prices.title
	short_description = prices.short_description
	description = prices.description

	price_categorys = PriceCategory.objects.filter(is_active=True)
	price_category_description = ProiceCategoryDescription.objects.filter(is_active=True)
	context = {
			'title': title,
			'description': description,
			'short_description': short_description,
			'price_categorys':price_categorys,
			'price_category_description':price_category_description,
		}

	return render(request, 'prices/prices.html', context)


class OrderFormView(FormView):
    form_class = OrderForm
    template_name  = 'prices/order_form.html'
    success_url = '/prices/'


    def form_invalid(self, form):
        response = super(OrderFormView, self).form_invalid(form)
        if self.request.is_ajax():
            
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(OrderFormView, self).form_valid(form)
        form.save()
        if self.request.is_ajax():
            print(form.cleaned_data)
            data = {
                'message': "Successfully submitted form data."
            }
            return JsonResponse(data)
        else:
            return response