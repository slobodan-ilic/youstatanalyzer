function createStatsGraph(stats, selector, type) {
    try {
        var data, g, days, drawStats, graphDiv;
        graphDiv = document.getElementById('statsGraph');

        if (stats.hasOwnProperty('day')) {
            days = stats.day.data;
            drawStats = stats[selector][type].data;

            data = "day, " + selector + "\n";
            for (var i = 0; i < days.length; i++) {
                var x = String(new Date(days[i]));
                var y = drawStats[i];
                data += x + ', ' + y + '\n';
            }

            g = new Dygraph(graphDiv, data, {});
        }
        else {
            g = new Dygraph(graphDiv, '', {});
        }

        return g;
    }
    catch (exc) {
        alert('Error: ' + exc)
    }
}
