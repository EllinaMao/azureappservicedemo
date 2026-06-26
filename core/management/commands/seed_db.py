from django.core.management.base import BaseCommand

from core.product_queries import product_seed, tag_seed, category_seed


class Command(BaseCommand):
    # help = "Create records for Category, Tag"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seedinng")
        try:
            tag_seed()
            category_seed()
            # product_seed()
            self.stdout.write("Succes")

        except Exception as e:
            self.self.stdout.write(self.style.ERROR(f"Error seeding: {e}"))

            