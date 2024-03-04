from .models import GlobalConfig

def context_configuration(request):
    config = GlobalConfig.objects.first()  # Obtén la primera instancia (puedes ajustar esto según tus necesidades)
    
    # Define un diccionario con las variables que deseas agregar al contexto
    if config is None:
        return {}

    return {
        'NAME': config.name,
        'LOGO': config.logo.url if config.logo else None,
        'NUMBER': config.number,
        'NAME_DOCUMENTS': config.name_documents,
        'LOGO_DOCUMENTS': config.logo_documents.url if config.logo_documents else None,
        'ADRESS': config.address,
        'PHONE': config.phone,
        'EMAIL': config.email,
        'WEB': config.web,
    }