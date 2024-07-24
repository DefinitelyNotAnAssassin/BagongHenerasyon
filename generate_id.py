import os
import django
from django.contrib.auth import login, authenticate
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ElectionSystem.settings')
django.setup()

from UserAuthentication.models import Account
# Correct the filter syntax
users = Account.objects.filter(date_joined__date="2024-07-23")

print(users)
options = Options()
options.headless = True  # Run in headless mode
driver = webdriver.Chrome(options=options)



for user in users:

    time.sleep(5)
    
    # Navigate to the /virtual_id page and take a screenshot
    driver.get(f"http://127.0.0.1:8000/user/virtual_id?id={user.id}")
    screenshot_path = f"D:\Projects\BagongHenerasyon\screenshots\\2024-07-23\{user.bh_id}.png"
    driver.save_screenshot(screenshot_path)
    print("Screenshot saved to:", screenshot_path)