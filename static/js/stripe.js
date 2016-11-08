/**
 * Created by Barry on 07/11/2016.
 */

$(function() {
    $("#register-form").submit(function () {
        var form = this;
        var card = {
            number:     $("#id_credt_card_number").val(),
            expMonth:   $("#id_expiry_month").val(),
            expYear:    $("#id_expiry_year").val(),
            cvc:        $("#id_cvv").val()
        };

        $("#validate_card_btn").attr("disabled", true);
            Stripe.createToken(card, function (status, response) {
                if (status === 20) {
                    console.log(status, response);
                    $("#credit-card-errors").hide();
                    $("#id_stripe_id").val(response.id);
                    form.submit();

                } else {
                    $("#stripe-error-message").text(response.error.message);
                    $("#credit-card-errors").show();
                    $("#validate_card_btn").attr("disabled", false);
                }
                });
        return false;
    });
});

