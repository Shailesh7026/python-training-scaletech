from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets 

from .models import Student
from .serializers import StudentSerializer




# class StudentListCreateAPIView(APIView):
#     def get(self,request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data , status=status.HTTP_200_OK)

#     def post(self,request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

# class StudentDetailAPIView(APIView):
#     def get_object(self, pk):
#         try:
#             return Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             return None

#     def get(self, request, id):
#         student = self.get_object(id)
#         if student is None:
#             return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data , status=status.HTTP_200_OK)

#     def put(self, request, id):
#         student = self.get_object(id)
#         if student is None:
#             return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_200_OK)
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         student = self.get_object(id)
#         if student is None:
#             return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# View Set - auto generates 

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # custom query set - branch
    def get_queryset(self):
        queryset = Student.objects.all()

        branch = self.request.query_params.get("branch")
        if branch:
            queryset = queryset.filter(branch__iexact=branch)

        return queryset
     