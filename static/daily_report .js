"use strict";

const incrementDaysOnSite = (daysOnSite) => {
  let daysPreviousOnSite = Number($('#days-on-site-counter').html());
  daysPreviousOnSite += daysOnSite;

  $('#days-on-site-counter').html(daysPreviousOnSite);
};

$('#Add').on('click', () => {
  incrementDaysOnSite($('#daysPreviousOnSite').children().length);
});