angular.module('openracer.data', ['ngResource'])
    .factory('events', function($resource) {
        return $resource('/rest/events/:id/');
    })
