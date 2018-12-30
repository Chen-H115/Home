;$(function()
{
  'use strict';


  var sidebar = $('#sidebar'),
      mask = $('.mask'),
      sidebar_trigger = $('#sidebar_trigger'),
      condition = 0;

  window.onload=function(){ $('.loading').hide(); }

  sidebar_trigger.on('click', function()
  {
    if (condition % 2 == 0) {
      mask.fadeIn();
      sidebar.css('right', 0);
      condition = condition + 1;
    }
    else {
      mask.fadeOut();
      sidebar.css('right', -sidebar.width());
      condition = condition + 1;
    }
  })
  mask.on('click', function()
  {
    mask.fadeOut();
    sidebar.css('right', -sidebar.width());
    condition = condition + 1;
  }
  )
})
