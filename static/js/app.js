(function(angular) {
  'use strict';

  angular.module('CREED',  ['ngRoute'])
  .controller('MainController', function($scope, $route, $routeParams, $location) {
    $scope.$route = $route;
    $scope.$location = $location;
    $scope.$routeParams = $routeParams;
  })
  .controller('LoginController', function($scope, $route, $routeParams, $location) {
    $scope.$route = $route;
    $scope.$location = $location;
    $scope.$routeParams = $routeParams;
    console.log('jeje');
  })
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
  })});
})(window.angular);
