(function() {
    var app = angular.module('youStatAnalyzer', []);

    app.controller('StatsController', ['$http', function($http) {
        var analyzer = this;

        analyzer.video = {};
        analyzer.vid = "";

        analyzer.updateStats = function() {
            try {
                $http.get('/stats.json', {params: {vid: analyzer.vid}}).then(
                    function (stats) {
                        analyzer.video.stats = stats;
                        createCumulativeViewsGraph(stats);
                    },
                    function () {
                        analyzer.video.stats = 'An error occurred.';
                    }
                );
            }
            catch (err) {
                alert("Error: " + err)
            }
        }
    } ]);
})();