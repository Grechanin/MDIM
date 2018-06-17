from django.shortcuts import render, get_object_or_404
from .models import Prices, PriceCategory, ProiceCategoryDescription

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