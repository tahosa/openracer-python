var app = angular.module('openracer', ['ngRoute', 'ngResource', 'mgcrea.ngStrap', 'openracer.controllers']);

app.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.when('/', {
            templateUrl: '/static/partials/index.tpl.html',
            controller: 'indexCtrl'
        }).
        otherwise({
            redirectTo: '/'
        })
    }]);
