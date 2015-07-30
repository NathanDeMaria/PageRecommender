$(document).ready(function() {
    // Set data if necessary
    chrome.storage.local.get("inline_percents", function(data) {
        if(data.inline_percents == undefined) {
            chrome.storage.local.set({'inline_percents': true}, function() {});
        };
    });

    chrome.storage.local.get("inline_percents", function(data) {
        if (data.inline_percents) {
            $("a").each(function(ind, val) {
                var tmp_parent = $(this).parent().get(0);

                if (tmp_parent.tagName == "TD" && tmp_parent.className == 'title' && $(this).text() != 'More' &&
                    $(this).attr('href').indexOf("datatau.com") == -1 &&
                    $(this).attr('href').indexOf("http") != -1) {
                    //console.log(tmp_parent.tagName + ' ::: ' + tmp_parent.className);
                    var tmp_link = $(this);
                    var tmp_url = tmp_link.attr('href');
                    try {
                        $.post("http://127.0.0.1:8000/extension/inline", {url: tmp_url}, function (data) {
                            tmp_link.prepend(data);
                            //$("#percent-val").text(data);
                            //$("#loading-div").hide();
                        }).fail(function() {
                            console.log(tmp_url);
                            console.log('No connection can be made to the server. Please check your internet connection' +
                                        ' or warn the admin that the server is down.')
                        });
                    } catch(err) {
                        console.log('No connection can be made to the server. Please check your internet connection' +
                                    ' or warn the admin that the server is down.')
                    };
                };
            });
        };
    });
});