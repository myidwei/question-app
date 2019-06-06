function load_user_info(fun){
    $.get("/users/user_info", function (ret) {
        if (ret.code != 0 && fun != 'login') {
            layer.alert(ret.msg);
        } else {
            if (ret.data.status == 1 && fun != 'change_password') {
                layer.alert("Please change your password first!", function () {
                    window.location = "/users/change_password";
                });
                return;
            }
    
            if(ret.data.level == 'staff'){
                $("button[data-opt=published]").hide();
                $("button[data-opt=submitted]").show();
                $("button[data-opt=pendding]").show();
            }
            if(ret.data.level == 'manager' || ret.data.level == 'admin'){
                $("button[data-opt=published]").show();
                $("button[data-opt=submitted]").show();
                $("button[data-opt=pendding]").show();
            }
    
            if(ret.data.level != 'admin'){
                $(".user_item").hide();
            }
        }
    });
}


function load_menu(fun){
    $(".layui-nav").load("/manage/static/menu.html",function(){
        $("." + fun).addClass("layui-this");
        load_user_info(fun);
    });
}