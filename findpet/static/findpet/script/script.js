$(document).ready(function () {
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
