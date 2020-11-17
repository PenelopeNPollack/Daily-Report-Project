"use strict";

const incrementDaysOnSite = (daysOnSite) => {
    let daysOnSite = Number($('#days-on-site-counter').html());
    daysOnSite += 1;
  
    $('#days-on-site-counter').html(daysOnSite);
  };

