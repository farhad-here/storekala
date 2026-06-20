from django.shortcuts import render
from stores.models import Product, Category
from django.views.generic import ListView

class HomePageView(ListView):
    model = Product
    template_name = 'home/home.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        queryset = Product.objects.select_related('store', 'category').filter(
            is_active=True,
            store__is_active=True
        )

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(name__icontains=query)

        category_slug = self.request.GET.get('category')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_category'] = self.request.GET.get('category', '')
        context['query'] = self.request.GET.get('q', '')
        return context