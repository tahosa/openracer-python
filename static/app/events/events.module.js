(function() {
    'use strict';

    angular
        .module('openracer.events', [
            'ngRoute',
            'mgcrea.ngStrap',

            'openracer.events.manager'
        ])
        .config(EventsConfig);

    EventsConfig.$inject = [ '$routeProvider' ];
    function EventsConfig($routeProvider) {
        $routeProvider
            .when('/events/:eventId?', {
                templateUrl: '/static/app/events/events.tpl.html',
                controller: 'Events',
                controllerAs: 'events'
            });

    }
})();
