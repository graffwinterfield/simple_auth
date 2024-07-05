from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

post_decorator = swagger_auto_schema(
    operation_description="GET запрос для моего представления",
    manual_parameters=[
        openapi.Parameter(
            'user_id',
            openapi.IN_QUERY,
            description="ID пользователя",
            type=openapi.TYPE_STRING
        ),
    ],
    responses={
        200: openapi.Response('Описание ответа'),
        201: openapi.Response('Not auth')
    },
#   security=[{'Bearer': []}]
)


@method_decorator(name="get", decorator=post_decorator)
class Protected(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(instance=request.user)
        return Response(serializer.data)
