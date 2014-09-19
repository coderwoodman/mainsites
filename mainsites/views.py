#coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db import connection,transaction
from mainsites.blogs.models import Blog
import HTMLParser 

def index(request):
    html_parser = HTMLParser.HTMLParser()
    cursor=connection.cursor()
    sql='select id,blogtitle,author,blogcontent,lastchagetime from blogs_blog'
    cursor.execute(sql)
    blogs=cursor.fetchall()
    cursor.close()
    
    bloglist=[]
    for i in range(0,len(blogs)):
        blog={}
        blog['id']=blogs[i][0]
        blog['blogtitle']=blogs[i][1]
        blog['author'] = blogs[i][2]
        blog['blogcontent'] = html_parser.unescape(blogs[i][3])
        blog['lastchangetime'] = blogs[i][4]
        bloglist.append(blog)

    return render_to_response('index.html',{'bloglist':bloglist,})

def about(request):
    return render_to_response(})

def tool(request):
    return render_to_response('tool.html',{})
