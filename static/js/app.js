var djShop = angular.module('djshop', [
  'ngRoute',
  'djShopControllers'
]);

djShop.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: 'static/partials/cms/home.html',
        controller: 'HomeCtrl'
      }).
      when('/article/:articleId',{
          templateUrl: 'static/partials/cms/article.html',
          controller: 'ArticleCtrl'
      }).
    when('/shop/',{
      templateUrl: 'static/partials/shop/category.html',
      controller: 'ShopCtrl'  
      })              
      ;
  }]);