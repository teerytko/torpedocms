(function() {

require(['jquery', 'bootstrap', 'jquerycookie'], 
  function($, bootstrap, cookie) {
  	function submit(e) {
			event.preventDefault();
			var name = $('#name').val();
			var csrftoken = $.cookie('csrftoken');
		  console.log( "Saving "+$('#name').val() );
			console.log(POSTURL);

		  $.ajax({
	      type: "POST",
	      headers: {"X-CSRFToken": csrftoken},
	      url: POSTURL,
	      data: {'name': name, 
	      			  "from_date": null,
								"to_date": null
								},
	      success: function(data)
	      {
	      	console.log("Saved ok");

	      }
	     });
			return false;
		};

  	$('#newleague').on('submit', submit);
  	$('.datarow').mouseover(function() {
  		$( this ).find( "span" ).show();
  	}).mouseout(function() {
  		$( this ).find( "span" ).hide();
  	});
	});


}).call(this);

