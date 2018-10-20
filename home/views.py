from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from home.forms import HomeForm, CommentForm
from home.models import Post, Friend, Comment


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
        friend, created = Friend.objects.get_or_create(current_user=request.user)
        friends = friend.users.all()

        args = {'form': form, 'posts': posts, 'users': users, 'friends': friends}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('home:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('home:home')


'''def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('home:home')

    else:
        form = CommentForm()
        comment = Comment.objects.all().order_by('-created')
        args = {'form': form, 'comment': comment}

    return render(request, 'home/add_comment_to_post.html', args)'''


class AddCommentToPost(TemplateView):
    template_name = 'home/add_comment_to_post.html'

    def get(self, request, pk):
        form = CommentForm()
        comment = Comment.objects.all().order_by('-created')
        args = {'form': form, 'comment': comment}

        return render(request, self.template_name, args)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.user = request.user
                comment.save()
                post = Post.objects.get(id=pk)
                post.comments.add(comment)
                post.save()
                return redirect('home:home')

        args = {'form': form}
        return render(request, self.template_name, args)
