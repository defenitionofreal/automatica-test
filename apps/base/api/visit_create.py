# rest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework import status
# core
from apps.base.serializers import VisitSerializer
from apps.base.models import Store


class VisitCreateAPIView(APIView):
    """ Create new visit """

    def post(self, request):
        serializer = VisitSerializer(data=request.data)
        store = get_object_or_404(Store, id=self.request.data.get('store'))
        phone = self.request.query_params.get('phone')

        if serializer.is_valid():
            if phone:
                if phone == store.worker.phone:
                    serializer.save(store=store)
                    return Response(serializer.data,
                                    status=status.HTTP_201_CREATED)
                else:
                    raise ValidationError({"error": "wrong employee's phone."})
            else:
                raise ValidationError({"error": "phone was not provided."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
