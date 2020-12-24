import logging

from django.utils.translation import ugettext_lazy as _
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

logger = logging.getLogger(__name__)


class StatusView(GenericAPIView):

    def get(request, format=None):
        return Response({
            "type": "success",
            "message": _("I'm healthy.")
        }, content_type='application/json')
