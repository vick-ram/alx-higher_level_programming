$(function() {
  $("#btn_translate, #language_code").on("click keypress", function(event) {
    if (event.type === "keypress" && event.key !== "Enter") {
      return; // Ignore non-Enter keypresses
    }
    const languageCode = $("#language_code").val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;

    $.get(apiUrl, function(data) {
      $("#hello").text(data.hello);
    }).fail(function(jqXHR, textStatus, errorThrown) {
      console.error("Error:", errorThrown);
      $("#hello").text("Error fetching translation.");
    });
  });
});
