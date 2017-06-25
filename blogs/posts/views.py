from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from django.contrib import messages
from django.http import HttpResponse
from posts.models import Post
from posts.forms import PostForm
# Create your views here.
def blogviewcreate(request):
	blogform=PostForm(request.POST or None)
	print request.method
	if request.method=="POST":
		

		if blogform.is_valid():
			blogname=blogform.cleaned_data.get("title")
			blogmatter=blogform.cleaned_data.get("matter")
			print "hey vishwa",blogname
			instance=blogform.save(commit=False)
			instance.save()
	
	return render(request ,"create.html",{})

def blogviewmake(request):
	print "new"
	print request.method
	blogform=PostForm(request.POST or None)
	print "yep"
	create_dict={
	"title":"Create",
	"blogform":blogform
	}
	
	return render(request ,"make.html",create_dict)



def blogviewlist(request):
	q=Post.objects.all()
	#inst=get_object_or_404(Post)
	context={
	"q":q
	}
	return render(request ,"list.html",context)



def blogviewupdate(request, id=None):
	instance = get_object_or_404(Post,id=id)
	#print "old instance is",instance
	updateform=PostForm(request.POST or None,instance=instance)
	if updateform.is_valid():
		instance=updateform.save(commit=False)
		instance.save()
		messages.success(request,"saved!")
		q=Post.objects.all()
		context={
		"q":q
		}
		return render(request ,"list.html",context)
	#print "new instance is",instance
	dicti={
	"title":"Update",
	"updateform":updateform
	}
	return render(request ,"update.html",dicti)


def blogviewdelete(request,id=None):
	instance = get_object_or_404(Post,id=id)
	instance.delete()
	return redirect("list")




	




def blogviewread(request,id):
	instance=Post.objects.get(id=id)
	print instance
	dic={
	"dicid":instance
	}
	return render(request,"new.html",dic)#render(request,"read.html",{})