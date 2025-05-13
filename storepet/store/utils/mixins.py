from typing import Any, Dict


class DataMixin:
    paginate_by = 3

    title_page = None
    selected = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context["title"] = self.title_page

        if self.selected is not None:
            self.extra_context["selected"] = self.selected

    @staticmethod
    def get_mixin_context(context: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        context["selected"] = None
        context.update(kwargs)

        return context
