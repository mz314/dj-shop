var djShopControllers = angular.module('djShopControllers', []);



djShopControllers.controller('HomeCtrl', ['$scope', '$http',
    function($scope, $http) {
        $http.get('ajax/fronts').success(function(data) {
            $scope.articles = data;
        });
    }]);

djShopControllers.controller('ArticleCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http) {
        $http.get('ajax/article/' + $routeParams.articleId).success(function(data) {
            $scope.article = data[0];
        });
    }]);

djShopControllers.controller('ShopCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http) {
        if (typeof $routeParams.catId === 'undefined') {
            $routeParams.catId = '';
        }
        $http.get('ajax/category/' + $routeParams.catId).success(function(data) {
            $scope.categories = data;
        });
        $http.get('ajax/items/' + $routeParams.catId).success(function(data) {
            $scope.items = data;
        });
    }]);


djShopControllers.controller('ItemCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http) {
        $http.get('ajax/item/' + $routeParams.itemId).success(function(data) {
            $scope.product = data[0];
        });

    }]);

djShopControllers.controller('CartCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http) {
        $scope.loadCart=function () {
            $http.get('ajax/cart/').success(function(data) {
            $scope.items = data;
            });
        };
        
        $scope.loadCart();
        
        $scope.cleanCart = function() {
            $http.get('ajax/cart/clean/').success(function(data) {
                    $scope.loadCart();
            });
        };
    }]);



djShopControllers.controller('CartAddController', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http) {
        $scope.addToCart = function(item, id) {
            $http.get('ajax/add_to_cart/' + id).success(function(data) {
            });
        };
    }]);


djShopControllers.controller('CleanCartController', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http) {
        
    }]);

djShopControllers.controller('UserCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http) {
        
      
       // $scope.create_form.html('kupa');
    
    }]);