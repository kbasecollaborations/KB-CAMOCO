# -*- coding: utf-8 -*-
import os
import time
import unittest
from configparser import ConfigParser
from pprint import pprint as pp

from camoco.camocoImpl import camoco
from camoco.camocoServer import MethodContext
from camoco.authclient import KBaseAuth as _KBaseAuth

from installed_clients.WorkspaceClient import Workspace


class camocoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = os.environ.get('KB_AUTH_TOKEN', None)
        config_file = os.environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('camoco'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'camoco',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = Workspace(cls.wsURL)
        cls.serviceImpl = camoco(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']
        suffix = int(time.time() * 1000)
        cls.wsName = "test_ContigFilter_" + str(suffix)
        ret = cls.wsClient.create_workspace({'workspace': cls.wsName})  # noqa

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    # NOTE: According to Python unittest naming rules test method names should start from 'test'. # noqa
    def test_ref_data(self):
        # Prepare test objects in workspace if needed using
        # self.getWsClient().save_objects({'workspace': self.getWsName(),
        #                                  'objects': []})
        #
        # Run your method by
        # ret = self.getImpl().your_method(self.getContext(), parameters...)
        #
        # Check returned data with
        # self.assertEqual(ret[...], ...) or other unittest methods

        # This test will build all the camoco objects using impl functions and data provided from the reference data
        # mount. This data is provided by camoco, and roughly follows there tutorial process, and can be accessed here:
        # https://camoco.readthedocs.io/en/latest/tutorial.html . Check out scripts/entrypoint.sh to see how reference
        # data is downloaded and processed

        pp(os.listdir('/data'))

        # Refgen data
        if os.path.exists('/data/ZmB73_5b_FGS.gff'):
            self.refgen_file = '/data/ZmB73_5b_FGS.gff'
        else:
            raise FileNotFoundError('RefGen reference data does not exist at: /data/ZmB73_5b_FGS.gff')

        # Expression data
        if os.path.exists('/data/Hirsch2014_PANGenomeFPKM.txt'):
            self.expr_file = '/data/Hirsch2014_PANGenomeFPKM.txt'
        else:
            raise FileNotFoundError('Expression reference data does not exist at: /data/Hirsch2014_PANGenomeFPKM.txt')

        # Ontology base data
        if os.path.exists('/data/go.obo'):
            self.base_ontology_file = '/data/go.obo'
        else:
            raise FileNotFoundError('Base ontology reference data does not exist at: /data/go.obo')

        # Maize ontology data
        if os.path.exists('/data/zm_go.tsv'):
            self.maize_ontology_file = '/data/zm_go.tsv'
        else:
            raise FileNotFoundError('Maize ontology reference data does not exist at: /data/zm_go.tsv')

        if os.path.exits('/data/ZmIonome.allLocs.csv'):
            self.maize_gwas_file = '/data/ZmIonome.allLocs.csv'
        else:
            raise FileNotFoundError('Maize GWAS reference data does not exist at: /data/ZmIonome.allLocs.csv')