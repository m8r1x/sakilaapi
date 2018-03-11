from rest_framework.pagination import PageNumberPagination

class StandardResultSetPagination(PageNumberPagination):
  page_size = 30
  page_size_query_param = 'per_page'
  max_page_size = 30
