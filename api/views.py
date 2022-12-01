from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt     
def student_api(request):
    if request.method == "GET":
        print("Reached Here")
        json_data = request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)

        id=pythondata.get('id',None)
        
        if id != None:
            stu=Student.objects.get(id=id)
            print(stu)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            print("sending particular data")
            return HttpResponse(json_data,content_type='application/json')
        else:
            stu=Student.objects.all()
            serializer=StudentSerializer(stu,many=True)
            json_data=JSONRenderer().render(serializer.data)
            print("Sending data")
            return HttpResponse(json_data,content_type='application/json')
        
    if request.method == 'POST':
      
        json_data=request.body
        stream=io.BytesIO(json_data)

        pythondata=JSONParser().parse(stream)

        serializer=StudentSerializer(data=pythondata)
   
        if serializer.is_valid():
            print("valid")
            serializer.save()
            res={'msg':'data created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        else:
            print("Not valid")
            json_data=JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type='application/json')

    if request.method=='PUT':
        json_data=request.body
        print("reached here")
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        print(id)
        stu=Student.objects.get(id=id)
        print(stu)
        serializer=StudentSerializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data update!!!!'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

    if request.method == 'DELETE':
        print("Here")
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        print(id)
        stu=Student.objects.get(id=id)

        print(stu)
    
        stu.delete()

        res={'msg':"Data deleted successfully"}
        json_data=JSONRenderer().render(res)
        print(json_data)
        return HttpResponse(json_data,content_type='application/json')
