from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .form import PostForm

# Create your views here.

def index(request) : 
    posts = Post.objects.all().order_by('-id')
    return render(request, 'index.html', {'posts_show':posts })

def detail(request, post_id) : 
    post_detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'detail.html', {'post':post_detail})

def new(request) :
    return render(request, 'new.html')

def create(request) : 
    post = Post()
    post.title = request.GET['title']
    post.content = request.GET['content']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('/post/'+str(post.id))

def modify(request, post_id) : 
    post_detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'modify.html', {'post':post_detail})

def newmodify(request, post_id) :
    post_instance = get_object_or_404(Post, pk = post_id)
    
    if request.method == 'POST' : # update
        form = PostForm(request.POST) # form 인스턴스 생성하고 요청에 의한 데이터로 채움
        if form.is_valid() : # 폼이 유효한지 체크
            # 유효통과하면 form의 필드가 cleaned_data로 dict형으로 정제 
            post_instance.title = form.cleaned_data['title']
            post_instance.content = form.cleaned_data['content']
            post_instance.pub_date = timezone.now()
            post_instance.save()
        
        return redirect('detail', post_id) # 수정한 post_id를 넘겨 
    else : # modify를 위해 post_id를 이용해 정보 가져오 렌더링
        form = PostForm(initial={'title':post_instance.title, 'content':post_instance.content}) # form 의 value 초기값을 설정해주어 bound된 form생성
        return render(request, 'newmodify.html', {'form':form})

        
        
        

def update(request, post_id) :
    post = get_object_or_404(Post, pk = post_id)
    post.title = request.GET['title']
    post.content = request.GET['content']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('/post/'+str(post.id))

def delete(request, post_id) :
    post = get_object_or_404(Post, pk = post_id)
    post.delete()
    return redirect('/') 

def newpost(request) : 
    if request.method == 'POST' :
        form = PostForm(request.POST) # form 인스턴스 생성하고 요청에 의한 데이터로 채운다(binding)
        if form.is_valid() : # 이 form이 유효한지 확인해 주는 코드
            post = form.save(commit = False) # 저장하기 않고 객체를 가져옴
            post.pub_date = timezone.now()
            post.save()
            return redirect('index')
    
    else: # GET 일경우
        form = PostForm() # unbound된 form
        print(form)
        return render(request, 'new.html', {'form':form})