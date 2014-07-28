var djShop = angular.module('djshop', [
  'ngRoute',
  'djShopControllers'
]);

djShop.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: 'static/js/app/partials/home.html',
        controller: 'HomeCtrl'
      });
  }]);