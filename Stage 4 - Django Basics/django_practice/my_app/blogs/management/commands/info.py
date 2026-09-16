from django.core.management.base import BaseCommand

# This is Example cmd Script For Printing info
class Command(BaseCommand):
    help = "Basic commands for info"
    
    def handle(self, *args, **kwargs):
        print("--- Project Info ---")
        print('''Name : Django example app \n Version : 1.0.0 \n Author : Shailesh''')