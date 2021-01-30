from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import userSerializer, attendanceSerializer, geologSerializer
from .models import user, attendance, geolog
# from django.views.decorators.csrf import csrf_exempt
import json
# from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
# from rest_framework import generics
# from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
# from rest_framework import viewsets
from django.shortcuts import get_object_or_404
# from django.views.generic.list import ListView
# from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
# from rest_framework. permissions import IsAuthenticated


# -------------------------------------generic viewset---------------------------
# class userViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
#     serializer_class = userSerializer
#     queryset = user.objects.all()  

# -----------------------class based APIView-------------------------------
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
# --------------------------User Start -------------------------------------
class userAPIView(APIView):
    def get (self, request):
        users = user.objects.all()
        serializer = userSerializer(users, many=True)
        return Response (serializer.data)
    
    def post(self, request):
        users = user.objects.all()
        data = request.POST

        for user_s in users:
            if(data["cnic"] == user_s.cnic and data["imei"] == user_s.imei):
                resp = "Duplicate"
                return HttpResponse(resp)

        serializer = userSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class user_detail(APIView):
    def get_object(self, cnic):
        try:
            return user.objects.get(cnic=cnic)

        except user.DoesNotExist:

            return HttpResponse(status=status.HTTP_400_NOT_FOUND)

    def get(self, request, cnic):
        user_d = self.get_object(cnic)
        serializer = userSerializer(user_d)
        return JsonResponse(serializer.data)


    def put (self, request, cnic):
        user_d = self.get_object(cnic)
        serializer = userSerializer(user_d, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete (self, request, cnic):
        user_d = self.get_object(cnic)
        user_d.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# --------------------------User End-------------------------------------
# --------------------------Attendance Start -------------------------------------


class attendanceAPIView(APIView):

    def get (self, request):
        att = attendance.objects.all()
        serializer = attendanceSerializer(att, many=True)
        return Response (serializer.data)
    
    def post(self, request):
        att = user.objects.all()
        data = request.POST

        for user_s in att:
            if(data["cnic"] == user_s.cnic and data["imei"] == user_s.imei):
                data._mutable = True
                resp = user_s.id
                data["user_id"] = resp
                serializer = attendanceSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_201_CREATED)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class attendance_detail(APIView):
    def get_object(self, cnic):
        try:
            return attendance.objects.get(cnic=cnic)

        except attendance.DoesNotExist:

            return HttpResponse(status=status.HTTP_400_NOT_FOUND)

    def get(self, request, cnic):
        att_d = self.get_object(cnic)
        serializer = attendanceSerializer(att_d)
        return JsonResponse(serializer.data)


    def put (self, request, cnic):
        att_d = self.get_object(cnic)
        serializer = attendanceSerializer(att_d, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete (self, request, cnic):
        att_d = self.get_object(cnic)
        att_d.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# --------------------------Attendance End -------------------------------------
# --------------------------Geolog Start -------------------------------------
class geologAPIView(APIView):

    def get (self, request):
        geo = geolog.objects.all()
        serializer = geologSerializer(geo, many=True)
        return Response (serializer.data)
    
    def post(self, request):
        geo = user.objects.all()
        data = request.POST

        for user_s in geo:
            if(data["cnic"] == user_s.cnic and data["imei"] == user_s.imei):
                data._mutable = True
                resp = user_s.id
                data["user_id"] = resp
                serializer = geologSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class geolog_detail(APIView):
    def get_object(self, cnic):
        try:
            return geolog.objects.get(cnic=cnic)

        except geolog.DoesNotExist:

            return HttpResponse(status=status.HTTP_400_NOT_FOUND)

    def get(self, request, cnic):
        geolog_d = self.get_object(cnic)
        serializer = geologSerializer(geo_d)
        return JsonResponse(serializer.data)


    def put (self, request, cnic):
        geo_d = self.get_object(cnic)
        serializer = attendanceSerializer(geo_d, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete (self, request, cnic):
        geo_d = self.get_object(cnic)
        geo_d.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------Geolog end-------------------------------

# -----------------------class based APIView end-------------------------------



# # ---------------------------Serializer Base------------------------------

# # ------------------------USER--------------------------------------------
# @csrf_exempt
# def user_list(request):
#     try:
#         if request.method =='GET':
#             users = user.objects.all()
#             serializer = userSerializer(users, many=True)
#             return JsonResponse(serializer.data, safe=False)
#         elif request.method == 'POST':
# # ---------------------------------------get-----------------------------
#             users2 = user.objects.all()
# # ----------------------------post--------------------------------
#             data_fetched = request.body
#             x = json.loads(data_fetched, object_hook=lambda d: SimpleNamespace(**d))
#             x.cnic
#             for user_s in users2:
#                 if(x.cnic == user_s.cnic and x.imei == user_s.imei):
#                     resp = "Duplicate"
#                     return HttpResponse(resp)

#             data = JSONParser().parse(request)
#             serializer = userSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return HttpResponse(data_fetched)
#                 # return JsonResponse(serializer.data, status = 201)
#             return JsonResponse(serializer.errors, status=400)
#     except ValueError:
#         print('error')

# @csrf_exempt
# def user_detail(request, cnic):
#     try:
#         user_d = user.objects.filter(cnic=cnic)

#     except user.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method =='GET':
#         serializer = userSerializer(user_d,many=True)
#         return JsonResponse(serializer.data, safe=False)
    


# # def user_detail(request, pk):
# #     try:
# #         user_d = user.objects.filter(pk=pk)

# #     except user.DoesNotExist:
# #         return HttpResponse(status=404)
# #     if request.method =='GET':
# #         serializer = userSerializer(user_d)
# #         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = userSerializer(user_d, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
    
#     elif request.method == 'DELETE':
#         user_d.delete()
#         return HttpResponse(status=204)

# ------------------------------USER END----------------------------

# ------------------------------attendance--------------------------
# @csrf_exempt
# def attendance_list(request):
#     try:
#         if request.method =='GET':
#             att = attendance.objects.all()
#             serializer = attendanceSerializer(att, many=True)
#             return JsonResponse(serializer.data, safe=False)
#         elif request.method == 'POST':
#             data = JSONParser().parse(request)
#             serializer = attendanceSerializer(data=data)

#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data, status = 201)
#             return JsonResponse(serializer.errors, status=400)
#     except ValueError:
#         print('error')

# @csrf_exempt
# def attendance_detail(request, cnic):
#     try:
#         att_d = attendance.objects.filter(cnic=cnic)

#     except attendance.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method =='GET':
#         serializer = attendanceSerializer(att_d,many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = attendanceSerializer(att_d, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
    
#     elif request.method == 'DELETE':
#         att_d.delete()
#         return HttpResponse(status=204)

# # -------------------------------attendance end------------------------

# # ------------------------------geolog--------------------------
# @csrf_exempt
# def geolog_list(request):
#     try:
#         if request.method =='GET':
#             geo = geolog.objects.all()
#             serializer = geologSerializer(geo, many=True)
#             return JsonResponse(serializer.data, safe=False)
#         elif request.method == 'POST':
#             data = JSONParser().parse(request)
#             serializer = geologSerializer(data=data)

#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse(serializer.data, status = 201)
#             return JsonResponse(serializer.errors, status=400)
#     except ValueError:
#         print('error')

# @csrf_exempt
# def geolog_detail(request, cnic):
#     try:
#         geo_d = geolog.objects.filter(cnic=cnic)

#     except geolog.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method =='GET':
#         serializer = geologSerializer(geo_d,many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = geologSerializer(geo_d, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
    
#     elif request.method == 'DELETE':
#         geo_d.delete()
#         return HttpResponse(status=204)

# # -------------------------------geolog end------------------------


# -----------------------------------routers & viewset---------------------------

# class userViewSet(viewsets.ViewSet):
#     def list(self, request):
#         users = user.objects.all()
#         serializer = userSerializer(users, many=True)
#         return Response(serializer.data)

#     def create(self,request):
#         serializer = userSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self, request, cnic=None):
#         queryset = user.objects.all()
#         user = get_object_or_404(queryset, cnic=cnic)
#         serializer = userSerializer(user)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         user_d = user.objects.get(cnic=pk)
#         serializer = userSerializer(user_d, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             # return Response(user_d)
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -----------------------------------routers & viewset end---------------------------
    

# # ------------------------------Generic views and mixins----------------------------

# class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
#     serializer_class = userSerializer
#     queryset = user.objects.all()
        # authentication_classes = [SessionAuthentication, BasicAuthentication]



#     lookup_field = "cnic"

#     def get(self, request, cnic=None):
#         if cnic:
#             return self.retrieve(request)
#         else:
#             return self.list(request)

#     def post (self, request):
#         return self.create(request)
    
#     def put (self, request, cnic=None):
#         return self.update(request, cnic)

#     def delete(self, request, cnic=None):
#         return self.destroy(request, cnic)

# # ------------------------------Generic views and mixins end----------------------------

# ----------------------------function based api view----------------------------
# @api_view(['GET', 'POST'])
# def user_list(request):
#     if request.method == 'GET':
#         users = user.objects.all()
#         serializer = userSerializer(users, many=True)
#         return Response (serializer.data)

#     elif request.method == 'POST':
#         serializer = userSerializer (data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def user_detail(request, cnic):
#     try:
#         user_d = user.objects.get(cnic=cnic)

#     except user.DoesNotExist:

#         return HttpResponse(status=status.HTTP_400_NOT_FOUND)

#     if request.method =='GET':
#         serializer = userSerializer(user_d)
#         return JsonResponse(serializer.data)
#         # return HttpResponse(user_d)


#     elif request.method == 'PUT':
#         serializer = userSerializer(user_d, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         user_d.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------------------function based api view  end----------------------------
