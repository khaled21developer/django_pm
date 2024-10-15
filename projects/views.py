from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from . import forms


class ProjectListView(ListView):
    model = models.Project
    template_name = 'project/list.html'
    paginate_by = 3

    def get_queryset(self):
        query_set = super().get_queryset()  # استدعاء مجموعة الاستعلام الأساسية
        where = {}
        q = self.request.GET.get('q', None)  # الحصول على قيمة البحث من GET
        if q:
            where['title__icontains'] = q  # استخدم __icontains بدلاً من _icontains
        return query_set.filter(**where)  # تطبيق الفلترة على مجموعة الاستعلام


class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_list')


class ProjectUpdateView(UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'project/update.html'
    success_url = reverse_lazy('Project_list')

    def get_success_url(self):
        return reverse_lazy('Project_update', args=[self.object.id])


class ProjectDeleteView(DeleteView):
    model = models.Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('Project_list')


class TaskCreateView(CreateView):
    model = models.Task
    fields = ['project', 'description']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse_lazy('Project_update', args=[self.object.project.id])


class TaskUpdateView(UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse_lazy('Project_update', args=[self.object.project.id])


class TaskDeleteView(DeleteView):
    model = models.Task

    def get_success_url(self):
        return reverse_lazy('Project_update', args=[self.object.project.id])