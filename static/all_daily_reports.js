"use strict";

$('#daily_reports').on('click', (evt) => {
  const choice = $('#daily_report_select option:selected').val();
  $.get(`/return_report/${choice}`, (results)=>{
    alert(results)  
  }) 
})
