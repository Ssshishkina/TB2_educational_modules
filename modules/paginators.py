from rest_framework.pagination import PageNumberPagination


class ModulePaginator(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'


class LessonPaginator(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
