from home.models import FaviconImage

def favicon(request):
	favicon = FaviconImage.objects.filter(is_active=True).last()
	print (favicon.name)

	return {"favicon": favicon}