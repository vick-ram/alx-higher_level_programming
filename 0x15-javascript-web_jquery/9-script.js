$(function() {
  $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
    $("#hello").text(data.hello); 
  }, function(jqXHR, textStatus, errorThrown) {
    console.error("Error:", errorThrown); 
    $("#hello").text("Error fetching data."); 
  });
});
