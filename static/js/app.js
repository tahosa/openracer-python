var app = angular.module('openracer', ['ngRoute', 'ngResource', 'ngSanitize', 'mgcrea.ngStrap', 'openracer.controllers']);

app.config(['$routeProvider', '$locationProvider',
    function($routeProvider, $locationProvider) {
        $locationProvider.html5Mode(true).hashPrefix('!');

        $routeProvider.when('/', {
            templateUrl: '/static/partials/index.tpl.html',
            controller: 'indexCtrl'
        }).
        when('/events/:id?', {
            templateUrl: '/static/partials/events.tpl.html',
            controller: 'eventsCtrl'
        }).
        when('/events/:id/runs', {
            templateUrl: '/static/partials/runs.tpl.html',
            controller: 'runsCtrl'
        }).
        when('/events/:id/standings', {
            templateUrl: '/static/partials/standings.tpl.html',
            controller: 'standingsCtrl'
        }).
        when('/events/:id/drivers', {
            templateUrl: '/static/partials/drivers.tpl.html',
            controller: 'driversCtrl'
        }).
        otherwise({
            redirectTo: '/'
        })
    }]);
