from django.core.management.base import BaseCommand
from django.utils import timezone
from news.models import News


class Command(BaseCommand):
    help = 'Populate sample news articles for the home page'

    def handle(self, *args, **options):
        news_data = [
            {
                'title': 'MPs Doubt Impact of State Funds Model Ministerial Poverty',
                'author': 'Parliament Watch Team',
                'category': 'latest_blogs',
                'excerpt': 'Members of Parliament have raised concerns about the effectiveness of the current state funds model in addressing ministerial poverty and its impact on service delivery.',
                'content': '''Members of Parliament have raised serious concerns about the effectiveness of the current state funds model in addressing ministerial poverty and its impact on service delivery across various government departments.

During a recent parliamentary session, several MPs questioned whether the existing funding mechanisms are sufficient to address the growing challenges faced by ministries. The debate centered on whether the current model adequately supports ministerial operations and ensures efficient resource allocation.

Key concerns raised include:
- Insufficient funding for critical ministerial functions
- Delayed disbursement of allocated funds
- Lack of transparency in fund utilization
- Impact on service delivery to citizens

The discussion highlighted the need for a comprehensive review of the state funds model to ensure better accountability and improved service delivery across all government ministries.''',
                'status': 'published',
            },
            {
                'title': 'Parliament Approves New Budget Allocation for Education Sector',
                'author': 'Parliament Watch Team',
                'category': 'parliament',
                'excerpt': 'In a landmark decision, Parliament has approved a significant increase in budget allocation for the education sector, with a focus on improving infrastructure and teacher welfare.',
                'content': '''In a landmark decision, Parliament has approved a significant increase in budget allocation for the education sector, with a focus on improving infrastructure and teacher welfare.

The budget allocation, which represents a 15% increase from the previous financial year, will be directed towards:
- Construction and renovation of school facilities
- Teacher recruitment and training programs
- Provision of learning materials and resources
- Scholarship programs for underprivileged students

The approval came after extensive debate in both the Committee on Education and the full House, with MPs emphasizing the critical role of education in national development. The Minister of Education welcomed the decision, stating that it will significantly improve the quality of education delivery across the country.

Stakeholders in the education sector have expressed optimism about the increased funding, noting that it addresses long-standing challenges in the sector.''',
                'status': 'published',
            },
            {
                'title': 'Committee Recommends Amendments to Anti-Corruption Bill',
                'author': 'Parliament Watch Team',
                'category': 'governance',
                'excerpt': 'The Parliamentary Committee on Legal and Parliamentary Affairs has recommended several key amendments to the Anti-Corruption Bill to strengthen accountability mechanisms.',
                'content': '''The Parliamentary Committee on Legal and Parliamentary Affairs has recommended several key amendments to the Anti-Corruption Bill to strengthen accountability mechanisms and enhance the fight against corruption.

After extensive public consultations and stakeholder engagement, the committee identified areas that require strengthening in the proposed legislation. The recommended amendments include:

- Enhanced penalties for corruption offenses
- Strengthened whistleblower protection mechanisms
- Improved asset recovery procedures
- Clearer definitions of corruption-related offenses
- Enhanced powers for anti-corruption agencies

The committee's report, which was tabled before Parliament, has been welcomed by civil society organizations and anti-corruption advocates. The recommendations are expected to be debated in the next parliamentary session, with MPs expected to provide their input on the proposed changes.

The amendments are seen as crucial in strengthening the legal framework for combating corruption and promoting good governance in the country.''',
                'status': 'published',
            },
        ]

        created_count = 0
        for article_data in news_data:
            # Check if article with same title exists
            article, created = News.objects.get_or_create(
                title=article_data['title'],
                defaults={
                    'author': article_data['author'],
                    'category': article_data['category'],
                    'excerpt': article_data['excerpt'],
                    'content': article_data['content'],
                    'status': article_data['status'],
                    'published_date': timezone.now().date(),
                }
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created news article: {article.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'News article already exists: {article.title}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully processed {len(news_data)} news articles. Created {created_count} new articles.')
        )


