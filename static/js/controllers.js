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
    if(typeof $routeParams.catId==='undefined') {
        $routeParams.catId='';
    }
      $http.get('ajax/category/'+$routeParams.catId).success(function(data) {
            $scope.categories = data;
    });
    $http.get('ajax/items/'+$routeParams.catId).success(function(data) {
            $scope.items = data;
    });
  }]);
  
  
   djShopControllers.controller('ItemCtrl', ['$scope', '$routeParams','$http',
  function($scope, $routeParams,$http) {
        $http.get('ajax/item/'+$routeParams.itemId).success(function(data) {
            $scope.product=data[0];
    });
    $scope.addToCart=function (product_id) {
       $http.get('ajax/add_to_cart/'+product_id).success(function(data) {
        console.log(data);
       });
    };
  }]);
  