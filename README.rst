=================
ckanext-tolltheme
=================

Tolltheme is a CKAN extension to customize Tolletaten's (Norwegian Customs) CKAN installation for providing open data
to the public.

------------
Requirements
------------

This extension is developed for CKAN 2.8. See https://docs.ckan.org/en/2.8/theming/index.html for more info.

------------
Installation
------------

To install ckanext-tolltheme:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-tolltheme Python package into your virtual environment::

     pip install ckanext-tolltheme

3. Add ``tolltheme`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

To use the theme's default logo::

   ckan.site_logo = /tolletaten-logo.svg

Document any optional config settings here.::

    # The filters to show in on the left side on the dataset page.
    # Specified as a list of elements separated by spaces. Can be specified as the ckan facet key names or
    # the display titles in the chosen language. The value * can be used to include all the filters.
    # (optional, default: tags res_format, which maps to the Norwegian titles Stikkord and Formater)
    tolltheme.dataset.filters = Stikkord Formater Lisenser

------------------------
Development Installation
------------------------

To install ckanext-tolltheme for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/tolletaten/ckanext-tolltheme
    cd ckanext-tolltheme
    python setup.py develop
    pip install -r dev-requirements.txt


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.tolltheme --cover-inclusive --cover-erase --cover-tests


-------------------------------------
Registering ckanext-tolltheme on PyPI
-------------------------------------

ckanext-tolltheme should be availabe on PyPI as
https://pypi.python.org/pypi/ckanext-tolltheme. If that link doesn't work, then
you can register the project on PyPI for the first time by following these
steps:

1. Create a source distribution of the project::

     python setup.py sdist

2. Register the project::

     python setup.py register

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the first release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags


--------------------------------------------
Releasing a New Version of ckanext-tolltheme
--------------------------------------------

ckanext-tolltheme is availabe on PyPI as https://pypi.python.org/pypi/ckanext-tolltheme.
To publish a new version to PyPI follow these steps:

1. Update the version number in the ``setup.py`` file.
   See `PEP 440 <http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
   for how to choose version numbers.

2. Create a source distribution of the new version::

     python setup.py sdist

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the new release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.2 then do::

       git tag 0.0.2
       git push --tags
