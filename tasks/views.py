from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Platform, Duty, Task
from .serializers import PlatformSerializer, DutySerializer, TaskSerializer
from rest_framework.permissions import AllowAny
from django.db.models import Sum, Q
from datetime import date


class TaskListView(APIView):
    
    permission_classes = [IsAuthenticated]
    

    def get(self, request):
        tasks = Task.objects.filter(owner=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskTotalView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.filter(owner=request.user).order_by('created_at')
        total = tasks.count()

        # 상태별 개수
        start_date = tasks.first().created_at
        expired_count = tasks.filter(status=Task.StatusChoices.expired).count()
        in_progress_count = tasks.filter(status=Task.StatusChoices.in_progress).count()
        completed_count = tasks.filter(status=Task.StatusChoices.completed).count()
        cancelled_count = tasks.filter(status=Task.StatusChoices.cancelled).count()


        # 타입별 개수
        food_count = tasks.filter(type=Task.TypeChoices.food).count()
        stuff_count = tasks.filter(type=Task.TypeChoices.stuff).count()
        activity_count = tasks.filter(type=Task.TypeChoices.activity).count()

        # 완료된 작업의 총 금액 
        completed_money = tasks.filter(
            status=Task.StatusChoices.completed
        ).aggregate(
            total_money=Sum('money')
        )['total_money'] or 0



        return Response({
            "total": total,
            "start_date": start_date,
            "expired_count": expired_count,
            "in_progress_count": in_progress_count,
            "completed_count": completed_count,
            "cancelled_count": cancelled_count,
            "food_count": food_count,
            "stuff_count": stuff_count,
            "activity_count": activity_count,
            "completed_money": completed_money,
        })
    
class TaskDateUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.filter(
            Q(due_date__lt=date.today()) & 
            Q(status=Task.StatusChoices.in_progress)
        )
        
        tasks.update(status=Task.StatusChoices.completed) 
        return Response({"updated": "ok"})

class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        task = Task.objects.get(pk=pk, owner=request.user)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    

class TaskTest(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"test": "test"})   
    
class PlatformListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        platforms = Platform.objects.filter(owner=request.user)
        serializer = PlatformSerializer(platforms, many=True)
        return Response(serializer.data)

class TaskStatusUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        task = Task.objects.get(pk=pk, owner=request.user)
        task.status = request.data['status']
        task.save()
        return Response({"status": "updated"})
        
class ModifyTaskView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        task = Task.objects.get(pk=pk, owner=request.user)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteTaskView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        task = Task.objects.get(pk=pk, owner=request.user)
        task.delete()
        return Response({"deleted": "ok"})  

class AddPlatformView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

