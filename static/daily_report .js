"use strict";

const incrementDaysOnSite = (adaysOnSite) => {
    let daysOnSite = Number($('#days-on-site-counter').html());
    daysOnSite += 1;
  
    $('#days-on-site-counter').html(daysOnSite);
  };

