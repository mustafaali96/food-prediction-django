
def get_side_menus(request):
    if not request.user.is_anonymous:
        return request.user.menus.filter(status=True).order_by("order").values("name", "url")
    return []

def side_menus_context_processor(request):
    """
    Return a lazy 'side_menus' context variable for the allowed 
    """
    return {
        "side_menus": get_side_menus(request),
    }
