
function register_user() {
	// TODO: add client-side validations for improved responsiveness
	var data_dict = {
		"username" : $("#register-username-input").val(),
		"email" : $("#register-email-input").val(),
		"password" : $("#register-password-input").val(),
		"confirm_password" : $("#register-confirm-password-input").val()

	}
	$.ajax({
		url:"/auth/register",
    	type: 'POST',
		contentType: 'application/json',
		data: JSON.stringify(data_dict),
		success: function(data) {
			// TODO: Make better success messages
			$("#register-username-input").val('');
			$("#register-email-input").val('');
			$("#register-password-input").val('');
			$("#register-confirm-password-input").val('');
			$("#register-response-label").html(
				"Registration successful."
				);
		},
		error: function(){
			// TODO: Make better error messages
			$("#register-response-label").html(
				"Registration failed."
				);
	    }
	})
}

function login_user() {
	var data_dict = {
		"username" : $("#user_username").val(),
		"password" : $("#user_password").val()

	}
	$.ajax({
		url:"/auth/login",
    	type: 'POST',
		contentType: 'application/json',
		data: JSON.stringify(data_dict),
		success: function(data) {
			// TODO: Make better success messages
			window.location.href = '/'
		},
		error: function(){
			// TODO: Make better error messages
			$("#login-response-label").html(
				"Registration failed."
				);
	    }
	})
}

$(document).ready(function() {

    $("#register-button").on('click', function() {
    	$('#register-modal').modal('show');
    });

    $("#user-register-button").on('click', function() {
    	register_user();
    });

    $("#login-button").on('click', function() {
    	login_user();
    });


});