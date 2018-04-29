from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.schemas import SchemaGenerator
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


@api_view()
@permission_classes((permissions.AllowAny,))
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = SchemaGenerator(title='AutoChurn API Docs')
    return Response(generator.get_schema(request=request))


@api_view()
@permission_classes((permissions.AllowAny,))
def elb_health_check(request):

    return Response('All good', status.HTTP_200_OK)

