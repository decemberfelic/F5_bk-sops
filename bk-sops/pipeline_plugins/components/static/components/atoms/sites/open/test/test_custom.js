(function () {
    $.atoms.test_custom = [
        {
            tag_code: "test_custom_value",
            type: "input",
            attrs: {
                name: gettext("参数"),
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        },
        {
            tag_code: "test_custom_value2",
            type: "textarea",
            attrs: {
                name: gettext("参数2")
            }
        },
    ]
})();
