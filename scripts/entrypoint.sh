#!/bin/bash

. /kb/deployment/user-env.sh

python ./scripts/prepare_deploy_cfg.py ./deploy.cfg ./work/config.properties

if [ -f ./work/token ] ; then
  export KB_AUTH_TOKEN=$(<./work/token)
fi

if [ $# -eq 0 ] ; then
  sh ./scripts/start_server.sh
elif [ "${1}" = "test" ] ; then
  echo "Run Tests"
  make test
elif [ "${1}" = "async" ] ; then
  sh ./scripts/run_async.sh
elif [ "${1}" = "init" ] ; then
  echo "Initialize module"

  # start in data folder
  cd /data

  # camoco tutorial and maize reference data
  # tutorial: https://camoco.readthedocs.io/en/latest/tutorial.html
  RefGen=https://github.com/LinkageIO/Camoco/raw/master/tests/raw/RefGen/ZmB73_5b_FGS.gff.gz
  RefGenfile=${RefGen##*/}

  Expr1=https://github.com/LinkageIO/Camoco/raw/master/tests/raw/Expr/RNASEQ/Hirsch2014_PANGenomeFPKM.txt.gz
  Expr1file=${Expr1##*/}

  GOBASE=https://github.com/LinkageIO/Camoco/raw/master/tests/raw/GOnt/go.obo.gz
  GOBASEfile=${GOBASE##*/}

  GOZM=https://github.com/LinkageIO/Camoco/raw/master/tests/raw/GOnt/zm_go.tsv.gz
  GOZMfile=${GOZM##*/}

  GWASZM=https://github.com/LinkageIO/Camoco/raw/master/tests/raw/GWAS/SchaeferPlantCell/ZmIonome.allLocs.csv.gz
  GWASZMfile=${GWASZM##*/}

  # Expr2=https://github.com/LinkageIO/Camoco/raw/master/tests/raw/Expr/RNASEQ/Stelpflug2018_B73_Tissue_Atlas.txt.gz
  # Expr3=https://github.com/LinkageIO/Camoco/raw/master/tests/raw/Expr/RNASEQ/Schaefer2018_ROOTFPKM.tsv.gz
  # GWASZM2=https://github.com/LinkageIO/Camoco/raw/master/tests/raw/GWAS/WallacePLoSGenet/Wallace_etal_2014_PLoSGenet_GWAS_hits-150112.txt.gz

  # cURL this data, follow github redirects (-L), preserve filename (-O), keep silent (-s) and accept only gzip
  #     files (-H), then decompress with gunzip and bash string manipulation "${URL##*/}"

  curl -L -sH 'Accept-encoding: gzip' -O "${RefGen}" && gunzip -f "${RefGenfile}"
  curl -L -sH 'Accept-encoding: gzip' -O "${Expr1}" && gunzip -f "${Expr1file}"
  curl -L -sH 'Accept-encoding: gzip' -O "${GOZM}" && gunzip -f "${GOZMfile}"
  curl -L -sH 'Accept-encoding: gzip' -O "${GOBASE}" && gunzip -f "${GOBASEfile}"
  curl -L -sH 'Accept-encoding: gzip' -O "${GWASZM}" && gunzip -f "${GWASZMfile}"

  # curl -L -sH 'Accept-encoding: gzip' -O "${Expr2}" && gunzip -f "${Expr2##*/}"
  # curl -L -sH 'Accept-encoding: gzip' -O "${Expr3}" && gunzip -f "${Expr3##*/}"
  # curl -L -sH 'Accept-encoding: gzip' -O "${GWASZM2}" && gunzip -f "${GWASZM2##*/}"

  if [ -f "/data/${RefGenfile::-3}" && -f "/data/${Expr1file::-3}" && -f "/data/${GOBASEfile::-3}" && -f "/data/${GOZMfile::-3}" && -f "/data/${GWASZMfile::-3}"]; then
    touch __READY__
  else
    echo "Init failed"
  fi
elif [ "${1}" = "bash" ] ; then
  bash
elif [ "${1}" = "report" ] ; then
  export KB_SDK_COMPILE_REPORT_FILE=./work/compile_report.json
  make compile
else
  echo Unknown
fi
