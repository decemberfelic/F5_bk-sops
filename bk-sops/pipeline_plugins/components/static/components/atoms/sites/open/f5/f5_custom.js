(function () {
    $.atoms.test_custom = [
        {
            tag_code: "test_custom_value1",
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


(function () {
    $.atoms.f5_custom = [
        {
            tag_code: "test_custom_value3",
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
            tag_code: "test_custom_value4",
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
    ]
})();