from src.reasoning.detected_object import DetectedObject


class ObjectPropertyExtractor:
    """
    Converts connected components into DetectedObject instances.
    """

    def extract(self, connected_components):
        """
        Parameters
        ----------
        connected_components : list
            List of ConnectedComponent objects.

        Returns
        -------
        list[DetectedObject]
        """
        objects = []

        for object_id, component in enumerate(connected_components, start=1):
            # Compute properties here
            pass

        return objects