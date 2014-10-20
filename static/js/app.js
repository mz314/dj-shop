var djShop = angular.module('djshop', [
    'ngRoute',
    'ngSanitize',
    'ngCookies',
    'djShopControllers'

]);//.config(['$sce']);

djShop.config(['$routeProvider','$interpolateProvider',
    function($routeProvider,$interpolateProvider) {
        $routeProvider.
                when('/', {
                    templateUrl: 'static/partials/cms/home.html',
                    controller: 'HomeCtrl'
                }).
                when('/article/:articleId', {
                    templateUrl: 'static/partials/cms/article.html',
                    controller: 'ArticleCtrl'
                }).
                when('/shop/:catId?', {
                    templateUrl: 'static/partials/shop/category.html',
                    controller: 'ShopCtrl'
                }).
                when('/details/:itemId', {
                    templateUrl: 'static/partials/shop/item.html',
                    controller: 'ItemCtrl',
                }).
                when('/cart', {
                    templateUrl: 'static/partials/shop/cart.html',
                    controller: 'CartCtrl'
                }).
                when('/checkout/:orderId', {
                    templateUrl: 'static/partials/shop/summary.html',
                    controller: 'CheckoutCtrl'
                }).
                when('/userpanel',{
                    templateUrl: 'static/partials/userdata/panel.html',
                    controller: 'UserPanelController'
                }).
                when('/user/login/', {
                    templateUrl: '/static/partials/userdata/login.html',
                    controller: 'UserCtrl'
                });


    }]);

