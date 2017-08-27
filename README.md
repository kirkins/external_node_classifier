# External Node Classifier

This script is the entry point for nodes connecting to puppet server.

It should be refered to in your `puppet.conf` file under `[master]`,
as attribute `external_nodes`. For example:

    [master]
    external_nodes = /etc/puppetlabs/node.py

It determines which configuration files to apply to the node.

This example contains 3 levels of classification.

1. check if over-ride groups exists for certname
2. check if pop machine model fact exists, if so use that
3. If no classification was found return default production branch

But you can make your own external node classifier for Puppet with
any logic you like, and any language you like.

As long as it can accept a certname and output a classification in
yaml format.
