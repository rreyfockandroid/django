from django.conf.urls import patterns, include, url

urlpatterns = patterns('myapp.views', 
	url(r'^hello/', 'hello', name = 'hello'),
	url(r'^hello_x/', 'helloX', name = 'helloX'),
	url(r'^morning/', 'morning', name = 'morning'),
	# http://127.0.0.1:8000/myapp/article/123/
	url(r'^article/(\d+)/', 'viewArticle', name = 'article'),
	# http://127.0.0.1:8000/myapp/articles/03/2003/
	url(r'^articles/(\d{2})/(\d{4})', 'viewArticles', name = 'articles'),
)
