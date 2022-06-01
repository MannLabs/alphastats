from alphastats.loader import BaseLoader
import pandas as pd

class MaxQuantLoader(BaseLoader):
    def __init__(self,
        file,
        intensity_column = "LFQ intentsity [experiment]",
        index_column = "Protein IDs",
        filter_columns = ["Only identified by site", "Reverse", "Potential contaminant"],
        qvalue_column = "Q-value",
        sep = "\t"):
        """_summary_

        Args:
            intensity_column (str, optional): _description_. Defaults to "LFQ intentsity [experiment]".
            index_column (str, optional): _description_. Defaults to "Protein IDs".
            filter_columns (list, optional): _description_. Defaults to ["Only identified by site", "Reverse", "Potential contaminant"].
            qvalue_column (str, optional): _description_. Defaults to "Q-value".
        """
        super.__init__(file, intensity_column, index_column, sep)
        self.filter_columns = filter_columns
        self.qvalue_column = qvalue_column
        self.software = "MaxQuant"
    
    def filter_contaminations(self):
        # make class method as other softwares don't annotate contaminations??
        pass

        
    def preprocess_contamination(self):
        # remove columns where +
        pass

    def annotate_contamination(self):
        pass
