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
    GIT_COMMIT_HASH = "b28eb7f18d73baa37b4c4ec16c716115c5042f5c"

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
        KBase Handling function
        :param params: instance of type "CoexpNetworkInputParams" ->
           structure: parameter "genome_ref" of type "GenomeRef" (Ref to a
           sequence set @id ws KBaseGenomes.Genome), parameter
           "association_ref" of type "AssociationRef" (Ref to a sequence set
           @id ws KBaseGwasData.Associations), parameter "exp_matrix_ref" of
           type "Expr_matrix_ref" (Ref to a sequence set @id ws
           KBaseMatrices.ExpressionMatrix), parameter "ontology" of type
           "ontology_dictionary" (Ref to an ontology dictionary @id ws
           KBaseOntology.OntologyDictionary), parameter "workspace_name" of
           String, parameter "workspace_id" of Long, parameter "window_size"
           of Long, parameter "flank_limit" of Long
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN build_co_exp_network

        #
        # Input validation:
        #
        # Reference: https://camoco.readthedocs.io/en/latest/tutorial.html
        #
        # What do we need?: Genome, GWAS Association, Assembly (from Genome), Expression data (trait matrix)
        #
        # How do we need it?: Everything is a KBase object. Genome will need to be downloaded as a GFF using GenomeFile-
        #   Util, then modified to suit camoco's ensemble GFF format. GWAS Associations object will need to read and
        #   turned into a delimited file with the column fields that match the camoco format, the trait matrix will need
        #   to be turned into a delimited file and GENEIDs validated
        if 'genome_ref' not in params:
            raise KeyError('Genome is required to build co-expression network with Camoco framework')

        if 'association_ref' not in params:
            raise KeyError('GWAS Associations are required to build co-expression network with Camoco framework')

        if 'exp_matrix_ref' not in params:
            raise KeyError('Expression matrix is required to build co-expression network with Camoco framework')

        if 'window_size' not in params:
            params['window_size'] = 1
        elif not isinstance(params['window_size'], int):
            try:
                params['window_size'] = int(params['window_size'])
            except TypeError:
                params['window_size'] = 1

        if 'flank_limit' not in params:
            params['flank_limit'] = 1
        elif not isinstance(params['flank_limit'], int):
            try:
                params['flank_limit'] = int(params['flank_limit'])
            except TypeError:
                params['flank_limit'] = 1

        #END build_co_exp_network

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method build_co_exp_network return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def buildrefgen(self, ctx, params):
        """
        Camoco wrapping function
        :param params: instance of type "BuildRefGenInputParams" ->
           structure: parameter "filename" of String, parameter "refgen_name"
           of String, parameter "description" of String
        :returns: instance of type "build_camoco_obj_out" -> structure:
           parameter "object_name" of type "camoco_obj_name" (Typdefs for
           camoco objects)
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN buildrefgen
        #END buildrefgen

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method buildrefgen return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def buildcob(self, ctx, params):
        """
        :param params: instance of type "BuildCOBInputParams" -> structure:
           parameter "filename" of String, parameter "cob_name" of String,
           parameter "description" of String, parameter "refgen_name" of
           String
        :returns: instance of type "build_camoco_obj_out" -> structure:
           parameter "object_name" of type "camoco_obj_name" (Typdefs for
           camoco objects)
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN buildcob
        #END buildcob

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method buildcob return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def buildontology(self, ctx, params):
        """
        :param params: instance of type "BuildOntologyInputParams" ->
           structure: parameter "filename" of String, parameter
           "ontology_name" of String, parameter "description" of String,
           parameter "refgen_name" of String
        :returns: instance of type "build_camoco_obj_out" -> structure:
           parameter "object_name" of type "camoco_obj_name" (Typdefs for
           camoco objects)
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN buildontology
        #END buildontology

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method buildontology return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def buildgwas(self, ctx, params):
        """
        :param params: instance of type "BuildGWASInputParams" -> structure:
           parameter "file_name" of String, parameter "obj_name" of type
           "camoco_obj_name" (Typdefs for camoco objects), parameter
           "description" of String, parameter "refgen_name" of type
           "camoco_obj_name" (Typdefs for camoco objects)
        :returns: instance of type "build_camoco_obj_out" -> structure:
           parameter "object_name" of type "camoco_obj_name" (Typdefs for
           camoco objects)
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN buildgwas
        #END buildgwas

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method buildgwas return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def overlapgwas(self, ctx, params):
        """
        :param params: instance of type "FindGWASCoexpOverlapParams" ->
           structure: parameter "window_size" of Long, parameter
           "flank_limit" of Long, parameter "snp2gene_map" of String,
           parameter "strongest_attr" of String
        :returns: instance of type "build_camoco_obj_out" -> structure:
           parameter "object_name" of type "camoco_obj_name" (Typdefs for
           camoco objects)
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN overlapgwas
        #END overlapgwas

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method overlapgwas return value ' +
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
