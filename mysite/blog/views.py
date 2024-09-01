from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PostForm
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', { 'posts': posts })



def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # post = form.save(commit=False)
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', { 'form': form })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', { 'post': post })

# def register_view(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful.")
#             return redirect("blog")
#     else:
#         form = UserRegisterForm()
#     return render(request, "blog/register.html", {"form": form})
#
# def login_view(request):
#     if request.method == "POST":
#         form = UserLoginForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "Login successful.")
#                 return redirect("blog")  # Замените на URL главной страницы блога
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     else:
#         form = UserLoginForm()
#     return render(request, "blog/login.html", {"form": form})
#
# @login_required
# def logout_view(request):
#     logout(request)
#     messages.success(request, "You have been logged out.")
#     return redirect("blog")  # Замените на URL главной страницы блога

