$(document).on("submit", "#mailingForm", function (e) {
    e.preventDefault();
    var form = $(this);
    var actionUrl = form.attr("data-url");

    $.ajax({
        type: "POST",
        url: actionUrl,
        data: form.serialize(),
        success: function (response) {
            toastr.success("Mailing list created");
            window.location.href = "/mailer/";
        },
        error: function (response) {
            toastr.error("Error when creating a mailing list: " + response.responseText);
        }
    });
});
