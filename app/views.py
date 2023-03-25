from .models import CourseModel
from .serializers import CourseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET' , 'POST'])
def CourseView(request):
    
    if request.method == 'GET':
        course_details=CourseModel.objects.all()
        course_details_serializer=CourseSerializer(course_details,many=True)
        return Response(course_details_serializer.data)
    
    elif request.method == 'POST':
        course_details_serializer=CourseSerializer(data=request.data)
        if course_details_serializer.is_valid():
            course_details_serializer.save()
            return Response(course_details_serializer.data)
        else:
            return Response(course_details_serializer.errors)
        