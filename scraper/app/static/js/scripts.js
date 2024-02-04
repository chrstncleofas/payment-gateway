function processPayment() {
    var cardNumber = document.getElementById('card_number').value;
    var expiryDate = document.getElementById('expiry_date').value;
    var cvv = document.getElementById('cvv').value;
    var amount = document.getElementById('amount').value;
    var xhr = new XMLHttpRequest();
    var url = '/process_payment/';
    var params = 'card_number=' + cardNumber + '&expiry_date=' + expiryDate + '&cvv=' + cvv + '&amount=' + amount;
    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var response = JSON.parse(xhr.responseText);
            var resultMessageElement = document.getElementById('result_message');
            resultMessageElement.textContent = response.result_message;

            $('#paymentModal').modal('show');
            if (response.success) {
                document.getElementById('payment-form').classList.add('d-none');
            }
        }
    }
    xhr.send(params);
}
