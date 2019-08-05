/*
A KBase module: camoco
*/

module camoco {
    /* Ref to a sequence set
        @id ws KBaseGenomes.Genome
    */
    typedef string GenomeRef;

    /* Ref to a sequence set
       	@id ws KBaseGwasData.Associations
    */
    typedef string AssociationRef;

    /* Reference to an Assembly object in the workspace
    		@id ws KBaseGenomeAnnotations.Assembly
    */
    typedef string Assembly_ref;

    /* Ref to a sequence set
    		@id ws KBaseMatrices.TraitMatrix
    */
		typedef string Trait_matrix_ref;

    typedef structure {
        GenomeRef genome_ref;
        AssociationRef association_ref;
        Trait_matrix_ref trait_matrix_ref;
        string workspace_name;
        int workspace_id;
    } CoexpNetworkInputParams;

    typedef structure {
        Assembly_ref assembly_ref;
        AssociationRef association_ref;
				Trait_matrix_ref matrix_ref;
    } ParseGWASInputParams;

    typedef structure {
        int window_size;
        int flank_limit;
        string snp2gene_map;
        string strongest_attr;
    } FindGWASCoexpOverlapParams;

    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        Name of created and returned camoco object
    */
    typedef string camoco_obj_name;

    typedef structure {
        camoco_obj_name object_name;
    } build_camoco_obj_out;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef build_co_exp_network(CoexpNetworkInputParams params) returns (ReportResults output) authentication required;
    funcdef parse_gwas(ParseGWASInputParams params) returns (build_camoco_obj_out output) authentication required;
    funcdef overlap_gwas_coexp(FindGWASCoexpOverlapParams params) returns (build_camoco_obj_out output) authentication required;
};
