# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import generics, status, permissions
#
# from .models import Monografia
# from .serializers import MonografiaSerializers
#
# class MonografiaApi(generics.RetrieveAPIView):
#     queryset = Monografia.objects.all()
#     serializer_class = MonografiaSerializers
#
#     def retrieve(self, request, *args, **kwargs):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = self.get_queryset().filter()
#         serializer = MonografiaSerializers(queryset, many=True)
#         return Response(serializer.data)