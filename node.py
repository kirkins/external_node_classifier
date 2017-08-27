#!/usr/bin/env python
#
# Contains 3 levels of classification.
#
# 1. check if over-ride groups exists for certname
# 2. check if pop machine model fact exists, if so use that
# 3. If no classification was found return default production branch

import psycopg2
import sys
import json

from pypuppetdb import connect
db = connect(
  host='puppetdb',
  port=8080,
  ssl_verify=False,
  ssl_key=None,
  ssl_cert=None,
  timeout=20)

certname = sys.argv[1]

# setup connection
try:
  with open('/etc/puppetlabs/puppet/puppetDb.json') as data_file:
    puppetDbCreds = json.load(data_file)
  try:
    conn = psycopg2.connect("dbname='puppetdb' user='"+puppetDbCreds["user"]+"' host='"+puppetDbCreds["host"]+"' port='"+puppetDbCreds["port"]+"' password='"+puppetDbCreds["password"]+"'")
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GROUPS WHERE certname = '" + certname + "'")
    print 'environment: ' + cursor.fetchone()[2]
  except:
    try:
      node = db.node(certname)
      print 'environment: ' + node.fact('pop_machine_model').value
    except:
      print 'environment: production'
except:
  print 'environment: production'
