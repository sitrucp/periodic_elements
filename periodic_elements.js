

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
    
    // sort elementsByOrigin by count desc
    elementsByOrigin.sort(function(x, y){
        return d3.ascending(x.element_count, y.element_count);
    })

    // create elements by origin axes x and y arrays
    var x = [];
    var y = [];
    for (var i=0; i<elementsByOrigin.length; i++) {
        row = elementsByOrigin[i];
        x.push( row['origin']);
        y.push( row['element_count']);
    }

    var trace1 = {
        x: y,
        y: x,
        orientation: 'h',
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
        title: {
            text: 'Periodic chart elements by origin',
            font: {
              size: 16
            }
        },
        barmode: 'stack',
        autosize: false,
        width: 500,
        height: 400,
        xaxis: {
            showgrid: false,
            showline: true,
            automargin: true,
            title: '# of elements',
            tickfont: {
                size: 12,
                color: 'black'
            },
        },
        yaxis: {
            showgrid: false,
            showline: true,
            automargin: true,
            tickformat: 'd',
        }
    };

    var config = {
        responsive: true,
        displayModeBar: false
    }

    Plotly.newPlot('chart', data, layout, config);


/////////////////
    // create chart of elements by origin source

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

    // sort sourceCountByElement by source_count asc
    sourceCountByElement.sort(function(x, y){
        return d3.ascending(x.source_count, y.source_count);
    })

    // create sourcecount axes x and y arrays
    var xc = [];
    var yc = [];
    for (var i=0; i<sourceCountByElement.length; i++) {
        row = sourceCountByElement[i];
        xc.push( row['source_count']);
        yc.push( row['element_count']);
    }

    var trace1c = {
        x: xc,
        y: yc,
        type: 'bar',
        text: yc.map(String),
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
        title: {
            text:'Periodic chart elements by number of origins',
            font: {
              size: 16
            }
        },
        barmode: 'stack',
        width: 500,
        height: 400,
        xaxis: {
            showgrid: false,
            showline: true,
            automargin: true,
            title: '# of origins',
            tickformat: 'd',
            tickfont: {
                size: 12,
                color: 'black'
            },
        },
        yaxis: {
            showgrid: false,
            showline: true,
            automargin: true,
            title: '# of elements',
            tickformat: 'd',
        }
    };

    var configc = {
        responsive: true,
        displayModeBar: false
    }

    Plotly.newPlot('chartc', datac, layoutc, configc);

});