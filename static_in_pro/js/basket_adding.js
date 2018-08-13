$(document).ready(function(){
	var form = $('#form_buying_product');
	// console.log(form);

	function basketUpdating(product_id, product_qnt, is_delete) {
		var data = {};
		data.is_delete = is_delete;
		data.product_id = product_id;
		data.product_qnt = product_qnt;
		var csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
		data["csrfmiddlewaretoken"] = csrf_token;

		var url = '/basket_adding/';
		console.log(data);
		console.log(url);
		$.ajax({
		 url: url,
		 type: 'POST',
		 data: data,
		 cache: true,
		 success: function (data) {
			 console.log("OK");
			 console.log(data);
			 // console.log(data.total_product_qnt);
			 if (data.total_product_qnt >= 0){
			 	$('#basket_total_qnt').text('('+data.total_product_qnt+')');
			 	// console.log(data.products);
			 	$('.basket-items ul').html('');
			 	$.each(data.products, function (index, value) {
					$('.basket-items ul').append('<li><a data-fancybox="gallery" href="' + value.image_url +'" class="outline-focus-none"><img class="basket-img" src="' + value.image_url +'"/></a>' + '<p class="basket-p">' + value.name + ', ' + value.nmb + ' шт. по ' + value.price_pre_item + ' грн   '
					  + '<a class="delete-item" href="#" data-product_id="' + value.id + '"><sup title="Видалити">X</sup></a></p>'
					  + '</li>');
                })
			 }
		 },
		 error: function () {
			 console.log('error');
		 }
		});
    };
	form.on('submit', function(e){
		e.preventDefault();
		var product_qnt = $('#product-qnt-input').val();
		// console.log(product_qnt);
		var qnt_submit_btn = $('#qnt-submit-btn');
		var product_id = qnt_submit_btn.data('product_id');
		var product_name = qnt_submit_btn.data('name');
		var product_price = qnt_submit_btn.data('price');
		// console.log(product_id);
		// console.log(product_name);
		// console.log(product_price);

		basketUpdating(product_id, product_qnt, is_delete = false);


		// $('.basket-items ul').append('<li>' + product_name + ', ' + product_qnt + ' шт. по ' + product_price + ' грн   '
		//   + '<a class="delete-item" href="#">x</a>'
		//   + '</li>');
	});

	// function hideShowClass(){
	// 	$('.basket-items').toggleClass('hidden');
	// };



	$('.basket').on('click', function(e){
		e.preventDefault();
		$('.basket-items').slideToggle('slow');
	});	

	// $('.basket-container').mouseover(function(){
	// 	hideShowClass();
	// 	// $('.basket-items').slideDown( "slow" );
	// });

	// $('.basket-container').mouseout(function(){
	// 	hideShowClass();
	// 	// $('.basket-items').slideUp( "slow" );
	// });



	$(document).on('click', '.delete-item', function(e){
		e.preventDefault();
		product_qnt = 0;
		product_id = $(this).data('product_id');
		console.log(product_id);
		basketUpdating(product_id, product_qnt, is_delete = true);
	});
	
	function totalOrderAmounCalculator() {
		var total_order_amount = 0;
		$('.total-product-price-in-basket').each(function () {
			total_order_amount += parseFloat($(this).text());
        });
		$('#total_order_amount').text(total_order_amount.toFixed(2));
    };


	$('input.product-nmb-in-basket').on('input', function (e) {
		var current_product_nmb_in_basket = $(this).val();
		var product_price_pre_item = $(this).closest('tr').find('.product-price-pre-item').text();
		console.log(product_price_pre_item);
		var total_product_price_in_basket = current_product_nmb_in_basket*product_price_pre_item;
		$(this).closest('tr').find('.total-product-price-in-basket').text(total_product_price_in_basket.toFixed(2));
		totalOrderAmounCalculator();
    });

    totalOrderAmounCalculator();
});