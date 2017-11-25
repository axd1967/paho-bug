qos=2 bug
=========

Preparation
+++++++++++

#. Install Vagrant
#. create a running VM
#. start client

.. code-block:: bash

    cd components/vagrant
    vagrant up srv-def cli-def
    vagrant ssh cli-def
    cd python/client
    source venv/bin/activate
    python cli.py
    pdb stops; enter 'c' to continue and demonstrate the bug
