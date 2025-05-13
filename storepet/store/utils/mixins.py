from typing import Any, Dict, List


MENU: List[Dict[str, str]] = [
    {
        "title": "О сайте",
        "url_name": "about"
    },
    {
        "title": "Добавить статью",
        "url_name": "add_page"
    },
    {
        "title": "Обратная связь",
        "url_name": "contact"
    },
    {
        "title": "Войти",
        "url_name": "login"
    }
]


class DataMixin:
    title_page = None
    selected = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context["title"] = self.title_page

        if "menu" not in self.extra_context:
            self.extra_context["menu"] = MENU

        if self.selected is not None:
            self.extra_context["selected"] = self.selected

    def get_mixin_context(self, context: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        context["menu"] = MENU
        context["selected"] = None
        context.update(kwargs)

        return context