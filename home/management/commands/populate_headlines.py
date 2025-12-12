from django.core.management.base import BaseCommand
from home.models import Headline


class Command(BaseCommand):
    help = 'Populate sample headlines for the home page'

    def handle(self, *args, **options):
        # Clear existing headlines (optional - comment out if you want to keep existing)
        # Headline.objects.all().delete()

        headlines_data = [
            {
                'text': 'Top Stories: Power transition underway; Museveni confirms',
                'is_bold': True,
                'order': 1,
                'is_active': True,
            },
            {
                'text': 'Among backs MP\'s proposal for increased oversight',
                'is_bold': False,
                'order': 2,
                'is_active': True,
            },
            {
                'text': 'Parliament approves new budget allocation for education sector',
                'is_bold': False,
                'order': 3,
                'is_active': True,
            },
            {
                'text': 'Breaking: Committee recommends amendments to Anti-Corruption Bill',
                'is_bold': True,
                'order': 4,
                'is_active': True,
            },
            {
                'text': 'MPs debate healthcare reforms in plenary session',
                'is_bold': False,
                'order': 5,
                'is_active': True,
            },
        ]

        created_count = 0
        for headline_data in headlines_data:
            headline, created = Headline.objects.get_or_create(
                text=headline_data['text'],
                defaults={
                    'is_bold': headline_data['is_bold'],
                    'order': headline_data['order'],
                    'is_active': headline_data['is_active'],
                }
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created headline: {headline.text[:50]}...')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Headline already exists: {headline.text[:50]}...')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully processed {len(headlines_data)} headlines. Created {created_count} new headlines.')
        )


