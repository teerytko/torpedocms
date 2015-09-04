(function() {

require(['jquery', 'bootstrap', 'jquerycookie'], 
  function($, bootstrap, cookie) {
    var csrftoken = $.cookie('csrftoken');
    function onSubmit(e) {
      event.preventDefault();
      var name = $('#name').val();
      var data = {'name': name,
                "from_date": null,
                "to_date": null
      };
      $.ajax({
        type: "POST",
        headers: {"X-CSRFToken": csrftoken},
        url: POSTURL,
        data: data,
        success: function(data)
        {
          location.reload();
        }
       });
      return false;
    };
    function onDelete(e) {
      event.preventDefault();
      var rowid = $( this ).parents('.datarow').data('id');
      var resurl = POSTURL+rowid+"/"

      $.ajax({
        type: "DELETE",
        headers: {"X-CSRFToken": csrftoken},
        url: resurl,
        success: function(data)
        {
          location.reload();
        }
       });
      return false;
    };

    $('#newleague').on('submit', onSubmit);
    $('.datarow').mouseover(function() {
      $( this ).find( "span" ).css('visibility', 'visible');
    }).mouseout(function() {
      $( this ).find( "span" ).css('visibility', 'hidden');
    });
    $('.datarow span').click(onDelete);
  });


}).call(this);

