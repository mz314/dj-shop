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
        $http.get('api/categories/' + $routeParams.catId).success(function(data) {
            $scope.categories = data;
        });
        $http.get('api/items/' + $routeParams.catId).success(function(data) {
            $scope.items = data;
        });
    }]);


djShopControllers.controller('ItemCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http) {
        $http.get('ajax/item/' + $routeParams.itemId).success(function(data) {
            $scope.product = data[0];
        });

    }]);


djShopControllers.controller('CheckoutCtrl', ['$scope', '$routeParams', '$http', '$sce','$cookies', '$location',
    function($scope, $routeParams, $http, $sce,$cookies,$location) {
        $scope.gw_template =
                {name: 'payment.html', url: '/static/partials/shop/payment.html'}
        ;

        $scope.loadOrder = function() {
            $http.get('/api/orders/' + $routeParams.orderId).success(function(data) {
                $scope.order = data;
                $scope.loadPayment();
            });

        };

        $scope.processPayment = function(fields) {
            $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
            $http.post($scope.gw_data.config.action+'/'+$scope.order.id,fields).success(function (data) {
                $scope.gw_errors=null;
                if(data.errors.length===0) {
                    alert('Cool');
                    //$location.path('/checkout/' + $scope.order.id);
                     //zrobić chowanie ngifem
               } else {
                   $scope.gw_errors=data.errors;
               }
            });
            
        };

        $scope.loadPayment = function() {
            $http.get('/api/payment/gateway/' + $scope.order.payment.id).success(function(data) {
                $scope.gw_data = data;
            });
        };


        $scope.loadOrder();
    }
]);

djShopControllers.controller('CartCtrl', ['$scope', '$routeParams', '$http', '$sce', '$location',
    function($scope, $routeParams, $http, $sce, $location) {
        $scope.total_items = 0;
        $scope.loadCart = function() {
            $http.get('api/cart').success(function(data) {
                $scope.items = data;
                $scope.sum();
            });
        };

        $scope.cleanCart = function() {
            $http.get('ajax/cart/clean/').success(function(data) {
                $scope.loadCart();

            });
        };



        $scope.sum = function() {
            for (i = 0; i < $scope.items.length; i++) {

                $scope.total_items += $scope.items[i].item.price * $scope.items[i].quantity;
                console.log($scope.items[i]);
            }
        }


        $scope.checkout = function(shipment, payment) {
            console.log(payment);

            console.log(shipment);

            $http.get('ajax/cart/checkout/' + shipment.id + '/' + payment.id + '/').success(function(data) {
                console.log(data);

                $location.path('/checkout/' + data);
            });
        }

        $scope.loadShipments = function() {
            $http.get('ajax/cart/shipment/').success(function(data) {
                $scope.shipment = data;
            });
        }

        $scope.loadPayments = function() {
            $http.get('/api/payment_list').success(function(data) {
                $scope.payments = data;
                console.log(data);
            });
        }

        $scope.sprice = 0;
        $scope.payments = 0;


        $scope.loadCart();
        $scope.loadShipments();
        $scope.loadPayments();





    }]);



djShopControllers.controller('CartAddController', ['$scope', '$routeParams', '$http', '$cookies',
    function($scope, $routeParams, $http, $cookies) {
        $scope.addToCart = function(item, id) {
            var q = $scope.quantity;

            $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
            $http.post('api/cart/' + id + '/' + q).success(function(data) {
            });
        };
    }]);


djShopControllers.controller('CleanCartController', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http) {

    }]);

djShopControllers.controller('UserCtrl', ['$scope', '$routeParams', '$http', '$sce',
    function($scope, $routeParams, $http, $sce, $interpolateProvider) {



        $scope.login = function() {
            //console.log($scope.login_form);
            $http.post('/user/login', $scope.login_form).success(function(data) {
                if (data === '0') {
                    $scope.login_message = "Cool";
                } else {
                    $scope.login_message = "Wrong credentials";
                }
                //console.log(data);
            });
        };

        $scope.register = function() {
            $http.post('/api/user/get', $scope.reg_form).success(function(data) {
                console.log(data);
            });
        };


        $scope.getCountries = function() {
            $http.get('/api/user/countries').success(function(data) {
                $scope.countries = data;
                console.log(data);
            });
        };

        $scope.getCountries();
        // $scope.loginForm();

        $scope.submit = function() {
            //  console.log($scope.userdata);
            $http.post('/ajax/user/create/', $scope.userdata).success(function(data) {

                console.log(data);
            });
        };
    }]);

djShopControllers.controller('ItemImagesCtrl', ['$scope', '$routeParams', '$http', '$sce',
    function($scope, $routeParams, $http) {

        //  console.log($scope.userdata);
        $http.get('ajax/item/images/' + $routeParams.itemId).success(function(data) {
            $scope.images = data;
            console.log(data);
        });

    }]);


djShopControllers.controller('UserPanelController', ['$scope', '$routeParams', '$http', '$sce',
    function($scope, $routeParams, $http) {



    }]);
