System.register(['angular2/core'], function(exports_1, context_1) {
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
    var core_1;
    var NewsComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            }],
        execute: function() {
            NewsComponent = (function () {
                function NewsComponent() {
                }
                NewsComponent.prototype.formatTime = function (time) {
                    console.log(time);
                    var weekdays = new Array(7);
                    weekdays[0] = "So";
                    weekdays[1] = "Mo";
                    weekdays[2] = "Di";
                    weekdays[3] = "Mi";
                    weekdays[4] = "Do";
                    weekdays[5] = "Fr";
                    weekdays[6] = "Sa";
                    var t = new Date(time);
                    return weekdays[t.getDay()] + " "
                        + t.getHours() + ":" + ("0" + t.getMinutes()).slice(-2);
                };
                __decorate([
                    core_1.Input(), 
                    __metadata('design:type', Object)
                ], NewsComponent.prototype, "news", void 0);
                NewsComponent = __decorate([
                    core_1.Component({
                        selector: '.newscomponent',
                        templateUrl: 'static/app/news.component.html'
                    }), 
                    __metadata('design:paramtypes', [])
                ], NewsComponent);
                return NewsComponent;
            }());
            exports_1("NewsComponent", NewsComponent);
        }
    }
});
//# sourceMappingURL=news.component.js.map