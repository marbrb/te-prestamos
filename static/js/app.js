(function(angular) {
  'use strict';

  angular.module('CREED',  ['ngRoute'])
  .controller('MainController', [
    '$scope',
    '$http',
    '$location',
    function($scope, $http, $location) {

  }])
  .controller('LoginController', [
    '$scope',
    '$http',
    '$location',
    function($scope, $http, $location) {
      $scope.submit = function() {
        console.log($scope.user);
        //console.log($http);
      }
    }])
    .config(function($routeProvider, $locationProvider) {
      $routeProvider
      .when('/', {
        templateUrl: 'templates/login.html',
        controller: 'LoginController',
        resolve: {
          // I will cause a 1 second delay
          delay: function($q, $timeout) {
            var delay = $q.defer();
            $timeout(delay.resolve, 1000);
            return delay.promise;
          }
        }
      })
    });
})(window.angular);
