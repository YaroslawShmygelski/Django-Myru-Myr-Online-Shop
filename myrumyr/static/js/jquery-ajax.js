const csrf = document.getElementsByName('csrfmiddlwaretoken');
const form = document.getElementById('form');

$(document).ready(function () {
    $('.modal-form').submit(function (e) {
        e.preventDefault();

        //Parsing id of exact form
        var product_id = $(this).data("form-product-id");
        //Parsing quantity of cart elements
        var goods_in_cart =$('#goods-in-cart-sum');
        var cartCount=0;

        var formData = {};
        // Collecting values for every element
        $(this).find('input, textarea, select').each(function () {
            formData[$(this).attr('name')] = $(this).val();
        });
        var quant = $('#id-quantity');
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: {
                form_data: formData,
                product_id: product_id,
                quantity: formData['quantity'],
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                console.log(formData);
                console.log(product_id);
                console.log(goods_in_cart);

                cartCount+=parseInt(formData['quantity']);
                goods_in_cart.text(cartCount);
            }
        });
    });
});
