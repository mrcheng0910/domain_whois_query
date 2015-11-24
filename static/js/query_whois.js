/**
 * Created by mrcheng on 15-11-24.
 */
function test(domain_whois) {
    whois = JSON.parse(domain_whois);
    //alert(whois[0].reg_name);
    $("#reg_name").val(whois[0].reg_name);
};