from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView

from .models import Thread


# class ForumView(View):

#     # template_name = 'forum/forumIndex.html'
#     def get(self, request, *args, **kwargs):
#         return render(request, 'forum/forumIndex.html')


# class ForumView(TemplateView):

#     template_name = 'forum/forumIndex.html'

class ForumView(ListView):

    paginate_by = 2
    template_name = 'forumIndex.html'

    def get_queryset(self):
        queryset = Thread.objects.all()
        order = self.request.GET.get('order', '')
        if order == 'views':
            queryset = queryset.order_by('-views')
        elif order == 'answers':
            queryset = queryset.order_by('-answers')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        context['tags'] = Thread.tags.all()
        return context


forumIndex = ForumView.as_view()
