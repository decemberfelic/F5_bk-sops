(function () {
    $.atoms.f5_pool = [
        {
            tag_code: "pool_value1",
            type: "input",
            attrs: {
                name: gettext("pool name"),
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        },
        {
            tag_code: "pool_value2",
            type: "input",
            attrs: {
                name: gettext("monitor"),
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        },
        {
            tag_code: "pool_value3",
            type: "textarea",
            attrs: {
                name: gettext("members")
            }
        },
    ]
})();
