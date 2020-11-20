from store.models import Aliment, Category


class NewAliment():
    def __init__(self, alim, category: Category):
        self.category = category
        self.name = alim['name']
        self.nutriscore = alim['nutriscore']
        self.image_url = alim['image_url']
        self.sugar = alim['sugars']
        self.product_url = alim['url']
        self.fat = alim['fat']
        self.salt = alim['salt']
        self.energy = alim['energy']

    def create_aliment(self):
        Aliment.objects.create(category=self.category, name=self.name,
                               nutriscore=self.nutriscore,
                               image_url=self.image_url,
                               product_url=self.product_url,
                               sugar=self.sugar,
                               fat=self.fat,
                               salt=self.salt,
                               energy=self.energy)
