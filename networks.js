$(document).ready(function() {
	$('#get-data').click(function() {
		var showData = $('#show-data');

		$.getJSON('data/data-network.json', function(data) {
			console.log(data);

			var items = data.items.map(function(item) {
				// return item.key + ': ' + item.value;
				return "<option value='" + item.key + "'>" + item.value + "</option>";
			});

			showData.empty();

			if (items.length) {
				var content = items.join('');
				var list = $('<select multiple class="form-control" id="networks-list" >').html(content);
				showData.append(list);
			}
		});

		showData.text('Loading the JSON file.');
	});
	$("#show-data").change(function() {
		var x = document.getElementById("networks-list").selectedIndex;
		var r = document.getElementsByTagName("option")[x].value;
		document.getElementById("network-selected").innerHTML = r;
	});
});
