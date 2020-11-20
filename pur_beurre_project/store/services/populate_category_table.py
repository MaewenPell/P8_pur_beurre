from store.models import Category


class NewCategory():
    def __init__(self, category: str):
        self.category = str(category)

    def create_new_category(self):
        category = Category.objects.create(category=self.category)

        return category
