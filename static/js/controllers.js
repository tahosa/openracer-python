angular.module('openracer.controllers', ['openracer.data']).
    controller('mainCtrl', function($scope) {

    }).
    controller('indexCtrl', function($scope, $location, $modal, events) {
        $scope.setView = function(view) {
            if($scope.selected)
                $location.path("/events/" + $scope.selected + "/" + view);
        };

        $scope.newEvent = function() {
            $modal({
                title: "New Event",
                contentTemplate: "/static/partials/event-new.tpl.html",
                show: true,
                scope: $scope.$new()
            });
        };

        $scope.$on('openracer.event.created', function(event, data) {
            $scope.events.push(data);
        })

        $scope.events = events.query();
    }).
    controller('eventsCtrl', function($scope) {

    }).
    controller('runsCtrl', function($scope) {

    }).
    controller('standingsCtrl', function($scope) {

    }).
    controller('driversCtrl', function($scope) {
        $scope.drivers = [
            {
                id: 1,
                name: "Driver 1",
                number: "100",
            },
            {
                id: 2,
                name: "Driver 2",
                number: "89",
            },
            {
                id: 3,
                name: "Driver 3",
                number: "99",
            },
            {
                id: 4,
                name: "Driver 4",
                number: "21",
            },
            {
                id: 5,
                name: "Driver 5",
                number: "82",
            },
            {
                id: 6,
                name: "Driver 6",
                number: "4111",
            },
            {
                id: 7,
                name: "Driver 7",
                number: "1001",
            },
            {
                id: 8,
                name: "Driver 8",
                number: "58",
            },
            {
                id: 9,
                name: "Driver 9",
                number: "13",
            },
            {
                id: 10,
                name: "Driver 10",
                number: "29",
            },
        ];

        $scope.setActive = function(driver) {
            $scope.active = driver;
        }

        $scope.edit = function(driver) {
            $scope.editing = driver;
            $scope.active = driver;
        };

        $scope.save = function() {
            console.log($scope.editing);
        };

        $scope.cancel = function() {
            delete($scope.editing);
        };
    }).
    controller('newEventCtrl', function($scope, events) {
        $scope.event = {};

        $scope.save = function() {
            console.log($scope.event);
            events.save($scope.event).$promise.then(function(data) {
                $scope.$emit('openracer.event.created', data);
            });
            $scope.$hide();
        };

        $scope.cancel = function() {
            if ($scope.event) {
                $scope.event = {};
            }
            $scope.$hide();
        };
    });
