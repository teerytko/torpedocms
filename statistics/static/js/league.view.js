(function() {
require(['jquery', 'bootstrap','jquerycookie', 'bootstrap_datetimepicker', 'locale_fi'], 
  function($, bootstrap, cookie) {
    var csrftoken = $.cookie('csrftoken');
    function onDelete(e) {
      event.preventDefault();
      var $row = $( this ).parents('.datarow');
      var rowid = $row.data('id');
      var resurl = GAMESURL+rowid+"/"

      $.ajax({
        type: "DELETE",
        headers: {"X-CSRFToken": csrftoken},
        url: resurl,
        success: function(data)
        {
          $row.remove();
        }
       });
      return false;
    };

    $('.datarow').mouseover(function() {
      $( this ).find( "span" ).css('visibility', 'visible');
    }).mouseout(function() {
      $( this ).find( "span" ).css('visibility', 'hidden');
    });
    $('.datarow span').click(onDelete);

    $('#datepicker').datetimepicker({
                      locale: 'fi',
                      format: 'DD-MM-YYYY HH:mm'
                  });

});
}).call(this);

