(function() {

require(['jquery', 'bootstrap', 'jquerycookie', 'bootstrap_datetimepicker', 'locale_fi'], 
  function($, bootstrap, cookie) {
    var csrftoken = $.cookie('csrftoken');
    function selectTeam(team) {      
      $select = $('.playerselect');
      $players = $('#'+team+'players');
      $select.empty()
      $select.append($players.children().clone());
    }

    function onTeamChange() {
      event.preventDefault();
      var team = $(this).val();
      selectTeam(team);
      return false;
    };
    function onDeleteEvent(e) {
      event.preventDefault();
      var rowid = $( this ).data('id');
      var type = $( this ).data('type');
      var eventrow = $( this ).parents('blockquote')
      var resurl = '';
      if (type == 'goal')
        resurl = GOALURL+rowid+"/"
      else
        resurl = PENALTYURL+rowid+"/"


      $.ajax({
        type: "DELETE",
        headers: {"X-CSRFToken": csrftoken},
        url: resurl,
        success: function(data)
        {
          eventrow.remove();
        }
       });
      return false;
    };

    $('blockquote').mouseover(function() {
      $( this ).find( "span" ).css('visibility', 'visible');
    }).mouseout(function() {
      $( this ).find( "span" ).css('visibility', 'hidden');
    });
    $('.removeevent').click(onDeleteEvent);
    $('.teamselect').change(onTeamChange);
    $('.timepicker').datetimepicker({
                      locale: 'fi',
                      format: 'mm:ss'
                  });
    selectTeam('home');

  });


}).call(this);

