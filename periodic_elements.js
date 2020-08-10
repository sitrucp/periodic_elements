

var file_elements = "https://raw.githubusercontent.com/sitrucp/periodic_elements/master/periodic_elements.csv";

Promise.all([
    d3.csv(file_elements),
]).then(function(data) {
    //everthing else below is in d3 promise scope
    // get data sets from promise
    var elements = data[0];

    // summarize elements by origin
    var elementsByOrigin = d3.nest()
        .key(function(d) { return d.source_word; })
        .rollup(function(v) { return v.length; })
        .entries(elements)
        .map(function(group) {
            return {
            origin: group.key,
            element_count: group.value
            }
        });

    // summarize elements by number of sources
    var sourceCountByElement = d3.nest()
    .key(function(d) { return d.source_count; })
    .rollup(function(v) { return v.length; })
    .entries(elements)
    .map(function(group) {
        return {
        source_count: group.key,
        element_count: group.value
        }
    });

    // sort elementsByOrigin by count desc
    sourceCountByElement.sort(function(x, y){
        return d3.ascending(x.source_count, y.source_count);
    })

    // create elements by origin axes x and y arrays
    var x = [];
    var y = [];
    for (var i=0; i<elementsByOrigin.length; i++) {
        row = elementsByOrigin[i];
        x.push( row['origin']);
        y.push( row['element_count']);
    }

    // create sourcecount axes x and y arrays
    var xc = [];
    var yc = [];
    for (var i=0; i<sourceCountByElement.length; i++) {
        row = sourceCountByElement[i];
        xc.push( row['source_count']);
        yc.push( row['element_count']);
    }

    var trace1 = {
        x: x,
        y: y,
        type: 'bar',
        text: y.map(String),
        textposition: 'auto',
        hoverinfo: 'none',
        marker: {
          color: '#d8d8d8',
          line: {
            color: '#d8d8d8',
            width: 1.5
          }
        }
      };

      var data = [trace1];

    var layout = {
        title: 'Periodic chart elements by origin',
        barmode: 'stack',
        xaxis: {
            showgrid: false,
            showline: true,
            automargin: true,
            tickfont: {
                size: 12,
                color: 'black'
              },
        },
        yaxis: {
            showgrid: false,
            showline: true,
            automargin: true,
        }
    };

    var design = {
        responsive: true,
        displayModeBar: false
    }

    Plotly.newPlot('chart', data, layout, design);



    var trace1c = {
        x: xc,
        y: yc,
        type: 'bar',
        text: y.map(String),
        textposition: 'auto',
        hoverinfo: 'none',
        marker: {
          color: '#d8d8d8',
          line: {
            color: '#d8d8d8',
            width: 1.5
          }
        }
      };

    var datac = [trace1c];

    var layoutc = {
        title: 'Periodic chart elements by number of origins',
        barmode: 'stack',
        xaxis: {
            showgrid: false,
            showline: true,
            automargin: true,
            tickfont: {
                size: 12,
                color: 'black'
              },
        },
        yaxis: {
            showgrid: false,
            showline: true,
            automargin: true,
        }
    };

    var designc = {
        responsive: true,
        displayModeBar: false
    }

    Plotly.newPlot('chartc', datac, layoutc, designc);

});