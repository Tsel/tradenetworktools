import pandas as pd

class TradeNetworkTool:
    """ Defines specific methods used in the analysis of trade networks """
    def __init__(self):
        self.fnedgelist = ""


    def readedgelist(self, fnedgelist, dtypes, dates=None):
        self.fnedgelist = fnedgelist
        """
        see also the comment in the from_edgelist method

        An edge list is the basic building block of the
        networks used as a model for animal trade between farms.

        As the name suggests, an edge list is a list of edges.
        Each line of an edge list corresponds to exactly one edge.
        Each line contains at least the names of the nodes connected
        by an edge and any other attributes of the edge.

        The list of edges is called el and the name of the file containing
        the data is called fnedgelist.

        The data of an edge list are read from cvs file (comma separated file)
        into a pandas dataframe, because here the possibilities of an extensive
        data processing exist. In addition, a pandas dataframe can be translated
        directly into a networkx graph.


        reads edgelist form csv and creates pandas dataframe
        scv file needs to have the following column header:

        S,T,VOL,"ZUGA_DATE","MELD_DATE",MELD_DELAY

        all columns except VOL and MELD_DELAY (which are of type int) are of type string

        :param fnedgelist:
        """

        if dates == None:
            return pd.read_csv(fnedgelist, sep=',',
                               dtype=dtypes
                               )

        return pd.read_csv(fnedgelist, sep=',',
                           dtype=dtypes,
                           parse_dates=dates,
                           infer_datetime_format=True
                           )



