import subprocess
import os

class CppCodeCompiler:
    def __init__(self, code, filename):
        self.code = code 
        self.filename = "cpp-files/" + filename + ".cpp"
        self.base_filename = filename
        self.os_type = '.exe' if os.name == 'nt' else '.out'
        

    # g++ 01_test.cpp -Wall -o 01_test.exe
    def __compiler_cpp_code(self):
        cmd = ["g++", self.filename, "-Wall", "-o", self.base_filename + self.os_type]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = p.wait()
        a, b = p.communicate()
        self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
        return result
    
    # text.exe
    def __run_cpp_prog(self, cmd):
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = p.wait()
        a, b = p.communicate()
        self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
        return result

    def run_cpp_code(self):
        with open(self.filename, "w") as file:
            file.write(self.code)

        res = self.__compiler_cpp_code()
        result_compilation = self.stdout + self.stderr
        result_run = ""
        if res == 0:
            self.__run_cpp_prog(f"{self.base_filename}{self.os_type}")
            result_run = self.stdout + self.stderr
        return result_compilation, result_run


