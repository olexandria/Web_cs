from rest_framework.permissions import AllowAny

from api.models import User
from api.serializers import UserSerializer

from myapi.permissions import IsLoggedInUserOrAdmin, IsAdminUser, IsAutorizateUser 
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Library
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course
from django.shortcuts import render
from .models import Post, Like   
from django.http import HttpResponse
from .models import Book
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import BookForm

def book_create(request):
    form = BookForm()
    context = {'form': form}
    html_form = render_to_string('partial_book_create.html',
        context,
        request=request,
    )
    return JsonResponse({'html_form': html_form})
def index(request):
    posts = Post.objects.all()  # Getting all the posts from database
    return render(request, 'index.html', { 'posts': posts })
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('code', 'title', 'duration', 'fee')
def likePost(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(pk=post_id) #getting the liked posts
        m = Like(post=likedpost) # Creating Like Object
        m.save()  # saving it to store in database
        return HttpResponse("Success!") # Sending an success response	
    else:
        return HttpResponse("Request method is not a GET")
          

def client(request):
    return render(request,"rest_client.html")
def librarys(request):
    return render(request,"librarys.html")
def index(request):
    return render(request,"index.html")
def books(request):
    return render(request,"books.html")


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
@api_view(['GET','POST'])
def list_courses(request):
    if request.method == "GET":
       courses = Course.objects.all()
       serializer = CourseSerializer(courses, many=True)
       return Response(serializer.data)
    else:  # Post
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Successful post

        return Response(serializer.errors, status=400)  #Invalid data



@api_view(['GET','DELETE','PUT'])
def course_details(request, code):
    try:
        course = Course.objects.get(code=code)
    except:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    elif request.method == 'PUT':    # Update
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
           serializer.save()    # Update table in DB
           return Response(serializer.data)

        return Response(serializer.errors, status=400)  # Bad request
    elif request.method == 'DELETE':
        course.delete()
        return Response(status=204)
class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ('code', 'book', 'rating', 'status')




@api_view(['GET','POST'])
def list_librarys(request):
    if request.method == "GET":
       librarys = Library.objects.all()
       serializer = LibrarySerializer(librarys, many=True)
       return Response(serializer.data)
    else:  # Post
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Successful post

        return Response(serializer.errors, status=400)  #Invalid data



@api_view(['GET','DELETE','PUT'])
def library_details(request, code):
    try:
        library = Library.objects.get(code=code)
    except:
        return Response(status=404)

    if request.method == 'GET':
        serializer = LibrarySerializer(library)
        return Response(serializer.data)
    elif request.method == 'PUT':    # Update
        serializer = LibrarySerializer(library, data=request.data)
        if serializer.is_valid():
           serializer.save()    # Update table in DB
           return Response(serializer.data)

        return Response(serializer.errors, status=400)  # Bad request
    elif request.method == 'DELETE':
        library.delete()
        return Response(status=204)




