(function () {
    $.atoms.f5_monitor = [
        {
            tag_code: "health_value1",
            type: "input",
            attrs: {
                name: gettext("健康检查 name"),
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        },
    ]
})();
