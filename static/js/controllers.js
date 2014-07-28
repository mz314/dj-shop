var djShopControllers = angular.module('djShopControllers', []);



djShopControllers.controller('HomeCtrl', ['$scope', '$http',
  function($scope, $http) {
        $http.get('ajax/fronts').success(function(data) {
         $scope.articles = data;
    });
  }]);