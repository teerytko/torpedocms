(function() {
require(['jquery', 'bootstrap','jquerycookie', 'tablesorter', 'tablesorter_pager'], 
  function($, bootstrap, cookie) {

    psorter = $('#playerstats').tablesorter({sortList: [[5,1], [3,1], [4,1]]});
    $.tablesorterPager.defaults.positionFixed = false;
    psorter.tablesorterPager({container: $("#pager")});
    
    $('#teamstats').tablesorter({sortList: [[5,1], [2,1], [8,1]]});
});
}).call(this);

