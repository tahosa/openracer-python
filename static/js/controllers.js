angular.module('openracer.controllers', []).
    controller('mainCtrl', function($scope){
        $scope.setView = function(view) {
            console.log(view);
        }
    }).
    controller('indexCtrl', function($scope){
        $scope.events = [
            {
                id: 1,
                name: "Event 1"
            },
            {
                id: 2,
                name: "Event 2"
            },
            {
                id: 3,
                name: "Event 3"
            },
            {
                id: 4,
                name: "Event 4"
            }
        ];
    });
