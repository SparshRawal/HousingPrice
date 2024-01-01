from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import HouseFeatures
from .forms import HouseFeaturesForm
from .serializers import HouseSerializers
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponseRedirect, JsonResponse
from rest_framework.permissions import AllowAny 
from rest_framework.decorators import permission_classes 
from .predict import predictPrice
import json
# Create your views here.
@api_view(['POST','GET','PUT'])
@permission_classes([AllowAny])
def predict_price(request):
    if request.method == 'POST':
        data=request.data
        
        serializer = HouseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            price = predictPrice(dict(data))
            pred,predprices,weights = price.preProcessAndPredict()
            values = [float(arr[0]) for arr in predprices[0]]
            # weights = [float(arr[0]) for arr in weights]
            response = {"PredictedPrice":pred,
                        "PredictedPriceList":values,
                        "Weights":weights}
            response_data = json.dumps(response)

            return JsonResponse(response_data, status=status.HTTP_200_OK, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
