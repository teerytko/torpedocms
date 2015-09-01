(function() {
  requirejs.config({
    baseUrl: STATIC_URL,
    paths: {
      'jquery': 'bower/jquery/dist/jquery',
      'bootstrap': 'bower/bootstrap/dist/js/bootstrap',
      'jeditable':  'vendor/jquery.jeditable',
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
    }
  });
}).call(this);
