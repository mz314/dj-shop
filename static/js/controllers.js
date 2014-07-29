var djShopControllers = angular.module('djShopControllers', []);



djShopControllers.controller('HomeCtrl', ['$scope', '$http',
  function($scope, $http) {
        $http.get('ajax/fronts').success(function(data) {
         $scope.articles = data;
    });
  }]);
  
  djShopControllers.controller('ArticleCtrl', ['$scope', '$routeParams','$http',
  function($scope, $routeParams,$http) {
        $http.get('ajax/article/'+$routeParams.articleId).success(function(data) {
            $scope.article = data[0];
    });
  }]);
  
    djShopControllers.controller('ShopCtrl', ['$scope', '$routeParams','$http',
  function($scope, $routeParams,$http) {
        $http.get('ajax/category/').success(function(data) {
            $scope.categories = data;
    });
    $http.get('ajax/items/1').success(function(data) {
            $scope.items = data;
    });
  }]);
  
  