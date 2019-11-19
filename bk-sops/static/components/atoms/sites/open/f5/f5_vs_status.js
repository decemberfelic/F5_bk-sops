(function () {
    $.atoms.f5_vs_status = [
        {
            tag_code: "vs_status1",
            type: "input",
            attrs: {
                name: gettext("需要检查的状态"),
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        },
    ]
})();
