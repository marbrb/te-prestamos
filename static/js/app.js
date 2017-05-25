(function(angular) {
  'use strict';

  angular.module('CREED',  ['ngRoute', 'ngCookies'])
  .factory('consult', function($http) {
      let url = '/creditos';
      return {
          getCreditos: function() {
              //console.log($http.get);
              return $http.get(url);
          }
      }
  })
  .factory('autorization', function ($http) {
    let url = '/login';
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
  .controller('MainController', ['$scope', '$location', 'consult', function($scope, $location, consult) {
    function success(res) {
        //console.log(res.data);
        if(res.data.logged === false) {
            //The user is not logged
            $location.path('/login');
        }
    }

    function error(err) {
        //TODO: Manejar el error
    }  
    console.log(consult);
    consult.getCreditos().then(success).catch(error); 
  }])

  .controller('LoginController', ['$scope', '$location', 'autorization', '$cookies', function($scope, $location, autorization, $cookies) {
      $scope.title = 'Login';

      $scope.submit = function() {
        const credentials = {
          user: this.user.cedula,
          password: this.user.pass
        };

        console.log(credentials);

        function success(res) {
          console.log(res.data);
          let cookie = res.data.token;

          $cookies.put('cookie', cookie);
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
          templateUrl: 'static/templates/home.html',
          controller: 'MainController'

      })
      .when('/login', {
        templateUrl: 'static/templates/login.html',
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
