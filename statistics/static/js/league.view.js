(function() {
require(['jquery', 'bootstrap','jquerycookie', 'bootstrap_datetimepicker', 'locale_fi'], 
  function($, bootstrap, cookie) {
  console.log("Testing!!!!!!!!!!!!")
  $('#datepicker').datetimepicker({
                    locale: 'fi',
                    format: 'DD-MM-YYYY HH:mm'
                });

});
}).call(this);

