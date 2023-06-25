from django.conf import settings
from django.http import JsonResponse
from Convox.convox_api_call import ConvoxApiClient

def make_call_view(request):
    phone_number = request.POST.get('phone_number')
    convox_api = ConvoxApiClient(settings.CONVOX_API_KEY, settings.CONVOX_API_URL)
    response = convox_api.make_call(phone_number)
    return JsonResponse(response)
