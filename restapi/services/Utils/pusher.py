from .converter import Converter


class Pusher(object):

    def __init__(self, df=None, obj_list=None):
        # Accepts list of objects and df
        self.df = df
        self.obj_list = obj_list
        self.converter = Converter(df=self.df, obj_list=self.obj_list)

    def get_obj_list(self, base_obj):
        # If df is given, convert to list of obj
        if self.converter.validate_df():
            self.obj_list = self.converter.to_obj_list(base_obj=base_obj)

        return self.obj_list

    def push(self, base_obj):
        # Pushes the list of objects to DB
        self.obj_list = self.get_obj_list(base_obj)
        try:
            for obj in self.obj_list:
                if not (obj in base_obj.objects.all()):
                    obj.save()

        except Exception as e:
            raise e
