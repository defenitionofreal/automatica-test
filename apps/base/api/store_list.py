# rest
from rest_framework.views import APIView
from rest_framework.response import Response
# core
from apps.base.models import Store
from apps.base.serializers import StoreSerializer


class StoreListAPIView(APIView):
    """ Stores by phones """

    def get(self, request):
        query = Store.objects.filter(
            worker__phone=self.request.query_params.get('phone'))
        serializer = StoreSerializer(query, many=True)
        return Response(serializer.data)
