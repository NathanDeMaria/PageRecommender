$(document).ready(function() {
    // Set data if necessary
    chrome.storage.local.get("inline_percents", function(data) {
        if(data.inline_percents == undefined) {
            chrome.storage.local.set({'inline_percents': true}, function() {});
        }
    });

    chrome.storage.local.get("inline_percents", function(data) {
        if (data.inline_percents) {
            var website = document.location.href;
            var site = document.location.hostname.substr(4);
            if (website.indexOf("datatau.com") >= 0 || website.indexOf("news.ycombinator.com") >= 0) {
                $("a").each(function (ind, val) {
                    var tmp_parent = $(this).parent().get(0);

                    if (tmp_parent.tagName == "TD" && tmp_parent.className == 'title' && $(this).text() != 'More' &&
                        $(this).attr('href').indexOf(site) == -1 &&
                        $(this).attr('href').indexOf("http") != -1) {
                        //console.log(tmp_parent.tagName + ' ::: ' + tmp_parent.className);
                        var tmp_link = $(this);
                        var tmp_url = tmp_link.attr('href');
                        try {
                            $.post("http://127.0.0.1:8000/extension/inline", {url: tmp_url}, function (data) {
                                tmp_link.prepend(data);
                                //$("#percent-val").text(data);
                                //$("#loading-div").hide();
                            }).fail(function () {
                                console.log('No connection can be made to the server. Please check your internet connection' +
                                    ' or warn the admin that the server is down.')
                            });
                        } catch (err) {
                            console.log('No connection can be made to the server. Please check your internet connection' +
                                ' or warn the admin that the server is down.')
                        }
                    }
                });
            // REDDIT
            } else if (website.indexOf("reddit.com") >= 0) {
                $("a").each(function (ind, val) {
                    var tmp_parent = $(this).parent().get(0);

                    if (tmp_parent.tagName == "P" && tmp_parent.className == 'title' &&
                        $(this).attr('href').indexOf("reddit.com") == -1 &&
                        $(this).attr('href').indexOf("imgur.com") == -1 &&
                        $(this).attr('href').indexOf("http") != -1) {
                        //console.log(tmp_parent.tagName + ' ::: ' + tmp_parent.className);
                        var tmp_link = $(this);
                        var tmp_url = tmp_link.attr('href');
                        try {
                            $.post("http://127.0.0.1:8000/extension/inline", {url: tmp_url}, function (data) {
                                tmp_link.prepend(data);
                                //$("#percent-val").text(data);
                                //$("#loading-div").hide();
                            }).fail(function () {
                                console.log(tmp_url);
                                console.log('No connection can be made to the server. Please check your internet connection' +
                                    ' or warn the admin that the server is down.')
                            });
                        } catch (err) {
                            console.log('No connection can be made to the server. Please check your internet connection' +
                                ' or warn the admin that the server is down.')
                        }
                    }
                });
            }
        }
    });
});

// WHAT TO DO WHEN A HASH HAS CHANGED...REALLY ONLY APPLIES TO REDDIT ENHANCEMENT SUITE USAGE
$(window).on('hashchange', function() {
    // Set data if necessary
    var details = ["inline_percents", "reddit", "datatau", "hackernews"];
    chrome.storage.local.get(details, function(data) {
        if(data.inline_percents == undefined) {
            chrome.storage.local.set({'inline_percents': true, 'reddit': true,
                                      'datatau': true, 'hackernews':true}, function() {});
        }
    });

    chrome.storage.local.get(details, function(data) {
        if (data.inline_percents) {
            var website = document.location.href;
            var site = document.location.hostname.substr(4);
            if ((website.indexOf("datatau.com") >= 0 && data.datatau) ||
                (website.indexOf("news.ycombinator.com") >= 0 && data.hackernews)) {
                $("a").each(function (ind, val) {
                    var tmp_parent = $(this).parent().get(0);

                    if (tmp_parent.tagName == "TD" && tmp_parent.className == 'title' && $(this).text() != 'More' &&
                        $(this).attr('href').indexOf(site) == -1 &&
                        $(this).attr('href').indexOf("http") != -1) {
                        //console.log(tmp_parent.tagName + ' ::: ' + tmp_parent.className);
                        var tmp_link = $(this);
                        var tmp_url = tmp_link.attr('href');
                        try {
                            $.post("http://127.0.0.1:8000/extension/inline", {url: tmp_url}, function (data) {
                                tmp_link.prepend(data);
                                //$("#percent-val").text(data);
                                //$("#loading-div").hide();
                            }).fail(function () {
                                console.log('No connection can be made to the server. Please check your internet connection' +
                                    ' or warn the admin that the server is down.')
                            });
                        } catch (err) {
                            console.log('No connection can be made to the server. Please check your internet connection' +
                                ' or warn the admin that the server is down.')
                        }
                    }
                });
            // REDDIT
            } else if (website.indexOf("reddit.com") >= 0 && data.reddit) {
                $("a").each(function (ind, val) {
                    var tmp_parent = $(this).parent().get(0);

                    if (tmp_parent.tagName == "P" && tmp_parent.className == 'title' &&
                        $(this).attr('href').indexOf("reddit.com") == -1 &&
                        $(this).attr('href').indexOf("imgur.com") == -1 &&
                        $(this).attr('href').indexOf("http") != -1) {
                        //console.log(tmp_parent.tagName + ' ::: ' + tmp_parent.className);
                        var tmp_link = $(this);
                        var tmp_url = tmp_link.attr('href');
                        try {
                            $.post("http://127.0.0.1:8000/extension/inline", {url: tmp_url}, function (data) {
                                tmp_link.prepend(data);
                                //$("#percent-val").text(data);
                                //$("#loading-div").hide();
                            }).fail(function () {
                                console.log(tmp_url);
                                console.log('No connection can be made to the server. Please check your internet connection' +
                                    ' or warn the admin that the server is down.')
                            });
                        } catch (err) {
                            console.log('No connection can be made to the server. Please check your internet connection' +
                                ' or warn the admin that the server is down.')
                        }
                    }
                });
            }
        }
    });
});