djShop.directive('ctree',function () {
    return {
      templateUrl: '/static/partials/ctree/ctree.html',
      restrict: 'C',
     controller: function($scope, $element, $attrs,$http) {
        $scope.loadChildren=function () {
            
            $http.get('/api/ctree').success(function (data) {
                $scope.categories=data;
                console.log(data);
            });
        };   
     }
    
    };
}).directive('ctreeChild',function () {
    return {  
    templateUrl: '/static/partials/ctree/child.html',
    restrict: 'C'       
    };
});