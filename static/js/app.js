(function(angular) {
  'use strict';

  angular.module('CREED',  ['ngRoute'])
  .controller('MainController', [
    '$scope',
    '$location',
    function($scope, $location) {

  }])
  .factory('autorization', function ($http) {
    let url = 'http://10.20.232.38:8888/login';
    return {
      login: function (credentials) {
          console.log('Helooo, me estoy loggeando');
          return $http({
            method: 'POST',
            url: url,
            data: credentials
          });
      }
    };
  })
  .controller('LoginController', ['$scope', '$location', 'autorization',
    function($scope, $location, autorization) {
      $scope.title = 'Login';

      $scope.submit = function() {
        const credentials = {
          user: this.user.cedula,
          pass: this.user.pass
        };

        console.log(credentials);

        function success(data) {
          let cookie = data.token;

          $cookieStore.put('token', token);
          $location.path('/');
        };

        function error(err) {
          console.log(err);
        };

        autorization.login(credentials).then(success).catch(error);
      };

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
    })
})(window.angular);
