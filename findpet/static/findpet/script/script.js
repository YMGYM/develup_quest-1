$(document).ready(function () {
  $("#{{ pet.id }}").each(function () {
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
