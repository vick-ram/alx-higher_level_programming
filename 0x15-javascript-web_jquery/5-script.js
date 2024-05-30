$('document').ready(function() {
	const my_list = $('.my_list');
	const new_list_item = $('<li>Item</li>');;
	$('#add_item').click(function() {
		my_list.append(new_list_item);
	});;
});
