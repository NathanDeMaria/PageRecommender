window.onload= function() {
	chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
	    var url = tabs[0].url;
	    var hiddenInput = document.getElementById('url-input');
	    hiddenInput.value = url;
	});	
};