from django.http import Http404
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import RecordCollection,FeedBack


@api_view(['GET', 'POST'])
@csrf_exempt 
def record_submission(request):
    if request.method == 'POST':
        print(request.data)
        item = RecordCollection(complaint=request.data['complaint'],issue=request.data['issue'],aspect=request.data['aspect'])
        item.save()
        return Response({"message":"Thank You for response."}, status=status.HTTP_200_OK)
    
    return Response(request.data, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'POST'])
@csrf_exempt 
def feedback_submission(request):
    if request.method == 'POST':
        print("Feed back data")
        print(request.data)
        item = FeedBack(name=request.data['name'],review=request.data['review'])
        item.save()
        return Response({"message":"Thank You for response."}, status=status.HTTP_200_OK)
    
    return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@csrf_exempt 
def home(request):
    print(settings.GLOBAL_MODEL.predict([[12,12,12,12,12,12]]))
    if request.method == 'POST':
        # print(request.data)
        Age = request.data["Age"]
        Systolic = request.data["Systolic"]
        Diastolic = request.data["Diastolic"]
        BS = request.data["BS"]
        BodyTemp = request.data["BodyTemp"]
        HeartRate = request.data["HeartRate"]
        prediction = settings.GLOBAL_MODEL.predict([[Age,Systolic,Diastolic,BS,BodyTemp,HeartRate]])
        # print(prediction)
        text = "The Future Mother has a low level Risk"
        if(prediction == 2):
            text = "The Future Mother has a mid level Risk"
        elif(prediction == 3 ):
            text = "The Future Mother has a high level Risk"
        
        return Response({"message":text}, status=status.HTTP_200_OK)
    
    return Response(request.data, status=status.HTTP_400_BAD_REQUEST)




# @api_view(['GET', 'POST'])
# @csrf_exempt 
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         return Response({"name":"Saeem"}, status=status.HTTP_200_OK)
#         # MODEL = settings.GLOBAL_MODEL
#         # MODEL.eval()
#         # return Response(predict_issue(MODEL,request.data['complaint']), status=status.HTTP_200_OK)


#     elif request.method == 'POST':
#         print(request.data)
#         MODEL = settings.GLOBAL_MODEL
#         return Response(predict_issue(MODEL,request.data['complaint']), status=status.HTTP_200_OK)
#         # import json
#         # f = open("./Model/non_iid.json")
#         # data = json.load(f)
#         # f.close()
#         # return Response(data['Sheet1'], status=status.HTTP_200_OK)
    
#     return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt 
# def detail(request):
#         print(request.POST.get("name"))
#         # MODEL = settings.GLOBAL_MODEL
#         # MODEL.eval()
#         # text = ['pitch is low.','Display got a scratch','gave me damage box']
#         # for t in text:  
#         #         print(predict_issue(MODEL,t))
#         return JsonResponse({'name':"Saeem",'Age':10,"Gender":"Male"})

# Database : sqllite for string user feeedback and compile
# for 