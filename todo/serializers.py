# apps/management/api/serializers.py

from rest_framework import serializers,validators
from .models import *
"""
Task Mark COmpleted Serializer
"""
class TaskMarkCompletedSerializer(serializers.ModelSerializer):
    task_id = serializers.IntegerField(required=True)
    completed = serializers.BooleanField(required=True)

    def update(self, instance, validated_data):  
        user = self.context.get("user")
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()  
        return instance

    class Meta:
        model = Task
        fields = ['task_id','completed']
"""
Add Task Serializer
"""
class TaskAddSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    date_of_completion = serializers.DateTimeField(required=False)

    def create(self,validated_data):
        title = validated_data.get("title")
        date_co = validated_data.get("date_of_completion")
        user = self.context['user']
        task = Task(title=title,completed=False,date_of_completion=date_co,user=user)
        task.save()
        return task

    def update(self,instance,validated_data):
        instance.title = validated_data.get("title",instance.title)
        instance.date_of_completion = validated_data.get("date_of_completion",instance.date_of_completion)

        instance.save()
        return instance
    class Meta:
        model = Task
        fields = ['title','date_of_completion']

"""
Task Serializer
"""
class TaskSerializer(serializers.ModelSerializer):
    task_id = serializers.IntegerField(required=True)
    title = serializers.CharField(required=True)
    completed = serializers.BooleanField(required=False)
    date_of_completion = serializers.DateTimeField(required=False)

    class Meta:
        model = Task
        fields = ['task_id','title','date_of_completion','completed']

"""
User Serializer
"""
class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True,validators=[validators.UniqueValidator(queryset=CustomUser.objects.all())])
    username = serializers.CharField(required=True,validators=[validators.UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(required=True)

    def create(self, validated_data):  
        """ 
        Create and return a new `Students` instance, given the validated data. 
        """  
        return CustomUser.objects.create(**validated_data)  
  
    def update(self, instance, validated_data):  
        """ 
        Update and return an existing `Students` instance, given the validated data. 
        """  
        instance.first_name = validated_data.get('first_name', instance.first_name)  
        instance.last_name = validated_data.get('last_name', instance.last_name)  
        instance.email = validated_data.get('email', instance.email)  
        instance.roll_number = validated_data.get('username', instance.username)  
        instance.password = validated_data.get('password', instance.password)  
  
        instance.save()  
        return instance  
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','username','password']
"""
Obtain Token Serializer
"""
class ObtainTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()