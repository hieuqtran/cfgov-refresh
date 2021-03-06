require( '../../on-demand/feedback-form' );
require( '../../on-demand/ask-autocomplete' );
var Analytics = require( '../../../modules/Analytics' );

var analyticsData = document.querySelector( '.analytics-data' );
if ( analyticsData ) {
  var answerID = analyticsData.getAttribute( 'data-answer-id' );
  var categorySlug = analyticsData.getAttribute( 'data-category-slug' );
  var categoryName = analyticsData.getAttribute( 'data-category-name' );

  function sendEvent() {
    var eventData = Analytics.getDataLayerOptions( 
      '/es/obtener-respuestas/c/'+ categorySlug + '/' + answerID + '/',
      document.title, 
      'Virtual Pageview' );
    eventData.category = categoryName;
    Analytics.sendEvent( eventData );
  }
  
  if ( Analytics.tagManagerIsLoaded ) {
    sendEvent();
  } else {
    Analytics.addEventListener( 'gtmLoaded', sendEvent );
  }
  
}