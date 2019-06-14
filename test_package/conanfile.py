from conans.model.conan_file import ConanFile
from conans import CMake
import os


class AndroidNdkTestConan(ConanFile):
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"

    def configure(self):
        if self.settings.os != "Android":
            raise Exception("os must be Android")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        bin_path = os.path.join("bin", "test_package")
        # Ensure it fails
        try:
            self.run(bin_path, run_environment=True)
        except:
            pass
        else:
            raise Exception("Cross building failed!")
