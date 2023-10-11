from rest_framework import views, permissions, status
from rest_framework.response import Response
from datetime import datetime
from .serializers import *
from .authentication import JWTAuthentication
from .models import CustomUser as User
from django.db.models import Q

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
class TaskDeletion(views.APIView):
   permission_classes = [IsAuthenticated]
   def delete(self,request):
      try:
        user = request.user
        tid = request.data.get("task_id")
        if tid == None or tid == '':
           return Response({"status":"error","data":{"task_id":"Invalid task id provided"}})
        task = Task.objects.filter(task_id=tid,user=user).first()
        if task == None:
           return Response({"status":"error","data":{"task_id":"Invalid task id provided"}})
        if task.user.username != user.username:
           return Response({"status":"error","message":"Unauthorized access request"})
        task.delete()

        return Response({"status": "success", "message": "Successfully deleted task"}, status=status.HTTP_200_OK) 
      except Exception as e:
        print(e)
        return Response({"status":"internal-error","message":"An unexpected error occured"})
class TaskEditView(views.APIView):
   permission_classes = [IsAuthenticated]

   def patch(self,request):
      try:
        user = request.user
        tid = request.data.get("task_id")
        if tid == None or tid == '':
           return Response({"status":"error","data":{"task_id":"Invalid task id provided"}})
        task = Task.objects.filter(task_id=tid,user=user).first()
        if task == None:
           return Response({"status":"error","data":{"task_id":"Invalid task id provided"}})
        serializer = TaskAddSerializer(data=request.data,context={"user":user}) 
        if serializer.is_valid():
          serializer.update(task,serializer.validated_data)
          return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK) 
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
      except Exception as e:
        print(e)
        return Response({"status":"internal-error","message":"An unexpected error occured"})  
class TaskMarkCompleted(views.APIView):
   permission_classes = [IsAuthenticated]

   def patch(self,request):
      try:
        user = request.user
        tid = request.data.get("task_id")
        if tid == None or tid == '':
           return Response({"status":"error","data":{"task_id":"Invalid task id provided"}})
        task = Task.objects.filter(task_id=tid,user=user).first()
        if task == None:
           return Response({"status":"error","data":{"task_id":"Invalid task id provided"}})
        serializer = TaskMarkCompletedSerializer(data=request.data,context={"user":user}) 
        if serializer.is_valid():
          serializer.update(task,serializer.validated_data)
          return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK) 
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
      except Exception as e:
        print(e)
        return Response({"status":"internal-error","message":"An unexpected error occured"})  
class TaskGetView(views.APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
      try:
          user = request.user
          state = request.query_params.get('status')  
          print(dir(request))
          if state == "expired":
            tasks = Task.objects.filter(user=user,completed=False,date_of_completion__lt= datetime.now())
            pass
          elif state == "completed":
            tasks = Task.objects.filter(user=request.user,completed=True)
          elif state == "pending":
            tasks = Task.objects.filter(Q(date_of_completion__gt=datetime.now()) | Q(date_of_completion__isnull=True),user=request.user,completed=False)
          else:
             tasks = Task.objects.filter(user=user)
          serializer = TaskSerializer(tasks, many=True)
          return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
      except Exception as e:
         print(e)
         return Response({"status":"internal-error","message":"An unexpected error occured"})  
class TaskAddView(views.APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
      try:
          user = request.user
          serializer = TaskAddSerializer(data=request.data,context={"user":user})
          if serializer.is_valid():
              serializer.save()
              return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
          return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
      except Exception as e:
         print(e)
         return Response({"status":"internal-error","message":"An unexpected error occured"})

class UserRegistrationView(views.APIView):
    def post(self, request):
      try:
        serializer = UserSerializer(data=request.data) 
        if serializer.is_valid():  
            serializer.save() 
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
      except:
          return Response({"status":"internal-error","message":"An unexpected error occured"})
        
 
 
# AUTHORIZATION: Bearer <TOKEN>
class ObtainTokenView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ObtainTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = User.objects.filter(username=username).first()
        # print(user.check_password(password),password,user.password)
        if user is None or not user.password== password:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        # Generate the JWT token
        jwt_token = JWTAuthentication.create_jwt(user)

        return Response({'token': jwt_token})