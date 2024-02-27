from django.utils.deprecation import MiddlewareMixin

class CaptureIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Obtener la dirección IP del usuario desde la solicitud
        ip_address = request.META.get('REMOTE_ADDR')
        if not ip_address:
            ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0].strip() or request.META.get('REMOTE_ADDR')

        # Almacenar la dirección IP en el objeto de solicitud para que esté disponible en las vistas
        request.ip_address = ip_address
        
        # Almacenar la dirección IP en el objeto de solicitud para que esté disponible en las vistas
        request.ip_address = ip_address

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Si el usuario está autenticado, actualizar la dirección IP en el modelo User
        user = request.user
        if user.is_authenticated and hasattr(request, 'ip_address'):
            user.ip = request.ip_address
            user.save()