window.onload = function () {
    $('.cart_list').on('click', 'input[type="number"]', function (event) {
        
        $.ajax({
            url: "/cart/edit/" + event.target.name + "/" + event.target.value + "/",
            success: function (data) {
                $('.cart_list').html(data);
            },
        });
    });   
}