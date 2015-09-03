(function() {
require(['jquery', 'bootstrap','jquerycookie', 'bootstrap_datetimepicker', 'locale_fi'], 
  function($, bootstrap, cookie) {
  console.log("Testing!!!!!!!!!!!!")
  $('#datepicker').datetimepicker({
                    locale: 'fi'
                });

});
}).call(this);

