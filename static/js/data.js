angular.module('openracer.data', ['ngResource'])
    .factory('events', function($resource) {
        return $resource('/rest/events/:id/');
    })
    .factory('eventDrivers', function($resource) {
        return $resource('/rest/event-drivers/:id/');
    })
    .factory('drivers', function($resource) {
        return $resource('/rest/drivers/:id/', {}, {
             update: { method: 'PATCH' }
        });
    })
    .factory('cars', function($resource) {
        return $resource('/rest/cars/:id/');
    })
    .factory('numbers', function($resource) {
        return $resource('/rest/numbers/:id/');
    })
    .factory('classes', function($resource) {
        return $resource('/rest/classes/:id/');
    });
