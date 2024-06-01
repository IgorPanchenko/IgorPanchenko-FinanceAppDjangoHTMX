import random
from faker import Faker
from django.core.management.base import BaseCommand
from tracker.models import User, Transaction, Category


class Command(BaseCommand):
    help = "Generates transaction for testing"

    def handle(self, *args, **kwargs):
        fake = Faker()

        categories = [
            "Чеки",
            "Кафе",
            "Одежда",
            "Товары для дома",
            "Зарплата",
            "Социальные услуги",
            "Транспорт",
            "Отдых",
        ]

        for category in categories:
            Category.objects.get_or_create(name=category)

        user = User.objects.filter(username='admin').first()
        if not user:
            user = User.objects.creae_superuser(username='admin', password='adminadmin')

        categories = Category.objects.all()
        types = [x[0] for x in Transaction.TRANSACTION_TYPE_CHOICES]
        for i in range(20):
            Transaction.objects.create(
                category=random.choice(categories),
                user=user,
                amount=random.uniform(1, 1000),
                date=fake.date_between(start_date='-1y', end_date='today'),
                type=random.choice(types)
            )
