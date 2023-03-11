
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

$('.delete-cust').click(function(){
    var cId = $(this).attr('data-cust-id')
    console.log(cId)
    $.ajax({
        type : 'GET',
        url : "/delete-cust",
        contentType: 'application/json;charset=UTF-8',
        data : {'cId':cId},
        success: function(data,status){
            $('.cust-'+data).remove();
        }
    });
});

$('.book-avail').click(function(){
    var searchId = $('#bookid').val()
    console.log(searchId);
    $.ajax({
        type : 'GET',
        url : "/check-book",
        contentType: 'application/json;charset=UTF-8',
        data : {'bookid':searchId},
        success: function(data,status){
            var datatoshow = JSON.parse(data);
            if(datatoshow === 'Book Not Exist'){
                document.getElementById('showinfo').style.display = 'block';
                document.getElementById('showinfo').innerHTML = 'Book ID Does Not Exist';
            }
            else if(datatoshow.length > 0){
                document.getElementById('showinfo').style.display = 'block';
                document.getElementById('showinfo').innerHTML = 'Book Available';
            }
            else{
                document.getElementById('showinfo').style.display = 'block';
                document.getElementById('showinfo').innerHTML = 'Book Not Available';
            }
        }
    });
});

$('.book-avail-name').click(function(){
    var searchName = $('#bkname').val()
    console.log(searchName);
    $.ajax({
        type : 'GET',
        url : "/check-book-by-name",
        contentType: 'application/json;charset=UTF-8',
        data : {'bkname':searchName},
        success: function(data,status){
            var datatoshow = JSON.parse(data);
            if(datatoshow === 'Book Not Exist'){
                document.getElementById('showinfo').style.display = 'block';
                document.getElementById('showinfo').innerHTML = 'Book Name Does Not Exist';
            }
            else if(datatoshow.length > 0){
                document.getElementById('showinfo').style.display = 'block';
                document.getElementById('showinfo').innerHTML = 'Book Available';
            }
            else{
                document.getElementById('showinfo').style.display = 'block';
                document.getElementById('showinfo').innerHTML = 'Book Not Available';
            }
        }
    });
});

/*
function searchBook(){
    var searchId = $('#bookid').val()
    console.log(searchId);
    $.ajax({
        type : 'GET',
        url : "/check-book",
        contentType: 'application/json;charset=UTF-8',
        data : {'bookid':searchId},
        success: function(data,status){
            var datatoshow = JSON.parse(data);
            if(datatoshow > 0){
                document.getElementById('showinfo').style.display = 'block';
                document.getElementById('showinfo').innerHTML = 'Book Available';
            }
        }
    });
}
*/
