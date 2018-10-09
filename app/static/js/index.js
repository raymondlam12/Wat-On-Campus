
function register_event() {
    // TODO: add client-side validations for improved responsiveness
    var data_dict = {
        "title" : $("#event-title-input").val(),
        "description" : $("#event-description-input").val(),
        "location" : $("#event-location-input").val(),
        "date" : $("#date-picker-input").val()

    }
    $.ajax({
        url:"/event/register",
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(data_dict),
        success: function(data) {
            // TODO: Make better success messages
            $("#event-title-input").val('');
            $("#event-description-input").val('');
            $("#event-location-input").val('');
            $("#date-time-picker").val('');
            $("#register-response-label").html(
                "Event registration successful."
                );
        },
        error: function(){
            // TODO: Make better error messages
            $("#register-response-label").html(
                "Event registration failed."
                );
        }
    })
}

function load_events() {
    $.ajax({
        url:"/event/events",
        type: 'GET',
        contentType: 'application/json',
        success: function(data) {
            // TODO: Make better success messages
            for (i = 0; i < data.length; ++i) {

                var username = data[i]['username']
                var description = data[i]['description']
                var title = data[i]['title']
                var location = data[i]['location']
                var date = data[i]['date']
                var email = data[i]['email']



                $("#event-listing").append(
                    "<div class=\"bottom-margin\">" +
                        "<div class=\"text-center\">" +
                            "<div class=\"rounded-box\">" +
                                "<h1>" + title + "</h1>" +
                                "<h3>Hosted by: " + username + "</h3>" +
                                "<h3>Location: " + location + "</h3>" +
                                "<h3>Date: " + date + "</h3>" +
                                "<p>" + description + "</p>" +
                                "<p>Questions can be directed to: " + email + "</p>" +
                            "</div>" +
                        "</div>" +
                    "</div> "
                );
            }


            

        },
        error: function(){
            // TODO: Make better error messages
            $("#event-listing").append(
                "Could not load list of events."
                );
        }
    })
}

$(document).ready(function() {

    $("#add-event-button").on('click', function() {
        $('#add-event-modal').modal('show');
    });

    $('#date-time-picker').datepicker({
        format: 'mm/dd/yyyy',
        startDate: '-3d'
    });

    $("#event-register-button").on('click', function() {
        register_event();
    });

    load_events()

});