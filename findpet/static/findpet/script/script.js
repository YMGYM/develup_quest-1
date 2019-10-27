$(document).ready(function () {
  $("#content div").hover(
    function() {
      $(this).addClass("hover");
    }, function() {
      $(this).removeClass("hover");
    }
  );

  $(".hover").each(function () {
    $(this).qtip({
      content: {
        text: '<img src=" {{ l.thumb }} " />'
      },
      hide: {
        fixed: true,
        delay: 300
      }
    });
  });
});
