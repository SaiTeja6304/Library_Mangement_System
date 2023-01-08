
$('.delete-book').click(function(){
    var bId = $(this).attr('data-dattr-id')
    console.log(bId)
    $.ajax({
        type : 'GET',
        url : "/delete-book",
        contentType: 'application/json;charset=UTF-8',
        data : {'bId':bId},
        success: function(data,status){
            $('.book-'+data).remove();
        }
    });
});