from django.conf.urls.defaults import *
from entries.models import *

num_entries_per_page = 100

urlpatterns = patterns('',
	url(r'^$',
		'django.views.generic.list_detail.object_list',
		{'paginate_by': num_entries_per_page,
			'queryset': Entry.objects.all().order_by('-publication_date')},
		name='entry_list'),
	url(r'^(?P<object_id>\d+)/$',
		'django.views.generic.list_detail.object_detail',
		{'queryset': Entry.objects.all().order_by('-publication_date')},
		name='entry_detail'),
	url(r'^create$',
		'django.views.generic.create_update.create_object',
		{'model': Entry},
		name='entry_create'),
	url(r'^delete/(?P<object_id>\d+)/$',
		'django.views.generic.create_update.delete_object',
		# FIXME: festgeschriebener Pfade sollte nicht sein -> URL-Name
		{'model': Entry, 'post_delete_redirect': '../..'},
		name='entry_delete'),
	url(r'^update/(?P<object_id>\d+)/$',
		'django.views.generic.create_update.update_object',
		{'model': Entry},
		name='entry_update'),
)
