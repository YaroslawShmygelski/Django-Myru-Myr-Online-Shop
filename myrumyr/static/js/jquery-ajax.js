// Handling of the modal windows for order
const form = document.getElementById('form');
var cartCount = 0;
$(document).ready(function () {
    $('.modal-form').submit(function (e) {
        e.preventDefault();

        //Parsing id of exact form
        var product_id = $(this).data("form-product-id");
        //Parsing quantity of cart elements
        var goods_in_cart = $('#goods-in-cart-sum');

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
                cartCount += parseInt(formData['quantity']);
                goods_in_cart.text(cartCount);
            }
        });
    });


    // Website search function
    $(document).ready(function () {
        $("#search-bar").autocomplete({
            source: '/search-data/',
            open: function () {
                $(".ui-autocomplete").hide();
            },
            response: function (event, ui) {
                $("#drpb").empty();
                $.each(ui.content, function (index, item) {
                    console.log(index);
                    // Adding a div of result and wrap it into a link of the element
                    $("#drpb").append("<a href='" + item.url + "' style=\"text-decoration: none !important; " +
                        "color: inherit !important; " +
                        "cursor: pointer !important;\"> " +
                        "<div class='dropdown-result'>" + item.name + "</div></a>");
                });

                if (ui.content.length > 0) {
                    $("#drpb").show();
                } else {
                    $("#drpb").hide();
                }
            }
        });

        // Handling of the element click
        $('#drpb').on('click', '.dropdown-result', function () {
            $('#search-bar').val($(this).text());
            $("#drpb").empty(); // Clear list after click
            $("#drpb").hide();
        });

        // Hide list if click out of the dropdown-box
        $(document).on('click', function (event) {
            if (!$(event.target).closest('#search-bar, #drpb').length) {
                $("#drpb").empty();
                $("#drpb").hide();
            }
        });
    });


});