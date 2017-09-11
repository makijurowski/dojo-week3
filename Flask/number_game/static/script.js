$(document).ready(function() {
    console.log('Loaded javascript');
    var $SCRIPT_ROOT = {{ request.script_root|tojson | safe }};
    /* $.getJSON($SCRIPT_ROOT + '/guess', {
        result: $['']
    } */
    $('#check').click(function() {
        $.ajax({
            type: "GET",
            url: $SCRIPT_ROOT + "/_get_result",
            contentType: "application/json; charset=utf-8",
            data: data,
            success: function (data) {
                alert('This worked!');
                // $('#wrapper').text(data.value);
                console.log('Result 1: ' + data);
            }
    });
});
});