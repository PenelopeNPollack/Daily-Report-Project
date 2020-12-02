"use strict";

$('#project_select').on('change', (evt) => {
  const choice = $('#project_select option:selected').val();
  $.get(`/return_count/${choice}`, (results)=>{
    $('#days_on_site').html(results)
  }) 
})

$(document).ready(function() {
  const choice = $('#project_select option:selected').val();
  $.get(`/return_count/${choice}`, (results)=>{
    $('#days_on_site').html(results)
  })
});