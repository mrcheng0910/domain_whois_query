$(document).ready(function () {
    $("#whois").attr("class", "active"); //the function changes the nav active item

    $("#btn-more").bind("click", function () {
        $("#tr-show").fadeToggle("slow", function () {
            if ($("#more").attr("class") == "fa fa-angle-double-right fa-fw") {
                $("#more").attr("class", "fa fa-angle-double-down fa-fw");
            } else {
                $("#more").attr("class", "fa fa-angle-double-right fa-fw");
            }
        });
    });// to change the details ico
    $("#btn-query").bind("click", function () {
        $.ajax({
            url: '/whois/query',
            type: "get",
            data: {
                domain: $("#name").val(),
                stamp: Math.random()   // preventing "get" method using cache send to client
            },
            timeout: 5000, //超时时间
            success: function (data) {
                assignment_element(data);
            },  //成功后的处理
            error: function (xhr) {
                if (xhr.status == "0") {
                    alert("超时，稍后重试");
                } else {
                    alert("错误提示：" + xhr.status + " " + xhr.statusText);
                }
            } // 出错后的处理
        });
    });

    function assignment_element(data) {
        // assignment element
        var whois = JSON.parse(data);
        $("#query_domain").text(whois[0].domain);
        $("#top_whois_server").text(whois[0].top_whois_server);
        $("#reg_org").text(whois[0].org_name);
        $("#reg_name").text(whois[0].reg_name);
        $("#reg_phone").text(whois[0].reg_phone);
        $("#reg_email").text(whois[0].reg_email);
        $("#creation_date").text(whois[0].creation_date);
        $("#updated_date").text(whois[0].updated_date);
        $("#expiration_date").text(whois[0].expiration_date);
        $("#details").text(whois[0].domain_details);
    }
    document.onkeydown = function (e) { // to bind enter to the button
        var theEvent = window.event || e;
        var code = theEvent.keyCode || theEvent.which;
        if (code == 13) {
            $("#btn-query").click();
        }
    };
});