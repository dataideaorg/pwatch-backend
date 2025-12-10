from django.db import models


class Bill(models.Model):
    BILL_TYPE_CHOICES = [
        ('government', 'Government'),
        ('private_member', 'Private Member'),
    ]

    BILL_STATUS_CHOICES = [
        ('1st_reading', '1st Reading'),
        ('2nd_reading', '2nd Reading'),
        ('3rd_reading', '3rd Reading'),
        ('passed', 'Passed by Parliament'),
        ('assented', 'Assented to by the President'),
    ]

    title = models.CharField(max_length=500)
    bill_type = models.CharField(max_length=50, choices=BILL_TYPE_CHOICES)
    year_introduced = models.DateField()
    mover = models.CharField(max_length=200)
    assigned_to = models.CharField(max_length=200, help_text="Committee assigned to")
    status = models.CharField(max_length=50, choices=BILL_STATUS_CHOICES, default='1st_reading')
    description = models.TextField(blank=True)
    video_url = models.URLField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Bill'
        verbose_name_plural = 'Bills'

    def __str__(self):
        return self.title


class BillReading(models.Model):
    READING_STAGE_CHOICES = [
        ('1st_reading', '1st Reading'),
        ('2nd_reading', '2nd Reading'),
        ('3rd_reading', '3rd Reading'),
    ]

    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='readings')
    stage = models.CharField(max_length=50, choices=READING_STAGE_CHOICES)
    date = models.DateField()
    details = models.TextField()
    document = models.FileField(upload_to='bill_documents/', blank=True, null=True)
    committee_report = models.FileField(upload_to='committee_reports/', blank=True, null=True)
    analysis = models.FileField(upload_to='bill_analysis/', blank=True, null=True)
    mp_photo = models.ImageField(upload_to='mp_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date']
        verbose_name = 'Bill Reading'
        verbose_name_plural = 'Bill Readings'
        unique_together = ['bill', 'stage']

    def __str__(self):
        return f"{self.bill.title} - {self.get_stage_display()}"