#coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db import connection,transaction
from mainsites.blogs.models import Blog

def bloglist(request):
    cursor=connection.cursor()
    sql='select blogtitle,blogcontent from blogs_blog'
    cursor.execute(sql)
    blogs=cursor.fetchall()
    cursor.close()
    
    bloglist=[]
    for i in range(0,len(blogs)):
        blog={}
        blog['blogtitle']=blogs[i][0]
        blog['blogcontent']=blogs[i][1]
        bloglist.append(blog)

    return render_to_response('blog/bloglist.html',{'bloglist':bloglist,'blogtitle':bloglist[0],})

def blog_add(request):
    blog=Blog(blogtitle=u'测试标题',author=u'张俊克',blogcontent=u'测试内容',blogdesc=u'测试备注',creartor='coderwood')
    blog.save()
    blog_list=Blog.objects.all()
    return render_to_response('blog/bloglist.html',{'bloglist',bloglist})
