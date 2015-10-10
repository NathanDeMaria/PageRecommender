$(document).ready(function() {
    inline_test();
    $("#inline-checkbox, #reddit-checkbox, #datatau-checkbox, #hackernews-checkbox").change(function() {
        var checked_var = $("#inline-checkbox").is(':checked');
        var reddit_checked_var = $("#reddit-checkbox").is(':checked');
        var datatau_checked_var = $("#datatau-checkbox").is(':checked');
        var hackernews_checked_var = $("#hackernews-checkbox").is(':checked');

        chrome.storage.local.set({'inline_percents': checked_var, 'reddit': reddit_checked_var,
                                  'datatau': datatau_checked_var, 'hackernews': hackernews_checked_var}, function() {
            if (checked_var) {
                $("#beta-sites").show();
            } else {
                $("#beta-sites").hide();
            }
            // Notify that we saved.
            $("#update-div").fadeIn(200);
            $("#update-div").fadeOut(1000);
        });
    });
});

function inline_test(){
    var details = ["inline_percents", "reddit", "datatau", "hackernews"];
    chrome.storage.local.get(details, function(data) {

        if(data.inline_percents == undefined || data.reddit == undefined ||
           data.datatau == undefined || data.hackernews == undefined) {
            if (data.inline_percents == undefined) {var tmp_inline = true} else {var tmp_inline = data.inline_percents};
            if (data.reddit == undefined) {var tmp_reddit = true} else {var tmp_reddit = data.reddit};
            if (data.datatau == undefined) {var tmp_datatau = true} else {var tmp_datatau = data.datatau};
            if (data.hackernews == undefined) {var tmp_hackernews = false} else {var tmp_hackernews = data.hackernews};

            chrome.storage.local.set({'inline_percents': tmp_inline, 'reddit': tmp_reddit,
                                      'datatau': tmp_datatau, 'hackernews': tmp_hackernews}, function() {
                $("#inline-checkbox").prop("checked", tmp_inline);
                $("#beta-sites").show();
                $("#reddit-checkbox").prop("checked", tmp_reddit);
                $("#datatau-checkbox").prop("checked", tmp_datatau);
                $("#hackernews-checkbox").prop("checked", tmp_hackernews);
            });
        } else {
            if (data.inline_percents) {
                $("#beta-sites").show();
                $("#reddit-checkbox").prop("checked", data.reddit);
                $("#datatau-checkbox").prop("checked", data.datatau);
                $("#hackernews-checkbox").prop("checked", data.hackernews);
            } else {
                $("#reddit-checkbox").prop("checked", data.reddit);
                $("#datatau-checkbox").prop("checked", data.datatau);
                $("#hackernews-checkbox").prop("checked", data.hackernews);
                $("#beta-sites").hide();
            };
            $("#inline-checkbox").prop("checked", data.inline_percents);
        }
    });
};