=========
Examples
=========

.. contents::
   :local:

How to run the examples
------------------------------
``dms_struct`` uses nglview_ to create interactive structure widgets in a `Jupyter notebook`_.
These structure widgets are rendered in a browser.
Therefore, you need to run them interactively by opening `Jupyter notebook`_.

To make this easy, the examples below are provided as links to mybinder_ interactive notebooks.
Once you have opened the notebooks in mybinder_, you may have to wait a minute for everything to load.
When the notebooks load, they will show some existing output--but the structure widgets will not be properly rendered.
To get them to render, you need to re-run the notebooks.
Furthermore, they take some time to render, so run the notebooks **cell-by-cell** to allow time for each widget to render.

Creating structure widgets
----------------------------
This example shows how to use :func:`dms_struct.struct_widget.colored_struct` to create appropriately colored nglview_ structure widgets.
`Click here <https://mybinder.org/v2/gh/jbloomlab/dms_struct/master?filepath=notebooks/struct_widget.ipynb>`__ to open the example in mybinder_.

Interactive visualization and static image of mutational antigenic profiling data 
---------------------------------------------------------------------------------
This example shows how to analyze a real data set in order to create both an interactive visualization and a static image appropriate for a paper figure.
It shows mutational antigenic profiling of the immune selection from influenza sera.

The notebook is designed so that it is possible to visualize the results as an interactive app using appmode_; this app can then be directly provided as a link to allow people to interactively view the structures.

First, `click here <https://mybinder.org/v2/gh/jbloomlab/dms_struct/master?urlpath=%2Fapps%2Fnotebooks/flu_sera_map.ipynb>`__ to visualize in appmode_ (you may have to wait a minute for it to load).
Note how the structures are interactive, and can be rotated and clicked on to get site numbers.

To look at the actual notebook (**not** in appmode_), `click here <https://mybinder.org/v2/gh/jbloomlab/dms_struct/master?filepath=notebooks/flu_sera_map.ipynb>`__.
You can run the actual notebook cell-by-cell (wait for widgets to render before going to then next cell!) and the notebook will also produce a static image that can be used as a figure (to view that figure, you need to uncomment the ``display`` command in the last cell).
The notebook is written without much in the way of Markdown descriptions; this is to avoid extraneous Markdown text in the appmode_ rendering.

The notebook can be used as a template to make your own similar notebooks.
To do that, use the following steps:

 1. Download the notebook by :download:`clicking here <../notebooks/flu_sera_map.ipynb>`.

 2. Re-configure the notebook to analyze your data.
    The configuration is specified by the *parameters* cell that is the third code cell in the notebook.
    For instance, this cell specifies that the notebook is currently configured to analyze the data in a file called ``data/Lee_serum_mapping.csv`` (:download:`click here <../notebooks/data/Lee_serum_mapping.csv>` to look at this file).
    It also specifies information about which columns in this CSV file to plot, the PDB to use, etc.
    Note also that this cell is tagged as a *parameters* cell, meaning that you can use `papermill parameterization <https://papermill.readthedocs.io>`_.

 3. To enable your new notebook to be opened in mybinder_, you need to put it in a GitHub repo that contains a ``./binder/`` subdirectory with the `binder configuration <https://mybinder.readthedocs.io/en/latest/config_files.html>`_.
    You can copy the binder configuration for this example from `here <https://github.com/jbloomlab/dms_struct/tree/master/binder>`__.

 4. To create a link to an interactive version of your notebook, follow the instructions on the mybinder_ page.
    For instance, the link for this example is https://mybinder.org/v2/gh/jbloomlab/dms_struct/master?filepath=notebooks/flu_sera_map.ipynb.
    To make the link open in appmode_ (useful if you just want to share the interactive visualization), replace the ``filepath=`` with ``urlpath=%2Fapps%2F`` in the above weblink `as described here <https://github.com/oschuett/appmode/issues/13>`__.
    For this example, the link is therefore https://mybinder.org/v2/gh/jbloomlab/dms_struct/master?urlpath=%2Fapps%2Fnotebooks/flu_sera_map.ipynb.
    

.. _nglview: https://github.com/arose/nglview
.. _`Jupyter notebook`: https://jupyter.org/
.. _mybinder: https://mybinder.org/
.. _appmode: https://github.com/oschuett/appmode
