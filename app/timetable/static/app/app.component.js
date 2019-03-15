System.register(['angular2/core', 'angular2/http', 'rxjs/Rx', './slots.component.js', './news.component.js'], function(exports_1, context_1) {
    "use strict";
    var __moduleName = context_1 && context_1.id;
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, http_1, slots_component_1, news_component_1;
    var AppComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (http_1_1) {
                http_1 = http_1_1;
            },
            function (_1) {},
            function (slots_component_1_1) {
                slots_component_1 = slots_component_1_1;
            },
            function (news_component_1_1) {
                news_component_1 = news_component_1_1;
            }],
        execute: function() {
            AppComponent = (function () {
                function AppComponent(http, renderer) {
                    var _this = this;
                    this.http = http;
                    this.renderer = renderer;
                    // state
                    this.menu = false;
                    this.view = "slots";
                    this.state = "loading";
                    // load recent view
                    if (localStorage && localStorage.getItem("view") !== null)
                        this.view = localStorage.getItem("view");
                    // load prefs
                    if (localStorage && localStorage.getItem("prefs") !== null)
                        this.prefs = JSON.parse(localStorage.getItem("prefs"));
                    else
                        this.prefs = {
                            slots: {
                                showFinished: false,
                                showNotAk: true,
                                highlight: true
                            }
                        };
                    // register to online/ofline events
                    renderer.listenGlobal("window", "online", function (event) {
                        setTimeout(_this.refreshData, 1000);
                    });
                    renderer.listenGlobal("window", "offline", function (event) {
                        _this.state = "offline";
                    });
                }
                AppComponent.prototype.ngOnInit = function () {
                    var _this = this;
                    // check for beamer mode
                    if (window.location.hash)
                        this.view = window.location.hash.substring(1);
                    // load Data
                    if (localStorage && localStorage.getItem("data") !== null)
                        this.data = JSON.parse(localStorage.getItem("data"));
                    this.refreshData();
                    // register beamer update
                    if (this.view == "beamer")
                        setInterval(function () { return _this.refreshData(); }, 20000);
                };
                AppComponent.prototype.refreshData = function () {
                    var _this = this;
                    this.state = "loading";
                    if (!navigator.onLine) {
                        this.state = "offline";
                        return;
                    }
                    this.http.get(AppComponent.dataUrl)
                        .map(function (res) { return res.json(); })
                        .subscribe(function (data) {
                        _this.state = "online";
                        _this.data = data;
                        if (localStorage)
                            localStorage.setItem("data", JSON.stringify(data));
                    }, function (httperror) {
                        _this.state = "error";
                    });
                };
                AppComponent.prototype.chView = function (view) {
                    this.view = view;
                    this.menu = false;
                    if (localStorage)
                        localStorage.setItem("view", view);
                    this.savePrefs();
                };
                AppComponent.prototype.savePrefs = function () {
                    if (localStorage)
                        localStorage.setItem("prefs", JSON.stringify(this.prefs));
                };
                AppComponent = __decorate([
                    core_1.Component({
                        selector: '.appcomponent',
                        viewProviders: [http_1.HTTP_PROVIDERS],
                        directives: [slots_component_1.SlotsComponent, news_component_1.NewsComponent],
                        templateUrl: 'static/app/app.component.html'
                    }), 
                    __metadata('design:paramtypes', [http_1.Http, core_1.Renderer])
                ], AppComponent);
                return AppComponent;
            }());
            exports_1("AppComponent", AppComponent);
        }
    }
});
//# sourceMappingURL=app.component.js.map
