const csrf = document.getElementsByName('csrfmiddlwaretoken');
const form = document.getElementById('form');

$(document).ready(function () {
    var cart_sum=$('goods-in-cart_sum');
    console.log(cart_sum)
    $('#modal-form').submit(function (e) {
        e.preventDefault();
        var formData = {};
        // Собираем значения каждого поля формы
        $(this).find('input, textarea, select').each(function () {
            formData[$(this).attr('name')] = $(this).val();
        });
        var quant = $('#id-quantity');
        console.log(quant)
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: {
                form_data: formData,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                console.log(formData);
                console.log(data.test1)
            }
        });
    });
});
