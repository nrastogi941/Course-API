from django.http import JsonResponse

def CourseView(request):
    return JsonResponse({"msg":"Hello nimit rastogi"})