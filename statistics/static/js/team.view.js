(function() {
require(['jquery', 'bootstrap','jquerycookie'], 
  function($, bootstrap, cookie) {
    var csrftoken = $.cookie('csrftoken');
    function onDelete(e) {
      event.preventDefault();
      var $row = $( this ).parents('.datarow');
      var rowid = $row.data('id');
      var resurl = PLAYERSURL+rowid+"/"

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
    $('#number').focus();


});
}).call(this);

