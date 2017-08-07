from conans import ConanFile, CMake
import os

channel = os.getenv("CONAN_CHANNEL", "stable")
username = os.getenv("CONAN_USERNAME", "tanker")

class SnappyTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "zlib/1.2.11@%s/%s" % (username, channel)
    #default_options = "zlib:system=True", "zlib:root=/tmp/sss", "zlib:shared=true"
    default_options = "zlib:shared=True"
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        os.chdir("bin")
        self.run(".%stestapp" % os.sep)
