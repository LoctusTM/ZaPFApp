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
<<<<<<< HEAD
            app_component_1.AppComponent.dataUrl = "https://zapf.ethylomat.de/database.json";
=======
            app_component_1.AppComponent.dataUrl = "htts://zapf.ethylomat.de/database.json";
>>>>>>> a117d26eeb584598d8ff7a4cd6057943bbad56b4
            browser_1.bootstrap(app_component_1.AppComponent, [http_1.HTTP_PROVIDERS]);
        }
    }
});
//# sourceMappingURL=main.js.map
