var file_hr_lookup = "https://raw.githubusercontent.com/sitrucp/canada_covid_health_regions/master/health_regions_lookup.csv";
//var file_case_days = "https://canada-covid-data.s3.amazonaws.com/case_last_dates.csv";

Promise.all([
    d3.csv(file_cases),
    d3.csv(file_mortality),
    d3.csv(file_update_time),
    d3.csv(file_hr_lookup),
    //d3.csv(file_case_days)
]).then(function(data) {
    //everthing else below is in d3 promise scope
    // get data sets from promise
    var cases = data[0];
    var mortalities = data[1];
    var updateTime = data[2];
    var regionLookup = data[3];
    //var caseDays = data[4];