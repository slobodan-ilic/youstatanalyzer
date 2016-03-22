(function() {
    var app = angular.module('youStatAnalyzer', []);

    app.controller('StatsController', ['$http', function($http) {
        var analyzer = this;

        analyzer.tab = 'Cumulative Views';
        analyzer.stats = {};
        analyzer.g = {};
        analyzer.title = '';

        analyzer.updateStats = function() {
            try {
                $http.get('/stats.json', {params: {vid: analyzer.vid}}).then(
                    function (stats) {
                        if (stats.data === 'Could not fetch data.') {
                            analyzer.title = "No statistics for this video."
                            return
                        }
                        analyzer.stats = stats.data;
                        analyzer.title = stats.data.title;
                        analyzer.g = analyzer.drawGraph();
                    },
                    function () {
                        analyzer.stats = 'An error occurred.';
                    }
                );
            }
            catch (err) {
                alert("Error: " + err)
            }
        };

        analyzer.drawGraph = function(tab) {
            analyzer.tab = tab || analyzer.tab;
            if (analyzer.tab === 'Cumulative Views') {
                analyzer.g = createStatsGraph(analyzer.stats, "views", 'cumulative');
            }
            else if (analyzer.tab === 'Daily Views') {
                analyzer.g = createStatsGraph(analyzer.stats, 'views', 'daily');
            }
            else if (analyzer.tab === 'Daily Shares') {
                analyzer.g = createStatsGraph(analyzer.stats, 'shares', 'daily');
            }
            else if (analyzer.tab === 'Cumulative Shares') {
                analyzer.g = createStatsGraph(analyzer.stats, 'shares', 'cumulative');
            }
            else if (analyzer.tab === 'Daily Subscribers') {
                analyzer.g = createStatsGraph(analyzer.stats, 'subscribers', 'daily');
            }
            else if (analyzer.tab === 'Cumulative Subscribers') {
                analyzer.g = createStatsGraph(analyzer.stats, 'subscribers', 'cumulative');
            }
            else if (analyzer.tab === 'Daily Watch-Time') {
                analyzer.g = createStatsGraph(analyzer.stats, 'watch-time', 'daily');
            }
            else if (analyzer.tab === 'Cumulative Watch-Time') {
                analyzer.g = createStatsGraph(analyzer.stats, 'watch-time', 'cumulative');
            }
        };
    } ]);
})();