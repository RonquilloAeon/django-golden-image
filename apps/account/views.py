from apps.account import tasks as account_tasks
from apps.common.views import get_default_response
from rest_framework import permissions
from rest_framework.views import APIView


class SampleTasksViewSet(APIView):
    """
    Class for api/sample_tasks
    """
    permission_classes = (permissions.AllowAny, )

    @staticmethod
    def get(request, **kwargs):
        """
        Not implemented
        :param request: request object
        :param kwargs: additional parameters
        :return: Response object
        """
        # NOT IMPLEMENTED, return 501!
        return get_default_response('501')

    @staticmethod
    def post(request):
        """
        POST /api/sample_tasks to create a sample Celery task.
        Use Flower to view result
        :param request: HTTP request object
        :return: Response object
        """
        payload = request.data
        value = payload.get('value', None)
        response = get_default_response('400')

        if value:
            # Pass value to task queue
            account_tasks.test_task.apply_async(args=[value], )

            # Prepare response
            response = get_default_response('201')
            response['message'] = 'Task has been accepted and is being processed.'
            response['userMessage'] = 'Your task is currently being processed.'

        return response
