from polymath.app import *
from sample.service.library import *
from sample.service.sample import *

class AppDelegate(Application.Delegate):
    def application_did_launch(self, app: Application):
        library = LibraryService(name="library", serving_path="/library")
        app.add_service(library)

        sample = SampleService(name="sample", serving_path="/sample")
        app.add_service(sample)



