(function() {
require(['jquery', 'bootstrap','jquerycookie', 'tablesorter'], 
  function($, bootstrap, cookie) {

    $('#playerstats').tablesorter({sortList: [[5,1], [3,1], [4,1]]});
    $('#teamstats').tablesorter({sortList: [[5,1], [2,1], [8,1]]});
});
}).call(this);

