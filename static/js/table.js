//table.js
    //获取发布模块类型
    function getModuleInfo() {
      $.ajax({
        type: "GET",
        dataType: "json",
        url: "/data",
        //data: { id: id, name: name },
        success: function(json) {
          
          // alert("ok!!")

          

          //清洗
          for(var i=0;i<json.length;i++){
            delete json[i]['is_new'];
            delete json[i]['is_hot'];
            delete json[i]['star_word'];
            delete json[i]['note']//note
            delete json[i]['realpos'];
            delete json[i]['flag'];
            delete json[i]['raw_hot'];
            delete json[i]['emoticon'];
            delete json[i]['subject_label'];
            delete json[i]['icon_desc_color'];
            delete json[i]['flag_desc'];
            delete json[i]['mid'];
            // delete json[i]['subject_querys'];
            delete json[i]['ad_info'];
            delete json[i]['topic_flag'];
            delete json[i]['fun_word'];
            delete json[i]['icon_desc'];
            delete json[i]['onboard_time'];
            delete json[i]['channel_type'];
            //add delete content 2023-3-24
            delete json[i]['is_fei'];
            delete json[i]['expand'];
            delete json[i]['small_icon_desc'];
            delete json[i]['small_icon_desc_color'];
            delete json[i]['word_scheme'];
            delete json[i]['star_name'];




            
          }


         







          

          //*******************填充*表头*************//
           //存key，存中文的
           var keyArray = new Array();
                    for(var key in json[0]){
                      if(key == "label_name")key="标签";
                      if(key == "category")key="类别";
                      if(key == "num")key="热度值/搜索量";
                      if(key == "word")key="话题";
                      if(key == "rank")key="排名";
                      if(key == "subject_querys")key="出处";
                      keyArray.push(key);
                      
                    }

          //part1
          tbHead = ""
          tbHead += "<thead ><tr> <th scope='col'>#</th>";
            
          //part2
          for(var key in keyArray){
              // keyArray.push(key);
              tbHead+="<th scope='col'>"+keyArray[key]+"</th> ";
          }
          //part3
          tbHead += " </tr></thead>";
          //删除旧的，填充新的
          $("#myTb").empty();
          $("#myTb").append(tbHead);
          









          //*******************填充*表体*************//
          //存value

          //part1
          tbBody = ""
          tbBody+="<tbody>";


          //part2

          for(var i=0;i<json.length;i++){
              // drop ads
              if(json[i].hasOwnProperty("ad_channel")){

                continue;
              }
          tbBody+="<tr><th scope='row'>"+(i+1)+"</th>";
            
            for(var key in json[i]){
              //CheckPoint
              // console.log(key+':'+json[i][key]);

              if(key=='word'){
                
                tbBody+="<td><a style='color:black;text-decoration:none;' href='https://s.weibo.com/weibo?q=" + json[i][key] + "'>"+json[i][key]+"</a></td>";
              }else if(key=='label_name'&&json[i][key]!=''){
                if(json[i][key]=='沸')tbBody+="<td class='hot'>"+json[i][key]+"</td>";
                else if(json[i][key]=='新')tbBody+="<td class='new'>"+json[i][key]+"</td>";
                
              }else{
                tbBody+="<td>"+json[i][key]+"</td>";
              }

            }
            if  (i+1<json.length && json[i]['rank']==json[i+1]['rank'])i++;//下一条是广告
            tbBody+="</tr>";
          }
            
         //part3
         tbBody+="</td></tbody>";
         $("#myTb").append(tbBody);


     
        },
        error: function() {
          alert("加载失败");
        }
      });
      var mydate=new Date();
      console.log("hotRank最近一次更新是在："+mydate)
    }


    $(function() {
      //第一次立刻获得数据
      getModuleInfo();
      //实时更新60s
      setInterval(getModuleInfo,20000);
    });









    //*******************美化*表格*************//
    function check(){
      // alert('111')
      $('.hot').parents('tr').css('background-color','#CD0000');
      $('.hot').parents('tr').css('color','white');
      $('.hot').parents('tr').find('a').css('color','white');
      $('.new').parents('tr').css('background','#FF7F00');
      $('.new').parents('tr').css('color','white');
      $('.new').parents('tr').find('a').css('color','white');
    }
    $(function(){
      setInterval(check,1000);
    })


    //*******************美化*控件板*************//
    $(function(){
      $('.list-group-item').css('background-color','#1E90FF');
      $('.list-group-item').find('a').css('color','#FFFFFF');
    })