//部署页面控制爬虫控件
$('#spider_start').click(function(){
    $.ajax({

        dataType: "json",
        url: "http://127.0.0.1:5000/start",
        data: { id: "id", name: "name" },
        success:function(data){
            alert("SPIDER_START_WORKING");
        },
        error:function(){
            alert("SPIDER_START_ERROR");
        }
    })
});


$('#spider_end').click(function(){
    alert("end");
});




