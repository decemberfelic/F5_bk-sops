(function () {
    $.atoms.f5_profile = [
        {
            tag_code: "profile_value1",
            type: "input",
            attrs: {
                name: gettext("http profile name"),
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        },
    ]
})();
