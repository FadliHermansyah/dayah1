// $(window).scroll(function(){
//     var scroll = $(window).scrollTop();

//     document.getElementById("myBody").style.marginTop = (-100 - 0.5*scroll) + "px";

//     if(scroll >= 100){
//         $("#myNav").removeClass("fixed-top");
//     } else {
//         $("#myNav").addClass("fixed-top")
//     }
// });

$(function (){
    var seedetail = function () {
        // var btn = $(this);
        // $.ajax({
        //   url: btn.attr("data-url"),
        //   type: 'get',
        //   dataType: 'json',
        //   beforeSend: function () {
        //     $("#modal-book .modal-content").html("");
        //     $("#modal-book").modal("show");
        //   },
        //   success: function (data) {
        //     console.log($(btn.attr("data-url")));
        //     $("#modal-book .modal-content").html(data.html_form);
        //   }
        // });
        console.log($("data-url"));
      };
});


// $(".nav-link").on('click', function (){
//     $(".nav-link").removeClass('active');
//     $(this).addClass('active');
// })

// $(".see-details").on('click', function (){
//     $(".modal-body").html(`
//         {% for ringkas in ringkasan %}
//         <div class="container-fluid">
//             <div class="row">
//                 <div class="col-md-2">
//                 <h1>{{ringkas.jumlah_pekerja}}</h1>
//                 </div>
//             </div>
//         </div>
//         {% endfor %}
//     `)
// })