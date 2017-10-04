(function() {
    'use strict';

    angular.module('openracer.drivers')
        .factory('DriverData', DriverData);

    DriverData.$inject = [ '$resource' ];
    function DriverData($resource) {
        var drivers = {
            drivers: $resource('/rest/drivers/:id/', {}, {
                     update: { method: 'PATCH' }
                }),
            cars: $resource('/rest/cars/:id/'),
            numbers: $resource('/rest/numbers/:id/'),
            classes: $resource('/rest/classes')
        };

        return drivers;
    }
})();
