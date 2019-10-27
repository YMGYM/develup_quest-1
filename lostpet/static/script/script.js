$(document).ready(function() {
  $(".hover").each(function () {
    // html로부터 이미지 source를 받아 옵니다.
    var link = $(this).data("thumb");
    var where = $(this).data('where');
    console.log(link)
    $(this).qtip({
      content: {
        text: '<img src= "' + link + '" /><br /><p>' + where + '</p>'
      },
      hide: {
        fixed: true,
        delay: 300
      }
    });
  });
});

