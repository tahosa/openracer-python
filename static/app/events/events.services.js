(function(){
    'use strict';

    angular.module('openracer.events')
        .factory('EventData', EventData)
        .factory('DriverData', DriverData);

    EventData.$inject = ['$resource'];
    function EventData($resource) {
        var events = {
            data: null,
            service: $resource('/rest/events/:id')

        };

        return events;
    }

    DriverData.$inject = ['$resource'];
    function DriverData($resource) {
        var drivers = {
            data: this.service.query(),
            service: $resource('/rest/event/:id/drivers')
        };

        return drivers;
    };
})();
