$(document).ready(function() {
    inline_test();
    $("#inline-checkbox").change(function() {
        var checked_var = $("#inline-checkbox").is(':checked');
        chrome.storage.local.set({'inline_percents': checked_var}, function() {
            // Notify that we saved.
            $("#update-div").fadeIn(200);
            $("#update-div").fadeOut(1000);
        });
    });
});

function inline_test(){
    chrome.storage.local.get("inline_percents", function(data) {
        if(data.inline_percents == undefined) {
            chrome.storage.local.set({'inline_percents': true}, function() {
                $("#inline-checkbox").prop("checked", true);
            });
        } else {
            $("#inline-checkbox").prop("checked", data.inline_percents);
        }
    });
};