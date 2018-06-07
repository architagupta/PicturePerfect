var CREATE_PAYMENT_URL = 'http://18.220.3.204/payment';
var EXECUTE_PAYMENT_URL = 'http://18.220.3.204/execute';

paypal.Button.render({

    env: 'sandbox', // Or 'sandbox'

    commit: true, // Show a 'Pay Now' button

    payment: function () {
        return paypal.request.post(CREATE_PAYMENT_URL).then(function (data) {
            return data.paymentID;
        });
    },

    onAuthorize: function (data) {
        return paypal.request.post(EXECUTE_PAYMENT_URL, {
            paymentID: data.paymentID,
            payerID: data.payerID
        }).then(function (res) {
            console.log(res.success)
            // The payment is complete!
            $('#premCust').css({ display: "inline-block" });
            $('#paypal_div').css({ display: "none" });
            // You can now show a confirmation message to the customer
        });
    }

}, '#paypal-button');


//$("#paypal-button").click(function () {
//    isPremCust()
//});

//function isPremCust() {
//    $.ajax({
//        type: 'GET',
//        cache: false,
//        url: '/isPremium',
//        success: function (resp) {
//            alert(resp);
//        }
//    });
//}
