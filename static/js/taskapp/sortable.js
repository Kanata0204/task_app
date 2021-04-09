console.log('OK');

$(function() {

    let csrf = $("input[name=csrfmiddlewaretoken]").val();
    console.log(csrf);

    $('.sortable').sortable({
        update: function(event, ui){
        //   let information = $('.sortable').sortable('serialize');
          // console.log($(this))
        //   console.log(information);

        sort =[];
        // console.log($(this).children());
        $(".sortable").children().each(function(){
        sort.push(
            {
                'pk':$(this).data('pk'),
                'order':$(this).index()
              }
            )
        });

        console.log(sort);
        // ここまで順調

        $.ajax({
            url: "",
            type: 'post',
            data: {
                text: JSON.stringify(sort),
                csrfmiddlewaretoken: csrf,
            }
        });
        }
    }).disableSelection();
    // #listに「ui-sortable」を追加
    // 子要素のドラッグ対象に「ui-sortable-placeholder」を追加
    // ドラッグ対象のもともとの位置に「ui-sortable-helper」という要素が挿入される
});