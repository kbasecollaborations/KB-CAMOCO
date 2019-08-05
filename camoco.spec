/*
A KBase module: camoco
*/

module camoco {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef build_co_exp_network(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;
    funcdef parse_gwas(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;
    funcdef overlap_gwas_coexp(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;
  
};
