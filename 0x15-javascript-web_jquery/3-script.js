// adds the class red to the <header> element
$(document).ready(function () {
  // Add a click event handler to the div with the id 'red_header'
  $("#red_header").click(function () {
    $("header").addClass("red");
  });
});
