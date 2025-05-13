from store.utils.base_mappings import MENU


def get_menu_context(request):
    return {"mainmenu": MENU}
