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
    var SlotsComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            }],
        execute: function() {
            SlotsComponent = (function () {
                function SlotsComponent() {
                }
                SlotsComponent.prototype.formatTime = function (begin, end) {
                    var weekdays = new Array(7);
                    weekdays[0] = "So";
                    weekdays[1] = "Mo";
                    weekdays[2] = "Di";
                    weekdays[3] = "Mi";
                    weekdays[4] = "Do";
                    weekdays[5] = "Fr";
                    weekdays[6] = "Sa";
                    var b = new Date(begin);
                    var e = new Date(end);
                    return weekdays[b.getDay()] + " "
                        + b.getHours() + ":" + ("0" + b.getMinutes()).slice(-2)
                        + " - "
                        + e.getHours() + ":" + ("0" + e.getMinutes()).slice(-2);
                };
                SlotsComponent.prototype.unfinished = function (end) {
                    return Date.now() < Date.parse(end);
                };
                __decorate([
                    core_1.Input(), 
                    __metadata('design:type', Object)
                ], SlotsComponent.prototype, "slots", void 0);
                __decorate([
                    core_1.Input(), 
                    __metadata('design:type', Object)
                ], SlotsComponent.prototype, "prefs", void 0);
                SlotsComponent = __decorate([
                    core_1.Component({
                        selector: '.slotscomponent',
                        templateUrl: 'static/app/slots.component.html'
                    }), 
                    __metadata('design:paramtypes', [])
                ], SlotsComponent);
                return SlotsComponent;
            }());
            exports_1("SlotsComponent", SlotsComponent);
        }
    }
});
//# sourceMappingURL=slots.component.js.map