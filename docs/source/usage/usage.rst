Usage
=====

The library needs a ``VersionSource`` object to work. To initiate a object of this type, you need a plugin that creates a type for this. Installation for the plugins will be documented by the plugin itself. After installing the plugin, you can use it to retrieve software:

.. code-block:: python

    from macpyver import MacPyVer, Software
    from macpyver_test_source import MacPyVerTestsource

    # First, you create a software object. This objects contains the name of the
    # software and additional information for the plugin to work. Which additional
    # information this is, is specific to the plugin. Please refer to the
    # documentation of the plugin to see what additional information is needed.
    my_software = Software(
        name='macpyver_core',
        extra_information={ 'github_repo': 'DarylStark/macpyver_core' })
    
    # Then you can create a MacPyVer object that gets the plugin as a VersionSource
    # class. This class is used to initialize a object that retrieves the version
    # information.
    macpyver = MacPyver(
        software=my_software,
        version_source=MacPyVerTestsource
    )

    # Now you can retrieve the versions
    versions = macpyver.get_all_versions()

This is the basic working of the library.