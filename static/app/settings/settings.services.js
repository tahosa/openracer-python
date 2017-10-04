(function() {
    'use strict';

    angular.module('openracer.settings')
        .factory('SettingsData', SettingsData);

    SettingsData.$inject = [ '$resource' ];
    function SettingsData($resource) {
        var settings = {
            classes: $resource('/rest/classes/:id/')
        };

        return settings;
    }
})();
