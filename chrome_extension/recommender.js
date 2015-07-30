$(document).ready(function() {
    chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
        var tab_url = tabs[0].url;
        $("#url-input").val(tab_url);
        $.post("http://127.0.0.1:8000/extension/load", {url: tab_url},function(data) {
            $("#percent-val").text(data);
        });
    });
});