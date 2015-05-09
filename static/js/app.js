var app = angular.module('openracer', ['ngRoute', 'ngSanitize', 'mgcrea.ngStrap', 'openracer.controllers', 'openracer.data']);

app.config(['$routeProvider', '$locationProvider', '$httpProvider', '$resourceProvider',
    function($routeProvider, $locationProvider, $httpProvider, $resourceProvider) {
        $locationProvider.html5Mode(true).hashPrefix('!');

        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        $resourceProvider.defaults.stripTrailingSlashes = false;

        $routeProvider.when('/', {
            templateUrl: '/static/partials/index.tpl.html',
            controller: 'indexCtrl'
        }).
        when('/events/:eventId?', {
            templateUrl: '/static/partials/events.tpl.html',
            controller: 'eventsCtrl'
        }).
        when('/events/:eventId/runs', {
            templateUrl: '/static/partials/runs.tpl.html',
            controller: 'runsCtrl'
        }).
        when('/events/:eventId/standings', {
            templateUrl: '/static/partials/standings.tpl.html',
            controller: 'standingsCtrl'
        }).
        when('/events/:eventId/drivers', {
            templateUrl: '/static/partials/drivers.tpl.html',
            controller: 'driversCtrl'
        }).
        otherwise({
            redirectTo: '/'
        })
    }]);
