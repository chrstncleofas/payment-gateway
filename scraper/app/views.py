import time
from selenium import webdriver
from django.shortcuts import render
from django.http import JsonResponse
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def process_payment(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')
        amount = request.POST.get('amount')

        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:5500/payment.html")

        card_number_field = driver.find_element(By.CSS_SELECTOR, "input#card_number")
        card_number_field.send_keys(card_number)

        expiry_date_field = driver.find_element(By.CSS_SELECTOR, "input#expiry_date")
        expiry_date_field.send_keys(expiry_date)

        cvvField = driver.find_element(By.CSS_SELECTOR, "input#cvv")
        cvvField.send_keys(cvv)

        amount_field = driver.find_element(By.CSS_SELECTOR, "input#amount")
        amount_field.send_keys(amount)

        pay_button = driver.find_element(By.CSS_SELECTOR, "button#pay_button")
        pay_button.click()

        result_message = driver.find_element(By.CSS_SELECTOR, "div#result_message").text
            
        driver.quit()
        print(result_message)

        return JsonResponse(result_message, safe=False)
    else:
        return render(request, 'app/index.html')
