//初始化whois信息
function test(domain_whois) {

    //if (domain_whois){
    //    whois = JSON.parse(domain_whois);
    //    $("#reg_name").text(whois[0].reg_name)
    //}else{
    //    alert("nihao");
    //    $("#reg_name").val("")
    //}
    $("#reg_name").val("")

}

//ajax数据分析
$(function () {
    $("#domain_query").bind("click", function () {
        $.post('/whois', {domain: $("#domain").val()}, function (data) {
            test(data);
        });
    });
});