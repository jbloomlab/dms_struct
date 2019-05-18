"""
==============
struct_widget
==============

Get `nglview <https://github.com/arose/nglview>`_ protein structure widgets.
"""


import os
import secrets
from urllib.error import HTTPError

import nglview


def colored_struct(*,
                   pdb,
                   prop_df,
                   chain_col='chain',
                   site_col='site',
                   color_col='color',
                   representation='cartoon',
                   highlight_col=None,
                   highlight_representation='spacefill',
                   show_other=False,
                   other_color='#FFFFFF',
                   orientation=None,
                   ):
    """Create widget showing a colored structure.

    Parameters
    ------------
    pdb : str
        Existing PDB file, or ID to be downloaded from PDB.
    prop_df : pandas DataFrame
        Data on sites to show and how to color them. You are responsible for
        ensuring that chaing / site labels are consistent with those in `pdb`,
        no automatic checks of this are performed.
    chain_col: str
        Column in `prop_df` with PDB chain ID.
    site_col : str
        Column in `prop_df` with PDB site numbers.
    color_col : str
        Column in `prop_df` with color for each site.
    representation : str
        Protein representation (e.g., 'cartoon', 'surface', 'spacefill',
        or other `nglview <https://github.com/arose/nglview>`_ representation.
    highlight_col : str or `None`
        Optional column of boolean values in `prop_df` indicating
        sites to also draw in `highlight_representation`.
    highlight_representation : str
        Additional representation for sites specified in `highlight_col`.
    show_other : `False` or str
        Show selections **not** listed as sites in `prop_df`? If so, specify
        those selections. Can be 'all', 'protein', or other selection string
        (`see here <https://github.com/arose/ngl/tree/master/doc/usage>`_).
    other_color : str
        Color for any sites not in `prop_df` but shown via `show_other`.
    orientation : `None` or list of 16 numbers
        Orientation to show the structure, can be obtained via the
        `_camera_orientation` property of a structure widget
        (https://github.com/arose/nglview/issues/785#issuecomment-487409212).

    Returns
    --------
    nglview.widget.NGLWidget
        The widget can be shown in a Jupyter notebook.

    """
    # error checking on `prop_df` and its columns
    cols = []
    for colname, col, optional in [('color_col', color_col, False),
                                   ('site_col', site_col, False),
                                   ('chain_col', chain_col, False),
                                   ('highlight_col', highlight_col, True),
                                   ]:
        if col is None:
            if not optional:
                raise ValueError(f"must specify `{colname}`")
        elif col not in prop_df.columns:
            raise ValueError(f"`prop_df` lacks `{colname}` of {col}")
        elif col in cols:
            raise ValueError(f"duplicate column names of {col}")
        else:
            cols.append(col)

    prop_df = (prop_df
               [cols]
               .drop_duplicates()
               )

    if len(prop_df) != len(prop_df.groupby([chain_col, site_col])):
        raise ValueError('Inconsistent duplicated rows for some sites in '
                         '`prop_df`. For each chain and site, entries must '
                         f"be the same for all rows in these columns: {cols}")

    # get PDB into a widget; use `default_representation=False` as here:
    # https://github.com/arose/nglview/issues/802#issuecomment-492760630
    if os.path.isfile(pdb):
        w = nglview.show_structure_file(pdb,
                                        default_representation=False,
                                        )
    else:
        try:
            w = nglview.show_pdbid(pdb,
                                   default_representation=False,
                                   )
        except HTTPError:  # noqa: F821
            raise ValueError(f"`pdb` {pdb} does not specify an existing "
                             'PDB file or an ID that can be downloaded')

    # Set up color schemes as here:
    # https://github.com/arose/nglview/pull/755
    # For details on selection strings, see here:
    # https://github.com/arose/ngl/blob/master/doc/usage/selection-language.md
    colorscheme = []
    selectionlist = []
    highlight_colorscheme = []
    highlight_selectionlist = []
    for row in prop_df.itertuples():
        color = getattr(row, color_col)
        sel_str = f":{getattr(row, chain_col)} and {getattr(row, site_col)}"
        selectionlist.append(f"({sel_str})")
        colorscheme.append([color, sel_str])
        if highlight_col and getattr(row, highlight_col):
            highlight_selectionlist.append(f"({sel_str})")
            highlight_colorscheme.append([color, sel_str])
    colorscheme.append([other_color, '*'])

    selection = ', '.join(selectionlist)
    if show_other:
        selection = f"({show_other}) or ({selection})"
    # uniquely label color schemes as here:
    # https://github.com/arose/nglview/issues/802#issuecomment-492501051
    colorscheme = nglview.color._ColorScheme(
                                colorscheme,
                                label=f"colorscheme_{secrets.token_hex(10)}",
                                )
    highlight_selection = ', '.join(highlight_selectionlist)
    highlight_colorscheme = nglview.color._ColorScheme(
                                highlight_colorscheme,
                                label=f"colorscheme_{secrets.token_hex(10)}",
                                )

    # color and style widget; set assembly to BU1 (biological unit 1) as here:
    # https://github.com/arose/ngl/blob/master/doc/usage/selection-language.md
    w.clear_representations()
    w.add_representation(representation,
                         selection=selection,
                         color=colorscheme,
                         assembly='BU1',
                         )
    if highlight_representation and highlight_selection:
        w.add_representation(highlight_representation,
                             selection=highlight_selection,
                             color=highlight_colorscheme,
                             assembly='BU1',
                             )

    if orientation:
        if len(orientation) != 16:
            raise ValueError('`orientation` not list of 16 numbers')
        w._set_camera_orientation(orientation)

    return w


if __name__ == '__main__':
    import doctest
    doctest.testmod()
