from nansat.mappers.mapper_arome import Mapper as MapperArome
from nansat.mappers.opendap import Opendap
from nansat.tools import WrongMapperError

class Mapper(Opendap, MapperArome):

    baseURLs = ['http://thredds.met.no/thredds/catalog/arome25/catalog.html']

    def __init__(self, *args, **kwargs):

        fn = args[0]
        #ds = args[1] - None
        #mm = args[2] - None

        import ipdb
        ipdb.set_trace()

        self.test_mapper(fn)
