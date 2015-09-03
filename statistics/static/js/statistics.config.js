(function() {
  requirejs.config({
    baseUrl: STATIC_URL,
    paths: {
      'jquery': 'bower/jquery/dist/jquery',
      'jquerycookie': 'bower/jquery-cookie/jquery.cookie',
      'bootstrap': 'bower/bootstrap/dist/js/bootstrap',
      'moment':  'bower/moment/min/moment.min',
      'bootstrap_datetimepicker':  'bower/eonasdan-bootstrap-datetimepicker/build/js/bootstrap-datetimepicker.min',
      'locale_fi': 'bower/moment/locale/fi',
    },
    shim: {
      jutils: {
          deps: ['jquery']
      },
      jeditable: {
          deps: ['jquery']
      },
      bootstrap: {
          deps: ['jquery']
      },
      bootstrap_datetimepicker: {
          deps: ['moment', 'jquery', 'bootstrap']
      },
    }
  });
}).call(this);
