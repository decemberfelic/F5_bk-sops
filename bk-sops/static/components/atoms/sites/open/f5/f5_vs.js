(function () {
    $.atoms.f5_vs = [
        {
            tag_code: "vs_value1",
            type: "input",
            attrs: {
                name: gettext("VS name"),
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        },
        {
            tag_code: "vs_value2",
            type: "textarea",
            attrs: {
                name: gettext("VIP")
            }
        },
                {
            tag_code: "vs_value3",
            type: "textarea",
            attrs: {
                name: gettext("ipProtocol")
            }
        },
                {
            tag_code: "vs_value4",
            type: "textarea",
            attrs: {
                name: gettext("pool")
            }
        },
                {
            tag_code: "vs_value5",
            type: "textarea",
            attrs: {
                name: gettext("profiles")
            }
        },
    ]
})();
