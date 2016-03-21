function createCumulativeViewsGraph(stats) {

    var data, g, days, cumulativeViews;

    days = stats['data']['day']['data'];
    cumulativeViews = stats['data']['views']['cumulative']['data'];

    data = "Day, Views\n";
    for (var i = 0; i < days.length; i++) {
        data += days[i] + ', ' + cumulativeViews[i] + '\n';
    }

    g = new Dygraph(document.getElementById('statsGraph'), data, {});
}
