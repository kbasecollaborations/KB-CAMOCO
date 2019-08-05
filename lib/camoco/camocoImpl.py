# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
#END_HEADER


class camoco:
    '''
    Module Name:
    camoco

    Module Description:
    A KBase module: camoco
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/kbasecollaborations/KB-CAMOCO.git"
    GIT_COMMIT_HASH = "32eff3d31d8fc077e83c025447ff0e454c84c363"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def build_co_exp_network(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of type "CoexpNetworkInputParams" ->
           structure: parameter "genome_ref" of type "GenomeRef" (Ref to a
           sequence set @id ws KBaseGenomes.Genome), parameter
           "association_ref" of type "AssociationRef" (Ref to a sequence set
           @id ws KBaseGwasData.Associations)
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN build_co_exp_network
        #END build_co_exp_network

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method build_co_exp_network return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def parse_gwas(self, ctx, params):
        """
        :param params: instance of type "ParseGWASInputParams" -> structure:
           parameter "assembly_ref" of type "Assembly_ref" (Reference to an
           Assembly object in the workspace @id ws
           KBaseGenomeAnnotations.Assembly), parameter "association_ref" of
           type "AssociationRef" (Ref to a sequence set @id ws
           KBaseGwasData.Associations), parameter "matrix_ref" of type
           "Trait_matrix_ref" (Ref to a sequence set @id ws
           KBaseMatrices.TraitMatrix)
        :returns: instance of type "build_camoco_obj_out" -> structure:
           parameter "object_name" of type "camoco_obj_name" (Name of created
           and returned camoco object)
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN parse_gwas
        output = {}
        #END parse_gwas

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method parse_gwas return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def overlap_gwas_coexp(self, ctx, params):
        """
        :param params: instance of type "FindGWASCoexpOverlapParams" ->
           structure: parameter "window_size" of Long, parameter
           "flank_limit" of Long, parameter "snp2gene_map" of String,
           parameter "strongest_attr" of String
        :returns: instance of type "build_camoco_obj_out" -> structure:
           parameter "object_name" of type "camoco_obj_name" (Name of created
           and returned camoco object)
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN overlap_gwas_coexp
        #END overlap_gwas_coexp

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method overlap_gwas_coexp return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
