System.register(['angular2/platform/browser', './app.component.js', 'angular2/http'], function(exports_1, context_1) {
    "use strict";
    var __moduleName = context_1 && context_1.id;
    var browser_1, app_component_1, http_1;
    return {
        setters:[
            function (browser_1_1) {
                browser_1 = browser_1_1;
            },
            function (app_component_1_1) {
                app_component_1 = app_component_1_1;
            },
            function (http_1_1) {
                http_1 = http_1_1;
            }],
        execute: function() {
            // app_component_1.AppComponent.dataUrl = "http://0.0.0.0:8000/database.json";
            app_component_1.AppComponent.dataUrl = "https://zapf.ethylomat.de/database.json";
            browser_1.bootstrap(app_component_1.AppComponent, [http_1.HTTP_PROVIDERS]);
        }
    }
});
//# sourceMappingURL=main.js.map
