from django.http import JsonResponse
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from.serializers import *
from django.contrib.auth.models import User
from UserProfiles.models import *
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from UserProfiles.models import *


@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def check_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)

    if user is not None:
        # Authentication successful
        user=User.objects.get(username=username)
        profile=Profile.objects.get(user=user)
        role=profile.Role
        return Response({'message': 'Login successful', 'role': role}, status=status.HTTP_200_OK)
    elif username is not None:
        # Username exists but password is wrong
        return Response({'error': 'Incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        # User not found
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def getProfiles(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data['user'])
        if serializer.is_valid():
            user_data = serializer.validated_data
            user = User.objects.create_user(
                username=user_data['username'],
                password=user_data['password'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                email=user_data['email']
            )
            user.save()
            profile = Profile.objects.get(user=user)
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def getProfile(request, username):
    try:
        if username.isdigit():
            user = User.objects.get(id=username)
            profile=Profile.objects.get(user=user)
        else:
            user = User.objects.get(username=username)
            profile=Profile.objects.get(user=user)
    except user.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
    except Profile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        profile = Profile.objects.get(user=user)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def getJobPosts(request):
    if request.method == 'GET':
        job_posts = JobPost.objects.all()
        serializer = JobPostSerializer(job_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = JobPostSerializer(data=request.data)
        try:
            manager=User.objects.get(id=request.data['Manager'])
        except User.DoesNotExist:
            return Response(
                {"error": f"User does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
        if serializer.is_valid():
            serializer.save()
            Subject = 'New Job Post'
            Body = f"Your jobpost for {request.data['Title']} has been posted succesfully."
            send_mail(
                Subject, Body, settings.EMAIL_HOST_USER, [manager.email], fail_silently=False
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def getJobPost(request, pk):
    if pk.isdigit():
        try:
            job_post = JobPost.objects.get(id=pk)
        except JobPost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = JobPostSerializer(job_post)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serializer = JobPostSerializer(job_post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            job_post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
            try:
                user=User.objects.get(username=pk)
                job_posts = JobPost.objects.filter(Manager=user.id)
                if not job_posts.exists():
                    return Response(
                        {"error": "No job posts found for this manager."},
                        status=status.HTTP_404_NOT_FOUND
                    ) 
                serializer = JobPostSerializer(job_posts, many=True)
                return Response(serializer.data)
            except ObjectDoesNotExist as e:
                return Response(
                    {"error": f"User does not exist: {str(e)}"},
                    status=status.HTTP_404_NOT_FOUND
                )
            except Exception as e:
                return Response(
                    {"error": f"Server error: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )


@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def getJobApplications(request):
    if request.method == 'GET':
        job_applications = JobApplication.objects.all()
        serializer = JobApplicationSerializer(job_applications, many=True)
        return Response(serializer.data, status=200)

    elif request.method == 'POST':
        serializer = JobApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def getJobApplication(request, id):
    if id.isdigit():
        try:
            job_application = JobApplication.objects.get(id=id)
        except JobApplication.DoesNotExist:
            return Response({'error': 'Job application not found'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = JobApplicationSerializer(job_application)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = JobApplicationSerializer(job_application, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            job_application.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
            try:
                user = User.objects.get(username=id)
                job_applications = JobApplication.objects.filter(Student=user.id)
                if not job_applications.exists():
                    return Response(
                        {"error": "No job applications found for this user."},
                        status=status.HTTP_404_NOT_FOUND
                    ) 
                serializer = JobApplicationSerializer(job_applications, many=True)
                return Response(serializer.data)
            except ObjectDoesNotExist as e:
                return Response(
                    {"error": f"User does not exist: {str(e)}"},
                    status=status.HTTP_404_NOT_FOUND
                )
            except Exception as e:
                return Response(
                    {"error": f"Server error: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getWaitlist(request, jobid, username):
    try:
        jobpost = JobPost.objects.get(id=jobid)
        student = Profile.objects.get(user__username=username)
        application = JobApplication.objects.filter(jobPost=jobpost,ApplicationStatus='waitlist').order_by('created_on')

        if not application.exists():
            return Response({'error': 'Student is not in the waitlist'}, status=status.HTTP_404_NOT_FOUND)
        # position = list(application).index(application[0]) + 1
        position=1
        for record in application:
            if record.Student==student:
                break
            else:
                position+=1
        return Response({'position': position}, status=status.HTTP_200_OK)

    except JobPost.DoesNotExist:
        return Response({'error': 'JobPost does not exist'}, status=status.HTTP_404_NOT_FOUND)
    except Profile.DoesNotExist:
        return Response({'error': 'Profile does not exist'}, status=status.HTTP_404_NOT_FOUND)
    except JobApplication.DoesNotExist:
        return Response({'error': 'JobApplication does not exist'}, status=status.HTTP_404_NOT_FOUND)


        
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getId(request, username):
    try:
        user = User.objects.get(username=username)
    except user.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
    except Profile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(user.id)

@api_view(['GET'])  
def hire(request,jobpostid):
    if request.method == 'GET':
        jobApplications=JobApplication.objects.filter(jobPost=jobpostid)
        if jobApplications.exists():
            serializer = JobApplicationSerializer(jobApplications, many=True)
            serialized_data = serializer.data
            return Response({'applications': serialized_data}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No applications found for this job post'}, status=status.HTTP_404_NOT_FOUND)
        
