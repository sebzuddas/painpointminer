from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .integrations import elevenlabs_tts, run_langflow
# Create your views here.

@api_view(['GET'])
def ping(request):
    return Response({'message': 'pong'})

@api_view(['POST'])
def tts(request):
    text = request.data.get('text')
    result = elevenlabs_tts(text)
    return Response(result)


# api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def langflow_chat(request):
    input_value = request.data.get('input_value', '')
    result = run_langflow(input_value)
    return Response(result)