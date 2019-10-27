$(document).ready(function() {
  $(".hover").each(function () {
    var thumb = $(this).data("thumb");
    var where = $(this).data('where');
    var link = $(this).data("link");
    $(this).qtip({
      content: {
        text: '<a href="'+ link + '"><img src= "' + thumb + '" /><br /><p class="black-text">' + where + '</p></a>'
      },
      hide: {
        fixed: true,
        delay: 300
      }
    });
  });
});

